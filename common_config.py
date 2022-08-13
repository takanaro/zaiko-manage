import os
from configparser import ConfigParser, NoOptionError

EXEC_ABS_DIR = os.path.dirname(os.path.abspath(__file__))
config = ConfigParser()
config.read(EXEC_ABS_DIR + '/common_config.ini')
env = 'development'

class CommonConfig:
    @staticmethod
    def get_line_channel_access_token():
        try:
            return config.get(env, 'line_channel_access_token')
        except NoOptionError:
            return None


    @staticmethod
    def get_spread_sheet_key():
        try:
            return config.get(env, 'spread_sheet_key')
        except NoOptionError:
            return None


    @staticmethod
    def get_user_id():
        try:
            return config.get(env, 'user_id')
        except NoOptionError:
            return None