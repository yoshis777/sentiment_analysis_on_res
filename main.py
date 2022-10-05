import sys

from dotenv import load_dotenv

from output import Output


def main():
    print("main_function")
    load_dotenv()

    try:
        output = Output()
        output.output(sys.argv[1])
        output.average()
    except IndexError:
        print('コマンドライン引数が指定されていません')
        sys.exit()


main()
