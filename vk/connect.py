import requests
import jwt


class VkMethods():

    """Simplifies interaction with the VK API. Initialized using the VK API methods."""

    def __init__(self):
        # This is the base url for all requests to the API VK.
        self.base_url = 'https://api.vk.com/method/'
        # This is the API version. Here is the latest version for the moment.
        self.version_api = '5.120'
        # This is the method for getting the confirmation code.
        self.callback_confirmation_code = self.base_url + \
            'groups.getCallbackConfirmationCode'
        # This is a method for adding a server.
        self.callback_add_server = self.base_url + 'groups.addCallbackServer'
        # This is the setting method.
        self.set_callback_settings = self.base_url + 'groups.setCallbackSettings'
        # This is the method for deleting the server.
        self.delete_callback_server = self.base_url + 'groups.deleteCallbackServer'


class CallBackConnect(VkMethods):
    """Performs actions to set up a callback connection: gets a unique server url, adds a server,
        deletes a server, sets server settings, and receives a server confirmation code."""

   def __init__(self, token, group_id, user_id, SECRET_KEY, server):
        super().__init__()
        # This is the unique identifier of the bot owner.
        self.user_id = user_id 
        # This is a secret key that allows you to generate a unique server
        #  url and which is passed to the VK to send requests to the server with the key.
        self.SECRET_KEY = SECRET_KEY 
        # This is the server domain.
        self.server = server
        # These are basic settings for all queries.
        self.base_params = {'access_token': token,
                            'group_id': group_id, 'v': self.version_api}

    """This method adds the server to the VC group. Returns the server ID and its unique url."""
    def add_server(self):
        server = self.gen_server_url()
        updates = {'url': server, 'title': 'bots',
                   'secret_key': self.SECRET_KEY}
        params = dict(self.base_params)
        params.update(updates)
        response = requests.post(url=self.callback_add_server, params=params).json()[
            'response']
        response.update({'server_url': self.server})
        return response

    """This method removes the server from the VK group and returns a response from the VK API."""
    def delete_server(self, server_id):
        params = dict(self.base_params)
        params.update({'server_id': server_id})
        response = requests.post(
            url=self.delete_callback_server, params=params)
        return response.json()

    """This method gets the confirmation code and returns it if it was successful."""
    def get_confirmation_code(self):
        confirmation_code = requests.post(
            url=self.callback_confirmation_code, params=self.base_params)
        try:
            return {'ok': confirmation_code.json()['response']['code']}
        except:
            return {'error': confirmation_code.json()['error']['error_msg']}

    """This method configures the server. Accepts the group's server number
        and option parameters in JSON format."""
    def set_settings(self, server_id, param_settings):
        params = dict(self.base_params)
        params.update({'server_id': server_id})
        params.update(param_settings)
        response = requests.post(url=self.set_callback_settings, params=params)
        return response.json()

    """This method generates a unique url on the server."""
    def gen_server_url(self):
        encode_str = str(jwt.encode(
            {'user_id': self.user_id}, self.SECRET_KEY, algorithm='HS256'))
        path = encode_str.split(sep='.')[2][0:-1]
        url = self.server + path
        return url


class LongPollConnect(VkMethods):
    # start/stop geting events
    pass
