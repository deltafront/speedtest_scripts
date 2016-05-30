import datetime
import json
from os import listdir
import os
from os.path import isfile, join
from companyB.configs import date_time_format

__author__ = 'charlie'


def get_timestamp():
    now = datetime.datetime.now()
    timestamp = now.strftime(date_time_format)
    return timestamp


def get_output(path_to_file):
    """
    Example File Output:
    Ping: 5.402 ms
    Download: 39.47 Mbit/s
    Upload: 11.47 Mbit/s
    Share results: http://www.speedtest.net/result/5327551818.png
    """
    print('Processing output from %s' % path_to_file)

    def get_and_replace(line_of_text, term, *replacements):
        result = None
        if term in line_of_text:
            result = line_of_text.replace(term, '')
            for replacement in replacements:
                result = result.replace(replacement, '')
            result = result.trim()
        return result

    timestamp = get_timestamp()
    ping = None
    download = None
    upload = None
    share_results = None
    f = open(path_to_file, 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        if ping is None:
            ping = get_and_replace(line, 'Ping', 'ms', ':')
        if download is None:
            download = get_and_replace(line, 'Download', 'Mbit/s', ':')
        if upload is None:
            upload = get_and_replace(line, 'Upload', 'Mbit/s', ':')
        if share_results is None:
            share_results = get_and_replace(line, 'Share results:')
    message = 'Ping=%s, Upload=%s, Download=%s, Share_Results=%s' % (ping, upload, download, share_results)
    print('Output processed. Returning values %s' % message)
    return timestamp, ping, upload, download, share_results


def generate_json_data(timestamp, ping, upload, download, share_results):
    mapping = {'timestamp': timestamp, 'ping': ping, 'upload': upload, 'download': download,
               'share_results': share_results}
    result = json.dumps(mapping)
    print('Returning json mapping\n%s' % result)
    return result


def generate_csv_data(timestamp, ping, upload, download, share_results):
    first_line = '#timestamp,ping,upload,download,share_results'
    second_line = '%s,%s,%s,%s,%s' % (timestamp, ping, upload, download, share_results)
    print('Returning CSV output:\n%s\n%s' % (first_line, second_line))
    return [first_line, second_line]


def get_files(path):
    return [f for f in listdir(path) if isfile(join(path, f))]


def delete_file(file_descriptor):
    os.remove(file_descriptor)

