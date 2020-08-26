from flask import Blueprint

api = Blueprint('api', __name__)


@api.route('CreateCastomVkBot', methods=['POST'])
def create_bot():
    pass


@api.route('ChangeCastomVkBot', methods=['PUT'])
def change_bot_settings():
    pass


@api.route('DeleteCastomVkBot', methods=['DELETE'])
def delete_bot():
    pass


@api.route('GetCurrentSettingsVkBot', methods=['GET'])
def get_settings_bot():
    pass


@api.route('ChangeActiveVkBot', methods=['POST'])
def change_active():
    pass


@api.route('AddMLToVkBot', methods=['POST'])
def add_ml():
    pass


@api.route('SignUp', methods=['POST'])
def sign_up():
    pass


@api.route('SignIn', methods=['GET'])
def sign_in():
    pass


@api.route('CallbackVk/<slag>', methods=['POST'])
def handler_callback_messages(slag):
    pass
