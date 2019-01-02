from typing import Optional
import datetime


class Personnel:
    id = ""
    name = ""
    age = 0
    address = ""
    phone_number = ""
    date = datetime.date
    
    def __init__(self,
                 p_id: str,
                 p_name: str,
                 p_age: int,
                 p_address: str,
                 p_phone_number: str,
                 p_date: datetime.date
                 ):
        
        self.id = p_id
        self.name = p_name
        self.age = p_age
        self.address = p_address
        self.phone_number = p_phone_number
        self.date = p_date
     
    def Display(self):
        print(self.id)
        print(self.name)
        print(self.age)
        print(self.address)
        print(self.phone_number)
        print(self.date)

    def Add(self):
        print("Them moi nhan vien")

    def Edit(self):
        print("Sua thong tin nhan vien")

    def Delete(self):
        print("Xoa thong tin nhan vien")
