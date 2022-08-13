from configparser import ConfigParser

config = ConfigParser()
section = 'development'

config.add_section(section)
config.set(section, 'spread_sheet_key', "dummy")
config.set(section, 'line_channel_access_token', "dummy")
config.set(section, 'user_id', "dummy")

with open('common_config.ini', 'w') as file:
    config.write(file)
