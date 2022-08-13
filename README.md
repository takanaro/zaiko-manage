# 在庫通知システム

## 仮想環境作成 ＆ アクティブ化 ＆ パッケージインストール

```
python3 -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```

## 実行方法

### 設定ファイル作成 ＆ 設定値入力

設定ファイルのダミーを作成し、LINEトークン、スプレッドシートID、ユーザーIDを設定する。

```
python create_common_config.py
```

### 在庫確認処理実行

下記コマンドを実行

```
python remind_zaiko.py
```

