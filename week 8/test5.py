from dotenv import load_dotenv

import os
load_dotenv()
key =os.getenv("ANTHROPIC_API_KEY")

if key:
    print("Da luu key thanh cong, do dai:", len(key))
else:
    print("Chua tim thay key")