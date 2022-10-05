import sys
import os
import requests


class HttpRequest:
    def __init__(self):
        pass

    @classmethod
    def get(cls, url, use_proxy=False):
        headers = {
            'User-Agent': os.environ['USER_AGENT'],
            'Accept-Language': os.environ['HTTP_ACCEPT_LANGUAGE']
        }
        try:
            if use_proxy:
                response = requests.get(url, headers=headers, proxies={'http': os.environ['PROXY_HOST'], 'https': os.environ['PROXY_HOST']})
            else:
                response = requests.get(url, headers=headers)
            response.encoding = response.apparent_encoding
        except Exception as e:
            print(e)
            sys.exit()

        if not response.status_code == 200:
            sys.exit()

        return response

    @classmethod
    def post(cls, url, data, headers, use_proxy=False):
        try:
            if use_proxy:
                response = requests.post(url, data=data, headers=headers, proxies={'http': os.environ['PROXY_HOST'], 'https': os.environ['PROXY_HOST']})
            else:
                response = requests.post(url, data=data, headers=headers)
        except Exception as e:
            print(e)
            sys.exit()

        if not response.status_code == 200:
            sys.exit()

        return
