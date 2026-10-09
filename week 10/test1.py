import os
from typing import Literal # gioi han 1 truong chi nhan gia tri co dinh

import anthropic
from dotenv import load_dotenv# ham doc file .env  va nap cac bien trong do vao moi truong
from pydantic import BaseModel, Field, ValidationError



load_dotenv()# doc file .env chua ANTHROPIC_API_KEY de key khong viet cung trong code

#tao client de lay file .env tu Anthropic_api_key tu trong moi truong da tao
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


#luu ten model bang hang so de de doi sau nay
MODEL = "claude-sonnet-5-5"

#SCHEMA dau ra
class DanhGia(BaseModel):
    cam_xuc: Literal["tich cuc", "tieu cuc", "trung_tinh"] #day la noi schema chi nhan 1 trong 3 gia tri, gia tri khac se bao loi
    diem: Field(ge=1, le=10) # field rang buoc tu 1 den 10
    tom_tat: str # mot chuoi tom tat khong rang buoc them


SYSTEM_PROMPT = """...""" # noi viet huong dan cho claude, yeu cau chi tra ve json

def phan_tich(danh_gia: str) -> DanhGia | None: # nhan 1 chuoi tra ve danh gia neu thanh cong hoac None neu loi
    message = client.messages.create( # goi message API
         model = MODEL, #goi model da khoi tao o tren dong 15
         max_token = 300, # gioi han token vua du cho json ngan
         system = SYSTEM_PROMPT, # truyen system prompt de dinh huong cau tra loi
         messages = [{"role": "user", "content": "..."}], #danh sach tin nhan cho thay bang danh_gia
    
    )
    text = message.content[0].text # lay noi dung van ban phan hoi tu tin nhan AI,vd claude API tra ve 1 danh sach khoi luong noi dung
                             # va cai text = message nay lay doan van ban o phan tu dau tien, thuong doan text nay la 1 chuoi json

    try:
        return DanhGia.model_validate_json(text) #QUAN TRONG lay chuoi text dang o dang JSON 
         #va dung thu vien PYDANTIC (DanhGia.model_validate_json(text) de chuyen doi no thanh doi tuong thuoc lop DanhGia
    
    except ValidationError as e:
        print("Output khong hop le:", e) # thong bao khi bi loi chi tiet e tai as e, pydantic se bao loi cu the thieu truong nao, sai dl o dau
        print("Claude da tra ve:", text) # in ra noi dung goc ma AI da tra ve 
        return None # tra ve gia tri None de ham biet rang viec lay du lieu da that bai, giup truong trinh ben ngoai xu ly tiep va bo qua
    
if __name__ == "__main__": #goi file de biet file duoc goi bang import hay da luu ten file nay vao file kahc hay chua
    cac_cau = [
        "Dien thoai dung rat muot, pin trau, rat hai long!",
        "Giao hang cham, hop mop meo, se khong mua lai.",
        "San pham tam duoc, khong co gi dac biet",
    ]
    for cau in cac_cau:
        ket_qua = phan_tich(cau)
        print(ket_qua)
        

