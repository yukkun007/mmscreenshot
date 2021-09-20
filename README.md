# moz-screenshot

[![mozkzki](https://img.shields.io/circleci/build/github/mozkzki/moz-screenshot)](https://circleci.com/gh/mozkzki/moz-screenshot)
[![codecov](https://codecov.io/gh/mozkzki/moz-screenshot/branch/master/graph/badge.svg?token=BRB5vsPkO2)](https://codecov.io/gh/mozkzki/moz-screenshot)
[![Maintainability](https://api.codeclimate.com/v1/badges/df50bbce59225073a577/maintainability)](https://codeclimate.com/github/mozkzki/moz-screenshot/maintainability)
[![Requirements Status](https://requires.io/github/mozkzki/moz-screenshot/requirements.svg?branch=master)](https://requires.io/github/mozkzki/moz-screenshot/requirements/?branch=master)

指定したサイトのスクリーンショットやテキスト要素を取得するライブラリ。

## Function

- screenshot
- get_text

## Requirements

- Chrome (headless-chromiumでもよい)
  - Lambdaで`serverless-chrome`を使う場合は[バージョンの組合せ](#serverless-chromeについて)に注意
  - Macに`Google Chrome Canary`を`homebrew`でインストール

```sh
# install
brew install Caskroom/versions/google-chrome-canary
# install 確認
/Applications/Google\ Chrome\ Canary.app/Contents/MacOS/Google\ Chrome\ Canary --version
```

- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
  - [ダウンロード](http://chromedriver.storage.googleapis.com/index.html?path=2.37/)して配置

```sh
# install 確認
/usr/local/bin/chromedriver -v
```

※ `scripts/install.sh`も参照

## Usage

Environmental variables

`.env`ファイルに書いてproject rootに配置。`.env_sample`をコピーすると楽。

```txt
CHROME_BINARY_LOCATION='/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
CHROME_DRIVER_LOCATION='/usr/local/bin/chromedriver'
```

Install

```sh
pip install git+https://github.com/mozkzki/moz-screenshot
# upgrade
pip install --upgrade git+https://github.com/mozkzki/moz-screenshot
# uninstall
pip uninstall moz-screenshot
```

Coding

### スクリーンショット取得

Yahoo天気予報がscreenshot.pngに保存される。

```python
from moz_screenshot import screenshot
screenshot(
    "https://weather.yahoo.co.jp/weather/jp/13/4410.html",
    "//div[@class='forecastCity']/table/tbody/tr/td/div",
    out_file="./screenshot.png",
)
```

### テキスト要素取得

```python
from moz_screenshot import get_text
text = get_text(
    "https://weather.yahoo.co.jp/weather/jp/13/4410.html",
    "//div[@class='forecastCity']/table/tbody/tr/td/div/table/tbody/tr[2]/td[3]",
)
print(text)
```

## Develop

base project: [mozkzki/moz-sample](https://github.com/mozkzki/moz-sample)

### Prepare

```sh
poetry install
poetry shell
```

### Run (Example)

```sh
python ./examples/example.py
# or
make start
```

### Unit Test

test all.

```sh
pytest
pytest -v # verbose
pytest -s # show standard output (same --capture=no)
pytest -ra # show summary (exclude passed test)
pytest -rA # show summary (include passed test)
```

with filter.

```sh
pytest -k app
pytest -k test_app.py
pytest -k my
```

specified marker.

```sh
pytest -m 'slow'
pytest -m 'not slow'
```

make coverage report.

```sh
pytest -v --capture=no --cov-config .coveragerc --cov=src --cov-report=xml --cov-report=term-missing .
# or
make ut
```

### Lint

```sh
flake8 --max-line-length=100 --ignore=E203,W503 ./src
# or
make lint
```

### Create API Document (Sphinx)

```sh
make doc
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
