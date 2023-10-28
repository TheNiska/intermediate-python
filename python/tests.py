import logging as lg
from second import do_stuff


def main():
    print('Doing stuff in root module')
    lg.warning("Warning in main module")
    do_stuff()


if __name__ == '__main__':
    # configuring logging
    lg.basicConfig(
        level=lg.INFO, filename='logs', filemode='a', encoding='utf-8',
        format="%(asctime)s - %(levelname)s\n%(message)s\n",
        datefmt="%d-%m-%Y %H:%M:%S"
    )

    main()
