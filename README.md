# mmscreenshot

[![Build Status](https://travis-ci.org/yukkun007/mmscreenshot.svg?branch=master)](https://travis-ci.org/yukkun007/mmscreenshot)
[![codecov](https://codecov.io/gh/yukkun007/mmscreenshot/branch/master/graph/badge.svg)](https://codecov.io/gh/yukkun007/mmscreenshot)
[![Maintainability](https://api.codeclimate.com/v1/badges/fa15a1c245473441c7d7/maintainability)](https://codeclimate.com/github/yukkun007/mmscreenshot/maintainability)
[![Requirements Status](https://requires.io/github/yukkun007/mmscreenshot/requirements.svg?branch=master)](https://requires.io/github/yukkun007/mmscreenshot/requirements/?branch=master)

指定したサイトのスクリーンショットを取得するライブラリ。

## Dependency

下記が必須。`serverless-chrome`を使う場合はバージョンの組合せに注意(後述)。

- Chrome(headless-chromium)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

### serverless-chrome

AWS Lambdaで動作させる場合、[serverless-chrome](https://github.com/adieuadieu/serverless-chrome/releases)がおすすめ。

- 最新のバージョンは1.0.0-55だが動かない
- 以下の組み合わで動確([参照](https://github.com/adieuadieu/serverless-chrome/issues/133))
  - [severless-chrome](https://github.com/adieuadieu/serverless-chrome/releases)==1.0.0-37 (64.0.3282.167 stable channel)
  - chromedriver==2.37
  - selenium==3.141.0

### Install Dependency

#### ダウンロード先

##### serverless-chrome

- https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-37/stable-headless-chromium-amazonlinux-2017-03.zip

##### Chromedriver

- http://chromedriver.storage.googleapis.com/index.html?path=2.37/

#### Install for AWS Lambda

- `serverless-chrome`と`chromedriver`をLambda Layerにあげて使う([参照](https://hacknote.jp/archives/49974/))

#### Install for Local (Mac)

インストールスクリプト→`script/install.sh`

- `Google Chrome Canary`をインストール

```sh
brew install Caskroom/versions/google-chrome-canary
/Applications/Google\ Chrome\ Canary.app/Contents/MacOS/Google\ Chrome\ Canary --version
```

- `chromedriver`をダウンロードして配置

```sh
/usr/local/bin/chromedriver -v
```

### 環境変数

`Chrome`および`ChromeDriver`のパスを環境変数として指定する。プロジェクトディレクトリ直下に、`.env`ファイルを配置して下記のように記載すれば良い。任意のファイルに記載して指定も可能。

#### ローカル

```env
CHROME_BINARY_LOCATION='/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
CHROME_DRIVER_LOCATION='/usr/local/bin/chromedriver'
```

#### AWS Lambda Layer

Lambda Layerでは/opt/に配置される。

```env
CHROME_BINARY_LOCATION='/opt/headless/python/bin/headless-chromium'
CHROME_DRIVER_LOCATION='/opt/headless/python/bin/chromedriver'
```

## Install

```sh
pip install git+https://github.com/yukkun007/mmscreenshot
```

## Usage

```sh
mmscreenshot --help
```

```sh
mmscreenshot "https://weather.yahoo.co.jp/weather/jp/13/4410.html" "//div[@class='forecastCity']/table/tbody/tr/td/div"
```

## Usage (Use Module)

[参照](Use Module)

## Upgrade

```sh
pip install --upgrade git+https://github.com/yukkun007/mmscreenshot
```

## Uninstall

```sh
pip uninstall mmscreenshot
```

## Deveropment

### Prepare

#### 環境変数追加

```sh
export PIPENV_VENV_IN_PROJECT=true  # 仮想環境はprojectディレクトリ配下に作成
```

#### Pipenv導入

```sh
pip install pipenv
```

#### Project 導入

```sh
git clone git@github.com:yukkun007/mmscreenshot.git
cd mmscreenshot
pipenv install --dev
pipenv shell
pip install -e .
```

### Run

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

### How to Use Module

#### Install Package

`-e`をつけると編集可能モードでインストールされるので便利。ソース編集の都度反映される。つけないと、都度`upgrade package`が必要になる。

```sh
pip install -e .
```

#### Use Module

スクリーンショットを取得。

```python
from mmscreenshot.chrome_driver import ChromeDriver
driver = ChromeDriver()
driver.screenshot(
    "https://weather.yahoo.co.jp/weather/jp/13/4410.html",
    "//div[@class='forecastCity']/table/tbody/tr/td/div",
    out_file="./screenshot.png",
)
```

テキスト要素を取得。

```python
from mmscreenshot.chrome_driver import ChromeDriver
driver = ChromeDriver()
text = driver.get_text(
    "https://weather.yahoo.co.jp/weather/jp/13/4410.html",
    "//div[@class='forecastCity']/table/tbody/tr/td/div/table/tbody/tr[2]/td[3]"
)
print(text)
```

#### Upgrade Package (-e付きでInstallしたなら不要)

```sh
pip install --upgrade .
```

or

```sh
pip install -U .
```

#### Uninstall Package

```sh
pip uninstall mmscreenshot
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
