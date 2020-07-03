import requests
from exceptions import InvalidData

URL = 'https://api.vk.com/method/'


class LongPollConnect():
    def get_data_for_connect(self):
        params = {'group_id': self.group_id,
                  'access_token': self.token, 'v': self.version_api}
        data = requests.post(url=self.url, params=params)
        data = data.json()
        try:
            key = data['response']['key']
            server = data['response']['server']
            ts = data['response']['ts']
            return (key, server, ts)
        except:
            raise InvalidData

    def __init__(self, token, version_api, group_id):
        self.method = 'groups.getLongPollServer'
        self.url = URL + self.method
        self.token = token
        self.version_api = version_api
        self.group_id = group_id
        self.connect = self.get_data_for_connect()
