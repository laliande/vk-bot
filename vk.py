import requests
from exceptions import InvalidData
from time import sleep
from random import randint
import json
import time

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
        self.flag_for_remove = False

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
            print(data.json())
            new_ts = int(self.connect['ts']) + 1
            self.connect['ts'] = str(new_ts)
            data = data.json()
            try:
                failed = data['failed']
                if failed == 1:
                    new_ts = data['ts']
                    self.connect['ts'] = new_ts
                    #print('faild1')
                #elif failed == 2:
                #    new_key = get_data_for_connect['key']
                #    self.connect['key'] = new_key
                #    print('faild2')
                #    print()
                else:
               #     new_key = get_data_for_connect['key']
               #     new_ts = get_data_for_connect['ts']
               #     self.connect['key'] = new_key
               #     self.connect['ts'] = new_ts
               #     print('faild3')
               #     print()
                     self.connect = self.get_data_for_connect()
                     #continue
            except:
                if data['updates']:
                    if data['updates'] != []:
                        if data['updates'][0]['type'] == 'message_new':
                            return self.data.append(data)
                else:
                    self.connect = self.get_data_for_connect()
                    self.flag_for_remove = True
                    #continue

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
        # elif len(self.data) != 0 and self.data[0]['updates'] == []:
        #     self.data.pop(0)
        elif forced:
            self.data.pop(num)

# monitors the current state of the user's screen: messages and buttons that are currently displayed
# input: data about default answers (json)


class ScreenNow():
    def __init__(self, answers):
        self.answers = answers
        self.now_screen = 0
        self.get_all_buttons_in_bot()
        self.all_buttons = self.get_all_buttons_in_bot()
        self.kit_button_on_screen = []
        self.user = ''
        self.message_id = 0
        self.method = 'messages.send'
        self.url = URL + self.method
        self.message = 'unknown request'
        self.num_lines = 0
        self.attach = ''

# gets data about all bot buttons that are set in standard responses
# output: all buttons (list)
    def get_all_buttons_in_bot(self):
        all_buttons = []
        for i in range(len(self.answers['elements'][0]['buttons'])):
            all_buttons.append(self.answers['elements'][0]['buttons'][i])
        return all_buttons

# gets the ID of the current user screen for easy iteration over the array
# output: id (int)
    def get_now_step_in_all_answers(self):
        for i in range(len(self.answers['actions'])):
            if self.answers['actions'][i]['step_id'] == self.now_screen:
                self.now_step_id = i
                break

# gets a set of buttons that are currently displayed on the user's screen
    def get_kit_button_on_screen(self):
        self.get_now_step_in_all_answers()
        kit_buttons_on_screen = []
        kit_id = []
        button = {}
        self.num_lines = len(
            self.answers['actions'][self.now_step_id]['kit_buttons'])
        for i in range(len(self.answers['actions'][self.now_step_id]['kit_buttons'])):
            for j in range(len(self.answers['actions'][self.now_step_id]['kit_buttons'][i]['buttons'])):
                button = {'button_id': self.answers['actions'][self.now_step_id]['kit_buttons']
                          [i]['buttons'][j]['button_id'], 'next_step': self.answers['actions'][self.now_step_id]['kit_buttons'][i]['buttons'][j]['next_step_id'], "line": self.answers['actions'][self.now_step_id]['kit_buttons'][i]['line']}
                kit_buttons_on_screen.append(button)
                kit_id.append(self.answers['actions'][self.now_step_id]['kit_buttons']
                              [i]['buttons'][j]['button_id'])
        for i in range(len(self.all_buttons)):
            for j in range(len(kit_buttons_on_screen)):
                if self.all_buttons[i]['button_id'] == kit_buttons_on_screen[j]['button_id']:
                    kit_buttons_on_screen[j].update(self.all_buttons[i])
        self.kit_button_on_screen = kit_buttons_on_screen


# updates information about the status of buttons on the user's screen when the user clicks on one of the buttons
# input: message from connect with API vk


    def change_data_about_screen(self, message):
        self.user = message['from_id']
        for i in range(len(self.kit_button_on_screen)):
            if message['text'] == self.kit_button_on_screen[i]['text']:
                self.now_screen = self.kit_button_on_screen[i]['next_step']
                self.get_now_step_in_all_answers()
                self.message_id = self.answers['actions'][self.now_step_id]['message_id']
                break
        self.get_kit_button_on_screen()
        for i in range(len(self.answers['elements'][0]['messages'])):
            if self.answers['elements'][0]['messages'][i]['message_id'] == self.message_id:
                self.message = self.answers['elements'][0]['messages'][i]['text']
                self.attach = self.answers['elements'][0]['messages'][i]['attach']
                break

# generates a keyboard array for sending data to the user
# output: array keyboard (json)
    def get_keyboard_for_send(self):
        keyboard = {}
        lines = []
        for i in range(self.num_lines):
            lines.append([])
        keyboard.update(
            {"one_time": self.kit_button_on_screen[0]["one_time"]})
        keyboard.update(
            {"inline": self.kit_button_on_screen[0]["inline"]})
        # print(self.kit_button_on_screen)
        for i in range(len(self.kit_button_on_screen)):
            labal = self.kit_button_on_screen[i]["text"]
            type_action = self.kit_button_on_screen[i]["action"]
            action = {"action": {"type": type_action, "label": labal}}
            color = {"color": self.kit_button_on_screen[i]["color"]}
            action.update(color)
            keyboard.update({"buttons": [[action]]})
            lines[int(self.kit_button_on_screen[i]["line"]) -
                  1].append(action)
        keyboard.update({"buttons": lines})
        return json.dumps(keyboard)

# sends a message to the user
# input: message from API VK (json), token (str), version_api (str)
    def send_message(self, message, token, version_api):
        keyboard = self.get_keyboard_for_send()
        self.change_data_about_screen(message=message)
        params = {'peer_id': self.user, 'random_id': randint(0, 65000),
                  'message': self.message, 'access_token': token, 'v': version_api, "keyboard": keyboard, "attachment": self.attach}
        requests.post(url=self.url, params=params)

# receives data about new messages and sends them to fix the current state of the user's screen and send messages to users
# input: default answers (json), token (str), group_id (str or int), version_api (str)


class Answer(LongPollConnect):
    def __init__(self, answers):
        super().__init__(token=answers["about_group"]["token"], version_api=answers["about_group"]
                         ["version_api"], group_id=answers["about_group"]["group_id"])
        self.answers = answers
        self.connections = []


# processing data about the current event-gets the necessary information
# input: data about event (dict)

    def get_data_about_event(self, event):
        keyboard = event['updates'][0]['object']['client_info']['keyboard']
        inline = event['updates'][0]['object']['client_info']['inline_keyboard']
        carousel = event['updates'][0]['object']['client_info']['carousel']
        from_id = event['updates'][0]['object']['message']['from_id']
        text = event['updates'][0]['object']['message']['text']
        return {"keyboard": keyboard, "inline": inline, "carousel": carousel, "from_id": from_id, "text": text}

# create new connect
# input:class instance
    def new_connect(self):
        connect = ScreenNow(answers=self.answers)
        return connect

# decides who to send the response to and sends it to
    def send_answer(self, about_event):
        connect = []
        for i in range(len(self.connections)):
            if self.connections[i]["from_id"] == about_event["from_id"]:
                connect.append(self.connections[i]['connect'])
                self.connections[i]['time'] = time.time()
                break
        if len(connect) == 0:
            new_connect = self.new_connect()
            new_connect.get_kit_button_on_screen()
            self.connections.append(
                    {"from_id": about_event["from_id"], "connect": new_connect, 'time': time.time()})
            new_connect.send_message(message=about_event, token=self.token,
                                     version_api=self.version_api)
        else:
            connect[0].send_message(message=about_event, token=self.token,
                                    version_api=self.version_api)
    
    def clear_list_users(self):
        time_now = time.time()
        for i in range(len(self.connections)):
            if time_now - self.connections[i]['time'] >= 600:
                self.connections.pop(i)
                print('remove: ' + str(self.connections[i]['from_id']))

# processes the receipt of new events and sends them for processing
    def process_message(self):
        next(self)
        try:
            about_event = self.get_data_about_event(event=self.data[0])
            self.delite(forced=True)
            self.send_answer(about_event=about_event)
            self.clear_list_users()
        except:
            sleep(1)
