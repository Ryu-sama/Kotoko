from nksama import bot
import logging

logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    filemode="a",
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
)


def main():
    bot.run()
    bot.send_message(-1001594147818, "He He He")


if __name__ == "__main__":
    main()
