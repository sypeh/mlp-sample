# mlp-sample
自然言語の機械学習モデル実行リポジトリ

# 構築手順
## 事前準備
pyenvとpoetryを使えるようにしておく

pyenvとpoetryについては以下を参照
https://data.gunosy.io/entry/can-you-reproduce-the-experiment-pyenv-poetry

## 環境構築
```
# モジュールをインストール
poetry install

# 仮想環境を有効にする
poetry shell

# アプリを起動
uvicorn sample.main:app --reload
```

## 動作確認
http://localhost:8000/ にアクセスする
