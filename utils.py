import datetime
from os import listdir
import os
from os.path import isfile, join
from configs import date_time_format

__author__ = 'charlie'


def get_timestamp(dt_format=date_time_format):
    now = datetime.datetime.now()
    timestamp = now.strftime(dt_format)
    return timestamp


def get_files(path, *exclusions):
    return [filename for filename in listdir(path) if
            isfile(join(path, filename)) and (exclusion not in filename for exclusion in exclusions)]


def delete_file(file_name):
    os.remove(file_name)


def append_extension(old_file_name, extension):
    new_file_name = '%s.%s' % (old_file_name, extension)
    os.rename(old_file_name, new_file_name)
    return new_file_name

