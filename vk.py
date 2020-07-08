import requests
from exceptions import InvalidData
from time import sleep

URL = 'https://api.vk.com/method/'

# establishes a connection and accepts messages
# input: token (str), server's url (str), verlion api (str or int), group id (str or int).
# Optional input: limit (default=7) sets the max number of messages to return.


class LongPollConnect():
    # returns data for connection
    # output: data for API connection (dict)
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

    # check and return an event about new messages in the chat
    # output: API data about new event (dict)
    def check_new_event(self):
        server = self.connect['server']
        params = {'act': 'a_check',
                  'key': self.connect['key'], 'ts': self.connect['ts'],  'wait': '25'}
        data = requests.post(url=server, params=params)
        return data

    # getting and processing new events
    # output: a class field with data about new events (list)
    def process_new_event(self):
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

    # continuously listens for events about new messages
    # output: returns the generator
    def get(self):
        while True:
            self.process_new_event()
            yield self.data

    # removes messages that have been read from the array
    # input: num (default = 0) specifies which message to delete from the array.
    #        forced (default=False) - allows you to delete an item even if the limit is not reached
    def delite(self, forced=False, num=0):
        if len(self.data) >= self.limit:
            self.data.pop(0)
        elif forced:
            self.data.pop(num)


class ScreenNow():
    def __init__(self, from_id, message, answers):
        self.from_id = from_id
        self.answers = answers
        self.message = message
        self.now_screen = 0

    def get_kit_button(self):
        kit_buttons = []
        now_step_id = 0
        for i in range(len(self.answers['actions'])):
            if self.answers['actions'][i]['step_id'] == self.now_screen:
                now_step_id = i
                break
        for i in range(len(self.answers['actions'][now_step_id]['kit_buttons'])):
            for j in range(len(self.answers['actions'][now_step_id]['kit_buttons'][i]['buttons'])):
                kit_buttons.append({'id_button': self.answers['actions'][now_step_id]['kit_buttons']
                                    [i]['buttons'][j]['button_id'], 'next_step': self.answers['actions'][now_step_id]['kit_buttons'][i]['buttons'][j]['next_step_id']})
        self.kit_buttons = kit_buttons
        # DEBUG
        # for i in range(len(kit_buttons)):
        #     print("i = " + str(i))
        #     print("id button = " + str(kit_buttons[i]['id_button']))
        #     print("id next = " + str(kit_buttons[i]['next_step']))


class Answer(LongPollConnect):
    def __init__(self, answers, token, group_id, version_api):
        super().__init__(token=token, version_api=version_api, group_id=group_id)
        self.answers = answers

    def get_data_about_event(self, event):
        keyboard = bool(event['updates'][0]['object']
                        ['client_info']['keyboard'])
        inline = bool(event['updates'][0]['object']
                      ['client_info']['inline_keyboard'])
        carousel = bool(event['updates'][0]
                        ['object']['client_info']['carousel'])
        from_id = event['updates'][0]['object']['message']['from_id']
        text = event['updates'][0]['object']['message']['text']
        return [keyboard, inline, carousel, from_id, text]

    def send_answer(self, about_event):
        print(about_event)

    def process_message(self):
        while True:
            next(self)
            about_event = self.get_data_about_event(event=self.data[0])
            self.send_answer(about_event=about_event)
            self.delite(forced=True)
