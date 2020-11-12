import argparse
import logging

from mmscreenshot.env import load_env
from mmscreenshot import screenshot


def main():
    parser = argparse.ArgumentParser(
        description="""
    HTMLのスクリーンショットを取得する。
    """
    )

    parser.add_argument("url", help="取得ページのURL")
    parser.add_argument("xpath", help="取得するHTML要素のXPath")
    parser.add_argument("-o", "--out", help="スクリーンショット画像の出力先ファイルパス", default="./screenshot.png")
    parser.add_argument("-e", "--env", help=".envファイルのパス (デフォルトはカレントディレクトリの.env)", default=".env")
    parser.add_argument("-d", "--debug", help="デバッグログ出力をON", action="store_true")

    args = parser.parse_args()

    # log設定
    formatter = "%(asctime)s : %(levelname)s : %(message)s"
    if args.debug:
        # ログレベルを DEBUG に変更
        logging.basicConfig(level=logging.DEBUG, format=formatter)
    else:
        logging.basicConfig(format=formatter)

    if load_env(args.env) is False:
        parser.print_help()
        return

    screenshot(args.url, args.xpath, args.out)


if __name__ == "__main__":
    main()
