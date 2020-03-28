# Project Overview

The purpose of this project is to pull down XML data from the Twinstar Armory website for raiders in your raid group, and generate a google sheet based on that content. The aggregated data shows the current gear your raiders are wearing, their professions, the current enchantment status of pieces, and other general information about their stats. 

# Developer Setup

This solution uses a virtual environment (venv), which we use to enforce library and python versions.

## A. Virtual Environment

Run the following commands in the terminal in order to setup and install library dependencies.

`source twinstarmory-tool/bin/activate`

This activates the virtual environment. You'll be able to verify it's running by location (twinstarmory-tool) prepended to your terminal $PATH.

[example of that here]

`pip install -r requirements.txt`

There is a requirements.txt file in the parent directory that contains all of the module dependencies. Running this command will install those module versions for this particular virtual environment only. This will not affect module versions globally on your machine.

## B. Google OAuth2 Account Setup

In order to compile the script and run, you'll need to setup a GoogleAPI OAuth2 account and initialize it with a google sheet. You can set it up so that your google API service provider will modify a sheet through your own Google account.

https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html



