from requests import post, ConnectionError
from cquptpiper.log import Log, loading
from cquptpiper.auth import Auth


URL_LOGIN_API = 'http://127.0.0.1:5000/login'


class Request:

    @staticmethod
    @loading('登录过期, 正在重新请求登录')
    def login(user: dict, cookie: dict) -> dict:
        user.update(cookie)
        try:
            return eval(post(URL_LOGIN_API, data=user).text)
        except ConnectionError:
            Log.fatal('服务器走丢啦~')
        except Exception:
            Auth.clear_config()

    @staticmethod
    def handle_login(resp: dict):
        if resp.get('code') == 401:
            print('\n', resp.get('msg'))
            Auth.update_user()
        elif resp.get('code') == 200:
            print('\n\033[92m登录成功\033[0m')
        else:
            Log.fatal('\n' + resp.get('msg'))
