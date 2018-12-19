import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAePHWZCiOCYBALzFxfBZAzsBt5Dc8crwZAGktkTt70sWLq71ijb3ZCIh51pxMzUKJQOmX7ZCUPZB4BOp3cQTTlUb8wK5QNANXr7b6kwd0XmBUZB39Uebd2zZCS33ZAfy11aLluPaB6y7UaE4HLzqPtT70uVyVWg4sglIZAFiGkCc7Wlxnn5vkS9EO"


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response



def send_image_url(id, img_url):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message":{
            "attachment":{
                "type":"image",
                "payload":{
                    "url":img_url,
                    "is_reusable":True
                }
            }
        }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send picture")
    return response


def send_button_message(id, text, buttons):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":text,
                    "buttons":buttons
                }
            }
        }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send picture")
    return response

