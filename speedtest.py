from datetime import datetime
import json
from pytz import timezone
from dropbox.files import WriteMode
from cleanup_utils import clean_dir
from configs import speedtest_file_loc, workbook_name, dropbox_file_name, email_date_time_format, default_timezone
from dropbox_utils import upload_to_dropbox, get_file_from_dropbox
from emailer import ping_service, construct_request_body, send_email_request
from mongo_utils import save_to_mongo
from speedtest_utils import make_directories, get_speedtest_file_name, get_output, generate_json_data, generate_csv_data
from utils import get_timestamp

__author__ = 'charlie'
import os
import subprocess


def main():
    print('Running speedtest')
    cmd = 'speedtest --simple --share'
    print('Checking to see if %s exists' % speedtest_file_loc)
    if not os.path.exists(speedtest_file_loc):
        print('Creating directory structure at %s' % speedtest_file_loc)
        make_directories()
    filename = get_speedtest_file_name()
    print('Running speedtest and pushing results to %s' % filename)
    logfile = open(filename, 'w')
    p = subprocess.Popen(cmd, shell=True, universal_newlines=True, stdout=logfile)
    ret_code = p.wait()
    logfile.flush()
    logfile.close()
    print(ret_code)
    print('Log published at %s.' % filename)
    print('Processing logfile output')
    (timestamp, ping, upload, download, share_results) = get_output(filename)
    print('Generating JSON data for insertion into Mongo.')
    json_data = generate_json_data(timestamp,ping,upload,download,share_results)
    print('Generating CSV data.')
    csv_data = generate_csv_data(timestamp, ping, upload, download, share_results)
    print('Writing out CSV data.')
    csv_file = get_file_from_dropbox(dropbox_file_name)
    write_mode = WriteMode.add
    if csv_file is None:
        csv_file = workbook_name
        print("Creating new CSV file.")
        f = open(csv_file, 'w')
        f.write(csv_data[0])
        f.write(csv_data[1])
        f.close()
    else:
        print("Appending existing file.")
        f = open(csv_file, 'a')
        f.write(csv_data[1])
        f.close()
        write_mode = WriteMode.overwrite
    print('Uploading workbook to Dropbox.')
    upload_to_dropbox(csv_file, dropbox_file_name, write_mode=write_mode)
    print('Inserting data into Mongo.')
    save_to_mongo([json.loads(json_data)])
    print('Pinging service in order to send email.')
    if ping_service():
        print('Sending email')
        email_timestamp = get_timestamp(dt_format=email_date_time_format)
        request_mapping = construct_request_body(email_timestamp,ping, upload, download, share_results, type_='speedtest')
        send_email_request(request_mapping)
    print('Cleaning up.')
    clean_dir(speedtest_file_loc)
    print('Done.')

if __name__ == '__main__':
    main()