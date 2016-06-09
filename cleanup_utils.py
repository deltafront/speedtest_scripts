from configs import speedtest_file_loc
from utils import get_files, delete_file

__author__ = 'charlie'


def clean_dir(base_directory):
    print('Cleaning all of the files in "%s".' % base_directory)
    files = get_files(base_directory)
    for f in files:
        file_name = '%s/%s' % (base_directory, f)
        print('Deleting file "%s".' % file_name)
        delete_file(file_name)
    print('Deleted %d file%s.' % (len(files), 's' if len(files) > 1 else ''))