# carousell-search

Getting near real-time notifications on Carousell.

NOTE:
- Slack integration is not working for the time being
- Only works for malaysia, RM currency

## Requirements

Python 3+

## Installing

`pip3 install -r requirements.txt`

## Configuring

Configure `myconfigurations.py` with 
- your Slack token from https://api.slack.com/tokens
- your Slack channel
- search queries in `ITEMS`

Ensure that your Slack app has the correct permissions to post in channel

## Running

`python3 main.py`
