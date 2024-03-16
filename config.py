from os import environ 

class Config:
    API_ID = environ.get("API_ID", "15656646")
    API_HASH = environ.get("API_HASH", "bfe52379811049f25bb01692fd9fe7a6")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6559284414:AAED40ypyjfXebeQmnO1byJnuXDNb8MXuQ8") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://kkhanyaseen:khan1234@cluster0.tyguiox.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '819697641').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
