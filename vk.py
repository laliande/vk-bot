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
            return {'key': str(key), 'server': str(server), 'ts': str(ts)}
        except:
            raise InvalidData

    def __init__(self, token, version_api, group_id):
        self.method = 'groups.getLongPollServer'
        self.url = URL + self.method
        self.token = token
        self.version_api = version_api
        self.group_id = group_id
        self.connect = self.get_data_for_connect()
        self.get_new_event()

    def check_new_event(self):
        server = self.connect['server']
        params = {'act': 'a_check',
                  'key': self.connect['key'], 'ts': self.connect['ts'],  'wait': '25'}
        data = requests.post(url=server, params=params)
        return data

    def get_new_event(self):
        while True:
            data = self.check_new_event()
            new_ts = int(self.connect['ts']) + 1
            self.connect['ts'] = str(new_ts)
            data = data.json()
            try:
                if data['failed'] == 1:
                    new_ts = data['ts']
                    self.connect['ts'] = new_ts
                elif data['failed'] == 2:
                    new_key = get_data_for_connect['key']
                    self.connect['key'] = new_key
                    print('faild2')
                    print()
                else:
                    new_key = get_data_for_connect['key']
                    new_ts = get_data_for_connect['ts']
                    self.connect['key'] = new_key
                    self.connect['ts'] = new_ts
                    print('faild3')
                    print()
            except:
                self.data = data
                print(data)
