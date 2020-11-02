import argparse
import logging
import setenv
from mmscreenshot.core import screenshot


def main():
    parser = argparse.ArgumentParser(
        description="""
    HTMLのスクリーンショットを取得します。
    """
    )

    parser.add_argument("url", help="取得ページのURL")
    parser.add_argument("xpath", help="取得するHTML要素のXPath")
    parser.add_argument("-o", "--out", help="スナップショットの出力先ファイルパス", default="./out.png")
    parser.add_argument(
        "-e", "--env", help=".envファイルのパスを指定します (デフォルトはカレントディレクトリの.env)", default=".env"
    )
    parser.add_argument("-d", "--debug", help="デバッグログ出力をONにします", action="store_true")

    args = parser.parse_args()

    # log設定
    formatter = "%(asctime)s : %(levelname)s : %(message)s"
    if args.debug:
        # ログレベルを DEBUG に変更
        logging.basicConfig(level=logging.DEBUG, format=formatter)
    else:
        logging.basicConfig(format=formatter)

    if setenv.load(args.env) is False:
        parser.print_help()
        return

    screenshot(args.url, args.xpath, args.out)


if __name__ == "__main__":
    main()
