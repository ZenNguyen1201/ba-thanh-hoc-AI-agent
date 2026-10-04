from dotenv import load_dotenv
import os

load_dotenv()
bi_mat = os.getenv("MY_SECRET")
print(bi_mat)