import requests


class HTTP:
    @classmethod
    def get(self,url,return_json=True):
        r = requests.get(url)   #r是此次http请求结果的封装对象

        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text

        # if r.status_code != 200:
        #     return {} if return_json