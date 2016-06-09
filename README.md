# Speedtest project


## Prerequisites

In order to run this project, you will need  the following

### Python

This project is designed to be run using the 3.0 branch of Python. If you do not have it installed, please go [here](https://wiki.python.org/moin/BeginnersGuide/Download) and follow the instructions.

### MongoDB

Please go [here](https://docs.mongodb.com/manual/administration/install-community/) and follow the installation instructions.

### Required packages

You will need the following python packages:

*   [speedtest-cli](https://github.com/sivel/speedtest-cli)
*   [dropbox](https://www.dropbox.com/developers-v1/core/sdks/python)
*   [pymongo](http://api.mongodb.com/python/current/installation.html?_ga=1.263110350.371206641.1464658656)


For each of these, installing them should be as easy as running `pip  install {package_name}`

If you do not have pip installed, please go [here](https://pip.pypa.io/en/stable/installing/) and follow the instructions

## Running the scripts

First of all, you will need to get a Dropbox account and obtain a developers key, which will need to be placed in a file called 'keys.py'

*   In order to register for a Dropbox account, go [here](https://www.dropbox.com/).
*   In order to get an API key for your Dropbox account, go here.
*   Copy and paste [keys.bak.py](https://github.com/deltafront/speedtest_scripts/blob/master/keys.bak.py) to a file called `keys.py` and then enter the key that you obtained in the step above.