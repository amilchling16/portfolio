import requests

def mail_handler(event, context):
    print event
    params = event['params']['querystring']
    url = "https://api.mailgun.net/v3/sandbox4cda96957a994f598823feb327543413.mailgun.org/messages"
    url2 = ""
    response = requests.post(
        url,
        auth=("api", "key-38edccbaabd873f9bc786c3fa219a65b"),
        data={
            "from": "New Inquiry <{}>".format(params['email']),
            "to": ["amilchling@gmail.com", "sjohnson540@gmail.com"],
            "subject": "Message from {}".format(params['name']),
            "text": params['body']
        }
    )
    print response.text
    return response.json()
