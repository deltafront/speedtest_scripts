import os

__author__ = 'charlie'

date_time_format = "%Y-%m-%d'T'%H:%M:%S"
spreadsheet_date_time_format = '%Y-%m-%d %H:%M:%S'
speedtest_file_loc = '%s/logs/speedtest' % os.getenv('HOME')
mongo_db_uri = 'mongodb://localhost:27017'
mongo_db_name = 'metrics'
workbook_name = 'speedtest.csv'
dropbox_file_name = '/speedtest.csv'
