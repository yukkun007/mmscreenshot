import argparse
import logging


def main():
    parser = argparse.ArgumentParser(
        description="""
    HTMLの一部分のスクリーンショットを撮ります。
    """
    )

    parser.add_argument(
        "-m", "--mode", help="検索モードを指定します", choices=["rental", "expire", "reserve", "prepare"]
    )
    parser.add_argument("-u", "--users", help="検索対象のユーザを名前(name)で指定します", nargs="*")
    parser.add_argument(
        "-a", "--alluser", help="全ユーザを対象に検索します(--users指定は無効になります)", action="store_true"
    )
    parser.add_argument(
        "-z",
        "--zero",
        help="結果0件の場合の表示モードを指定します",
        default="always",
        choices=["always", "message", "none"],
    )
    parser.add_argument("-r", "--result_type", help="取得する結果の形式を指定します", choices=["message", "info"])
    parser.add_argument("-s", "--separate", help="結果をユーザごとに個別表示します", action="store_true")
    parser.add_argument("-d", "--debug", help="デバッグログ出力をONにします", action="store_true")
    parser.add_argument("-l", "--userlist", help="登録済みユーザのリストを表示します", action="store_true")

    args = parser.parse_args()

    # userlistの処理
    # returnする
    if args.userlist:
        pass
        return

    # log設定
    formatter = "%(asctime)s : %(levelname)s : %(message)s"
    if args.debug:
        # ログレベルを DEBUG に変更
        logging.basicConfig(level=logging.DEBUG, format=formatter)
    else:
        logging.basicConfig(format=formatter)

    if args.mode == "rental" or args.mode == "expire":
        # 借りてる系
        pass
    elif args.mode == "reserve" or args.mode == "prepare":
        # 予約系
        pass
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
