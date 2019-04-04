import os

API_TOKEN = os.environ['TICHAITI_TOKEN']
DEFAULT_REPLY = 'Mwen pa konprann...'
ERRORS_TO = 'tichaitibot-errs'
PLUGINS = [
    'slackbot.plugins',
    # 'tichaitibot.plugins',
]
