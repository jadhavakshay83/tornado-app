from botHandler import BotHandler

class APIHandler():
    @staticmethod
    def getAPIs():
        urls = []
        urls.append(("/bot", BotHandler))
        return urls