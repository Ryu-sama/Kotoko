from nksama import bot 
import logging




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    bot.run()
    with bot:
        bot.send_message(-1001594147818 , "wisdom")
    


