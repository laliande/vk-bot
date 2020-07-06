import requests
from exceptions import InvalidData
from time import sleep

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

    def __init__(self, token, version_api, group_id, limit=7):
        self.method = 'groups.getLongPollServer'
        self.url = URL + self.method
        self.token = token
        self.version_api = version_api
        self.group_id = group_id
        self.connect = self.get_data_for_connect()
        self.data = []
        self.limit = limit

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
                failed = data['failed']
                if failed == 1:
                    new_ts = data['ts']
                    self.connect['ts'] = new_ts
                    print('faild1')
                elif failed == 2:
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
                return self.data.append(data)

    def __iter__(self):
        return self

    def __next__(self):
        self.delite()
        return next(self.get())

    def get(self):
        while True:
            self.get_new_event()
            yield self.data

    def delite(self, num=0):
        if len(self.data) >= self.limit:
            self.data.pop(num)
