# Speedtest project


## Prerequisites

In order to run this project, you will need  the following:

### GIT Client

You will need a git command line client in order to clone this repository onto your computer. A good place to start looking for one to download and install would be [here](https://git-scm.com/downloads)

### This repository

Once you have a command-line client install, open up a terminal / command window, navigate to the folder you want this project to be in, and type in the following:

`git clone https://github.com/deltafront/speedtest_scripts.git`

### Python

This project is designed to be run using the 3.0 branch of Python. If you do not have it installed, please go [here](https://wiki.python.org/moin/BeginnersGuide/Download) and follow the instructions.

### MongoDB

Please go [here](https://docs.mongodb.com/manual/administration/install-community/) and follow the installation instructions.

### Required packages

You will need the following python packages:

*   [speedtest-cli](https://github.com/sivel/speedtest-cli)
*   [dropbox](https://www.dropbox.com/developers-v1/core/sdks/python)
*   [pymongo](http://api.mongodb.com/python/current/installation.html?_ga=1.263110350.371206641.1464658656)
*   [requests](http://docs.python-requests.org/en/master/)
*   [pytz](http://pytz.sourceforge.net/)
*   [iso8601](https://pypi.python.org/pypi/iso8601)


For each of these, installing them should be as easy as running `pip  install {package_name}`

If you do not have pip installed, please go [here](https://pip.pypa.io/en/stable/installing/) and follow the instructions

### Download and setup the emailer service

If you want emails sent to you everytime a speedtest run has been executed, you will need to do the following:

*   Install the Google App Engine SDK for Python.
    *   Run `pip install appengine`
    *   Add the following to your path:
        *   ~google_appengine
        *   ~google_appengine/lib
        *   ~google_appengine/lib/yaml
    *   Setup a Google App Engine project
        *   This is pretty easy, assuming you have a Google Account. I would recommend following the steps listed underneath "Before You Begin" [here](https://cloud.google.com/appengine/docs/python/gettingstartedpython27/creating-guestbook#objectives)
    *   Get the code for the Emailer Service
        *   Clone the project at ``
    *   Set up your custom configurations
        *   In your `keys.py` file in this project, copy the `api_key` value that you specified in the `configs.py` file in your local copy of the Emailer Service to the `emailer_api_key`
        *   In your copy of [configs.py](https://github.com/deltafront/speedtest_scripts/blob/master/configs.py), make the following changes:
            *   `sender_email_address` - change this so that the part after the `@` matches your App Engine's Application name + `.appspotmail.com`
            *   `recipient_email_address` - change this, please and don't use mine :)
            *   `emailer_api_endpoint` - change this to match your App Engine's Application name
    *   Upload the service
        *   In your command line / terminal, navigate to where you have cloned the Emailer Service and run the command specified in the [notes]() file.

## Running the scripts

First of all, you will need to get a Dropbox account and obtain a developers key, which will need to be placed in a file called 'keys.py'

*   In order to register for a Dropbox account, go [here](https://www.dropbox.com/).
*   In order to get an API key for your Dropbox account, go here.
*   Copy and paste [keys.bak.py](https://github.com/deltafront/speedtest_scripts/blob/master/keys.bak.py) to a file called `keys.py` and then enter the key that you obtained in the step above.
*   In [configs.py](https://github.com/deltafront/speedtest_scripts/blob/master/configs.py), you can change several of the settings. Please consult that file directly in order to view your options.

Once the above steps have been done, I would recommend a test run. Go to the directory in which you have cloned this project and run the following command:

`python speedtest.py`

The following things should happen:

## Getting the script to run automatically

Once you have verified that the speedtest script works, you will need to add this script to your crontab in order for it to run on a regular basis by itself.

I would recommend that this script is executed on an hourly basis. Edit your crontab so that, for example, the following entry is added:

`0 * * * * python /Users/charlie/PycharmProjects/speedtest_scripts/speedtest.py`

The path `/Users/charlie/PycharmProjects/` is where my `speedtest-scripts` repo has been clones to; most likely yours will be in a different place.

This will cause the script to be executed every hour on the hour. If you want to change it, I would recommend using a tool such as the one found [here](http://crontab-generator.org/).