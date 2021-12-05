## 概要

検出した顔を黒く塗りつぶすことで匿名化を実施するCUIアプリケーション

実行例：

![output](example.gif)

## 使用技術

顔検出にRetinaFace( https://arxiv.org/abs/1905.00641 )を使用

## 前提条件

以下のいずれかが使用するPCにインストールされていること

()内のバージョンは、動作検証環境でのバージョンである。

* Python(バージョン:3.8.12)

* Docker(バージョン：20.10.2) + docker-compose(バージョン：1.29.2)

## 環境構築

### インストール済みのPythonを用いる場合

基本的には、https://docs.python.org/ja/3/library/venv.html を参照

1. 仮想環境を作成

```bash
python -m venv .venv
```

2. 仮想環境有効化

* Windowsのコマンドプロンプトの場合

    ```bash
    .venv\Scripts\activate.bat
    ```

* Windowsのパワーシェルを用いる場合

    パワーシェルの場合、以下の問題が発生する可能性がある。

    1. ps1ファイルが実行できない

        https://qiita.com/teruto725/items/49b56c778c345170c157 を参照

    2. 絶対パスに日本語が含まれているため、仮想化が上手くいかない

        .venv\Scripts\Activate.ps1をエディタで開き、文字コードをsjisに変更する。

    ```bash
    .venv\Scripts\Activate.ps1
    ```

3. パッケージをインストール

    ```
    pip install -r requirements.txt
    ```

### Dockerを使用する場合

Docker imageをbuild

```
docker-compose build
```

## 実行方法

### インストール済みのPythonを用いる場合

1. 匿名化したい動画をinputディレクトリに入れる

2. スクリプト実行

```
python main.py --src <手順1でinputディレクトリに入れたファイル名>
```

### Dockerを用いる場合

1. 匿名化したい動画をinputディレクトリに入れる

2. コンテナ経由でスクリプト実行

```
docker-compose run --rm face_anonymizer python main.py --src <手順1でinputディレクトリに入れたファイル名>
```
