import sys
import os
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import line_api
from common_config import CommonConfig

EXEC_ABS_DIR = os.path.dirname(os.path.abspath(__file__))


class ZaikoMaster:
    def __init__(self):
        self.df = pd.DataFrame()

    def __init__(self, ws: gspread.worksheet.Worksheet):
        self.df = pd.DataFrame(ws.get_all_records())

    def get_missing_products(self):
        t = self.df[self.df['補充ステータス'] == '補充必要']
        return t['備品名'].tolist()


def main():
    # お決まりの文句
    # 2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
    scope = ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive']
    # ダウンロードしたjsonファイル名をクレデンシャル変数に設定。
    credentials = Credentials.from_service_account_file(
        EXEC_ABS_DIR + "/acfile.json", scopes=scope)
    # OAuth2の資格情報を使用してGoogle APIにログイン。
    gc = gspread.authorize(credentials)

    # スプレッドシート（ブック）を開く
    workbook = gc.open_by_key(CommonConfig.get_spread_sheet_key())
    # シートを開く
    ws = workbook.worksheet('志村三丁目')

    obj = ZaikoMaster(ws)

    # LINEメッセージ送信用文字列作成
    send_text = '下記商品の補充が必要です。\n'
    for item in obj.get_missing_products():
        send_text += '・' + item + f"\n"
    send_text += '注文完了後、下記シートの「発注セット数」を更新してください。\n'
    send_text += 'https://docs.google.com/spreadsheets/d/' \
        + CommonConfig.get_spread_sheet_key() \
        + '/edit?usp=sharing'

    # LINEでプッシュ通知
    line_api.send_push_message(send_text)


if __name__ == "__main__":
    main()
