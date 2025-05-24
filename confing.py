import os

class Config:
    # टेलीग्राम बॉट टोकन (BotFather से मिलेगा)
    BOT_TOKEN = os.getenv("BOT_TOKEN")  
    
    # एडमिन की टेलीग्राम यूजर आईडी (जैसे: 1234567890)
    ADMIN_ID = int(os.getenv("ADMIN_ID"))  
    
    # ग्रुप आईडी (कॉमा सेपरेटेड, जैसे: -100xxx,-100yyy)
    GROUP_IDS = [int(gid.strip()) for gid in os.getenv("GROUP_IDS", "").split(",") if gid.strip()]
