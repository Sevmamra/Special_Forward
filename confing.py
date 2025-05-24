import os

class Config:
    BOT_TOKEN = os.getenv("7763888885:AAGGtCSMRc0tvvGCFJwRMmYJBR819JfiOmQ")
    ADMIN_ID = int(os.getenv("6567162029"))
    GROUP_IDS = [int(gid.strip()) for gid in os.getenv("-1002501498159", "-1002665578655").split(",") if gid.strip()]
    
    # डेटाबेस के लिए (SQLite इस्तेमाल करेंगे)
    DB_URL = "sqlite:///groups.db"  # यही फाइल database.py में इस्तेमाल होगी
