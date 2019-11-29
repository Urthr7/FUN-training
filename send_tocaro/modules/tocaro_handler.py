import urllib.request
import json
import os
import ssl


class TocaroHandler:
    def __init__(self):
        self.message = {
            "text": "string",
            "color": "color",
            "attachments": [
                {
                    "title": "string",
                    "value": "string"
                },
                {
                    "image_url": "url"
                }
            ]
        }

    def set_text(self, text):
        self.message["text"] = text

    def set_color(self, color):
        self.message["color"] = color

    def set_attachments(self, contents):
        self.message["attachments"] = contents

    def send2tocaro(self):
        tocaro_url = "URLを入れる"
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

        headers = {'Content-type': 'application/json'}
        req = urllib.request.Request(tocaro_url, json.dumps(self.message).encode(), headers)
        with urllib.request.urlopen(req, context=context) as res:
            body = res.read()
        return body
