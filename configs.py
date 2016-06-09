import os

__author__ = 'charlie'

'''
Date-Time format for  the generated file. This is pretty much legacy, but don't change it
'''
date_time_format = "%Y-%m-%d'T'%H:%M:%S"
'''
Date-Time format that will be used in the CSV file. Do not change.
'''
spreadsheet_date_time_format = '%Y-%m-%d %H:%M:%S'
'''
Location that all of the speedtest files will be written to. By default this is set to a folder named
"logs/speedtest/" in the user's home directory. This can be changed.
 '''
speedtest_file_loc = '%s/logs/speedtest' % os.getenv('HOME')
'''
URI of the Mongo database. These are pretty much default settings.
'''
mongo_db_uri = 'mongodb://localhost:27017'
'''
Name of the Mongo Datatbase
'''
mongo_db_name = 'metrics'
'''
Name of the CSV file written locally
'''
workbook_name = 'speedtest.csv'
'''
Name of the CSV file uploaded to Dropbox
'''
dropbox_file_name = '/speedtest.csv'
