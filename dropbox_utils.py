import codecs
from unittest import TestCase
from dropbox import dropbox
from dropbox.exceptions import ApiError
from dropbox.files import DownloadError, WriteMode
from keys import dropbox_key

__author__ = 'charlie'


def upload_to_dropbox(origin_file_name, destination_file_name, write_mode=WriteMode.add):
    print('Processing file %s' % origin_file_name)
    f = open(origin_file_name)
    content = f.read()
    f.close()
    dbx = dropbox.Dropbox(dropbox_key)
    print('Uploading content to %s\n%s' % (destination_file_name, content))
    dbx.files_upload(content, destination_file_name, mode=write_mode)
    sharing_info = dbx.sharing_create_shared_link(destination_file_name)
    print('%s shared at %s:\n%s' % (destination_file_name, sharing_info, content))
    return sharing_info


def connect():
    return dropbox.Dropbox(dropbox_key)


def get_file_from_dropbox(destination_file_name):
    dbx = connect()
    try:
        md, res = dbx.files_download(destination_file_name)
        file_out = res
        if res is not None:
            print('Returning file: %s\n%s\Md=%s' % (destination_file_name, res.content, md))
    except ApiError as le:
        file_out = None
        print(le)
    return file_out




class DropboxUtilsTest(TestCase):

    def testGetFileFromDropboxNotExists(self):
        f = get_file_from_dropbox('/test')
        self.assertIsNone(f)

    def testGetFileFromDropboxExists(self):
        f = open('test.txt','w')
        f.write('this is some text')
        f.close()
        sharing_info = upload_to_dropbox('test.txt', '/test.txt')
        self.assertIsNotNone(sharing_info)
        f = get_file_from_dropbox('/test.txt')
        self.assertIsNotNone(f)
