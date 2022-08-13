from linebot import LineBotApi
from linebot.models import TextSendMessage
from common_config import CommonConfig

# リモートリポジトリに"ご自身のチャネルのアクセストークン"をpushするのは、避けてください。
# 理由は、そのアクセストークンがあれば、あなたになりすまして、プッシュ通知を送れてしまうからです。
LINE_CHANNEL_ACCESS_TOKEN = CommonConfig.get_line_channel_access_token()
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

def main():
    user_id = "XXXXX"
    messages = TextSendMessage(text=f"こんにちは😁\n\n")
    line_bot_api.push_message(user_id, messages=messages)


def send_push_message(txt):
    user_id = CommonConfig.get_user_id()
    messages = TextSendMessage(text=txt)
    line_bot_api.push_message(user_id, messages=messages)

if __name__ == "__main__":
    main()
