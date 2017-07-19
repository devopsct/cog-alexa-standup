import requests
import os

webhook_url = os.environ['COG_WEBHOOK']
def standup_reminder(event, context):
    webhook_resp = requests.post(webhook_url)

    response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': 'The team has been reminded to join standup',
            }
        }
    }

    return response
