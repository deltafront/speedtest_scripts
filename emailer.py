import json
from unittest import TestCase
import requests
from configs import sender_email_address, recipient_email_address, emailer_api_endpoint
from keys import emailer_api_key

__author__ = 'charlie'


def construct_request_body(timestamp, ping, upload, download, share_results):
    return {
        'type':'speedtest',
        'from': sender_email_address,
        'to': recipient_email_address,
        'timestamp': timestamp,
        'attributes': {
            'ping': '%s ms' % ping,
            'download': '%s Mbit/s' % download,
            'upload': '%s  Mbit/s' % upload,
            'share_results': share_results
        }
    }


def ping_service():
    print('Pinging service at "%s".' % emailer_api_endpoint)
    r = requests.get(emailer_api_endpoint, headers=get_headers())
    response_mapping = r.json()
    status = response_mapping['status']
    message = response_mapping['message'] if 'message' in response_mapping else None
    status_code = r.status_code
    print('Status Code:\t%s\nStatus:\t%s\nMessage:\t%s' % (status_code, status, message))
    return status_code == 200


def send_email_request(request_body_mapping):
    print('Sending email via "%s" from "%s" to "%s".' % (emailer_api_endpoint, sender_email_address,recipient_email_address ))
    r = requests.post(emailer_api_endpoint, data=json.dumps(request_body_mapping), headers=get_headers())
    response_mapping = r.json()
    status = response_mapping['status']
    message = response_mapping['message']
    status_code = r.status_code
    print('Status Code:\t%s\nStatus:\t%s\nMessage:\t%s' % (status_code, status, message))
    return status, message, status_code


def get_headers():
    return {
        'CB-Api-Key': emailer_api_key,
        'Content-Type': 'application/json'
    }



class EmailerTester(TestCase):

    def testSendRequest(self):
        timestamp = '03 August 1969'
        ping = 100
        download = 300
        upload = 200
        share_results = 'http://www.blah.com'
        status, message, status_code = send_email_request(construct_request_body(timestamp, ping, upload, download, share_results))
        self.assertIsNotNone(status)
        self.assertIsNotNone(message)
        self.assertIsNotNone(status_code)
        self.assertEqual(201, status_code)

    def testPingService(self):
        self.assertTrue(ping_service())