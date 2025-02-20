# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "20697474")

API_HASH = os.environ.get("API_HASH", "1acf41c146d578a57741ab0760208eb4")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7568011035:AAHcbHFH4liBxobuVrVtIZWdya5MGD6bjAc") 

FORCE_SUB = os.environ.get("FORCE_SUB", "chrunchyrool") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "Cluster0")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://mdaquibjawed1106:Sq9GdsM3TbWzd3aV@cluster0.nzjib.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5851158054').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
