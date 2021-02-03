# mmscreenshot

[![yukkun007](https://img.shields.io/circleci/build/github/yukkun007/mmscreenshot)](https://circleci.com/gh/yukkun007/mmscreenshot)
[![codecov](https://codecov.io/gh/yukkun007/mmscreenshot/branch/master/graph/badge.svg)](https://codecov.io/gh/yukkun007/mmscreenshot)
[![Maintainability](https://api.codeclimate.com/v1/badges/fa15a1c245473441c7d7/maintainability)](https://codeclimate.com/github/yukkun007/mmscreenshot/maintainability)
[![Requirements Status](https://requires.io/github/yukkun007/mmscreenshot/requirements.svg?branch=master)](https://requires.io/github/yukkun007/mmscreenshot/requirements/?branch=master)

指定したサイトのスクリーンショットやテキスト要素を取得するライブラリ。

## Requirements

- 動作に必要
  - Chrome(headless-chromium)
  - [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- 開発環境構築に必要
  - pipenv

※ Lambdaで`serverless-chrome`を使う場合は[バージョンの組合せ](#serverless-chromeについて)に注意。

## Usage

### Install

```sh
pip install git+https://github.com/yukkun007/mmscreenshot
```

- [chromeとchromedriverをインストール](#chrome-and-chromedriver)
- [`.env`ファイルを配置](#env)

### Run with command line

コマンドラインからの呼び出し方法。

```sh
mmscreenshot --help
```

```sh
mmscreenshot "https://weather.yahoo.co.jp/weather/jp/13/4410.html" "//div[@class='forecastCity']/table/tbody/tr/td/div"
```

### Use library

ライブラリの使用方法。

#### スクリーンショット取得

```python
from mmscreenshot import screenshot
screenshot(
    "https://weather.yahoo.co.jp/weather/jp/13/4410.html",
    "//div[@class='forecastCity']/table/tbody/tr/td/div",
    out_file="./screenshot.png",
)
```

#### テキスト要素取得

```python
from mmscreenshot import get_text
text = get_text(
    "https://weather.yahoo.co.jp/weather/jp/13/4410.html",
    "//div[@class='forecastCity']/table/tbody/tr/td/div/table/tbody/tr[2]/td[3]",
    dotenv_path="/pat/to/.env"
)
print(text)
```

### Upgrade

```sh
pip install --upgrade git+https://github.com/yukkun007/mmscreenshot
```

### Uninstall

```sh
pip uninstall mmscreenshot
```

## Local Development

### Setup requirements

#### Chrome and chromedriver

下記はMacでの例。詳細は`script/install.sh`を参照。

- `Google Chrome Canary`をインストール

```bash
brew install Caskroom/versions/google-chrome-canary
/Applications/Google\ Chrome\ Canary.app/Contents/MacOS/Google\ Chrome\ Canary --version
```

- `chromedriver`を[ダウンロード](http://chromedriver.storage.googleapis.com/index.html?path=2.37/)して配置

```sh
/usr/local/bin/chromedriver -v
```

#### pipenv

`pipenv`を使うので無ければ入れる。

```bash
pip install pipenv # pipenvを導入
export PIPENV_VENV_IN_PROJECT=true  # 仮想環境をprojectディレクトリ配下に作成
```

### Setup

下記の通り。

```bash
git clone git@github.com:yukkun007/mmscreenshot.git
cd mmscreenshot
pipenv sync --dev # "sync"でPipfile.lockと一致した環境になる
pipenv shell # 仮想環境に入る, pipenv run pip install -e . でも可
pip install -e . # mmscreenshot自体をinstall
```

- `pipenv install`は依存関係の解決がすごく遅いので`sync`を使う
- `pipenv sync`では「再ロック」(PipfileやPipfile.lockの内容更新)はされない
- 参考: [Pipfile.lockで固定された依存関係を再現するならpipenv syncコマンドを使おう | Developers.IO](https://dev.classmethod.jp/articles/pipenv-sync-is-useful/)

#### .env

プロジェクトディレクトリ直下に`.env`ファイルを配置する。
ローカル環境の`Chrome`および`ChromeDriver`のパスを指定。

下記はMac環境のサンプル(`.env_sample`)。

```env
CHROME_BINARY_LOCATION='/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
CHROME_DRIVER_LOCATION='/usr/local/bin/chromedriver'
```

### Run

Yahoo天気予報がscreenshot.pngに保存される。

```sh
pipenv run start
```

### Lint

```sh
pipenv run lint
```

### Unit Test

```sh
pipenv run ut
```

### Create API Document (Sphinx)

`docs/_build/html`に出力される。

```sh
pipenv run doc
```

### Library management

ローカル環境で、このライブラリを操作する方法。

#### Install library

```sh
pip install -e .
```

- [Setup](#setup)で実施済み
- `-e`をつけると編集可能モードでインストールされるので便利
  - ソース編集の都度反映される
  - つけないと、都度[Upgrade library](#upgrade-library)が必要

#### Upgrade library

`-e`付きでインストールしたなら不要。

```sh
pip install --upgrade .
```

または

```sh
pip install -U .
```

#### Uninstall library

```sh
pip uninstall mmscreenshot
```

### Update dependency modules

requires-ioを使っている。pull reqが来るので下記手順で対応。

```sh
git checkout requires-io-master
# remove Pipfile.lock
pipenv install --dev
# run and test
git add Pipfile.lock
git commit -m "update modules"
git push origin requires-io-master
# merge branch "requires-io-master" at github web ui
```

## AWS Lambda で使う場合

### 注意点

- `serverless-chrome`と`chromedriver`をLambda Layerに上げる必要あり([参照](https://hacknote.jp/archives/49974/))
- フォントがないと文字化けする
  - デプロイパッケージのルートに`.fonts`ディレクトリを作成してフォントを格納する([参照](https://qiita.com/havveFn/items/bb8cd0d937c671100200))
  - なお、CircleCI等でも同様だが、同じく`~/.fonts`に置くか[インストール](https://worklog.be/archives/3422#Google_Noto_Fonts)すれば良い

### serverless-chromeについて

Chrome を AWS Lambda で動作させる場合に利用できる。

- 最新のバージョンは1.0.0-55だが動かない
- 以下の組み合わで動確している([参考](https://github.com/adieuadieu/serverless-chrome/issues/133))
  - [severless-chrome](https://github.com/adieuadieu/serverless-chrome/releases)==[1.0.0-37](https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-37/stable-headless-chromium-amazonlinux-2017-03.zip) (64.0.3282.167 stable channel)
  - [chromedriver==2.37](http://chromedriver.storage.googleapis.com/index.html?path=2.37/)
  - selenium==3.141.0

### 環境変数

Lambda Layerではchrome等が/opt/に配置される。
`.env`は下記のようにする。

```env
CHROME_BINARY_LOCATION='/opt/headless/python/bin/headless-chromium'
CHROME_DRIVER_LOCATION='/opt/headless/python/bin/chromedriver'
```

## 配布物関連

<details>

### ソースコード配布物の作成

dist/ 以下に mmscreenshot-0.0.1.tar.gz が生成される。

```sh
python setup.py sdist
```

### ソースコード配布物から pip でインストール

```sh
pip install mmscreenshot-0.0.1-tar.gz
```

### ビルド済み配布物(wheel 形式)の作成

dist/ 以下に mmscreenshot-0.0.1-py3-none-any.whl が生成される。

```sh
python setup.py bdist_wheel (wheelパッケージが必要)
```

### ビルド済み配布物(wheel 形式)から pip でインストール

```sh
pip install mmscreenshot-0.0.1-py3-none-any.whl
```

</details>

## 参考

<details>

### パッケージング/開発環境

- <https://techblog.asahi-net.co.jp/entry/2018/06/15/162951>
- <https://techblog.asahi-net.co.jp/entry/2018/11/19/103455>

### コマンドライン引数のパース

- <https://qiita.com/kzkadc/items/e4fc7bc9c003de1eb6d0>

### 環境変数の定義

- <https://pod.hatenablog.com/entry/2019/04/29/164109>

### TravisCIでファイルを(簡単に)暗号化して使用する

- <https://qiita.com/kmats@github/items/d22fd856883e6c16d7ea>

</details>
