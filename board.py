import os
import sys

from bs4 import BeautifulSoup

from http_request import HttpRequest


class Board:
    def get(self, key):
        if not key.isdecimal():
            print('数字以外が含まれています。掲示板URL内のkeyを指定してください')
            sys.exit()

        url = os.environ['GET_URL'].format(os.environ['THREAD_PLANET'], os.environ['THREAD_BOARD'], key)
        print('now requesting for ' + url)
        response = HttpRequest.get(url)

        html_text = response.text
        soup = BeautifulSoup(html_text, 'html.parser')

        def get_res_info(res):
            res_num = res.get('id')
            message = res.select_one("div[class='message']").text.strip()
            return {'res_num': res_num, 'message': message}
        res_list = list(map(get_res_info, soup.select("div[class='post']")))

        if not res_list:
            print('指定先が間違っているか、レスがありません')
            sys.exit()

        return res_list
