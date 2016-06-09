import json
import os
from unittest import TestCase
from configs import speedtest_file_loc, spreadsheet_date_time_format
from utils import get_timestamp

__author__ = 'charlie'

def get_speedtest_file_name():
    return '%s/%s.speedtest.log' % (speedtest_file_loc, get_timestamp())


def make_directories():
    print('Making directories.')
    home = os.getenv('HOME')
    logs_loc = '%s/logs' % home
    make_dir(logs_loc)
    speedtest_logs_loc = '%s/speedtest' % logs_loc
    make_dir(speedtest_logs_loc)


def make_dir(directory):
    print('Checking to see if directory %s exists' % directory)
    if not os.path.exists(directory):
        print('Making directory %s' % directory)
        os.mkdir(directory)


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
            result = result.strip()
        return result

    timestamp = get_timestamp(dt_format=spreadsheet_date_time_format)
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
    return timestamp, float(ping), float(upload), float(download), share_results


def generate_json_data(timestamp, ping, upload, download, share_results):
    mapping = {'name': 'speedtest',
                'attributes': {
                    'timestamp': str(timestamp),
                    'ping': float(ping),
                    'upload': float(upload),
                    'download': float(download),
                    'share_results': str(share_results)}}
    result = json.dumps(mapping)
    print('Returning json mapping\n%s' % result)
    return result


def generate_csv_data(timestamp, ping, upload, download, share_results):
    first_line = 'timestamp,ping,upload,download,share_results\n'
    second_line = '%s,%s,%s,%s,%s\n' % (timestamp, ping, upload, download, share_results)
    print('Returning CSV output:\n%s\n%s' % (first_line, second_line))
    return [first_line, second_line]



class SpeedtestUtilsTest(TestCase):

    def testJsonData(self):
        timestamp = get_timestamp()
        ping = 99.0
        upload = 9
        download = 10
        share_results = 'blah'
        json_string = generate_json_data(timestamp, ping, upload, download, share_results)
        self.assertIsNotNone(json_string)
        mapping = json.loads(json_string)
        self.assertEqual('speedtest', mapping['name'])
        attributes = mapping['attributes']
        self.assertEqual(ping, attributes['ping'])
        self.assertEqual(upload, attributes['upload'])
        self.assertEqual(download, attributes['download'])
        self.assertEqual(share_results, attributes['share_results'])

    def testCsvData(self):
        timestamp = get_timestamp()
        ping = 99.0
        upload = 9
        download = 10
        share_results = 'blah'
        csv_string = generate_csv_data(timestamp, ping, upload, download, share_results)
        self.assertIsNotNone(csv_string)
        self.assertTrue(2 == len(csv_string))
        self.assertIn(str(ping), csv_string[1])
        self.assertIn(str(download), csv_string[1])
        self.assertIn(str(upload), csv_string[1])
        self.assertIn(str(timestamp), csv_string[1])
        self.assertIn(str(share_results), csv_string[1])

    def testGetOutput(self):
        content = """
    Ping: 5.402 ms
    Download: 39.47 Mbit/s
    Upload: 11.47 Mbit/s
    Share results: http://www.speedtest.net/result/5327551818.png
    """
        f = open('test.txt', 'w')
        f.write(content)
        f.close()
        timestamp, ping, upload, download, share_results = get_output('test.txt')
        self.assertEqual(5.402, float(ping))
        self.assertEqual(39.47, float(download))
        self.assertEqual(11.47, float(upload))
        self.assertEqual('http://www.speedtest.net/result/5327551818.png', share_results)