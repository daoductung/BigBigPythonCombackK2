from typing import Optional


class Customer:
    name = ""
    age = 0
    address = ""
    id = ""

    def __init__(self,
                 c_id: str,
                 c_name: str,
                 c_age: int,
                 c_address: str
                 ):
        self.name = c_name
        self.age = c_age
        self.address = c_address
        self.id = c_id

    def Display(self):
        print(self.id)
        print(self.name)
        print(self.age)
        print(self.address)

    def Add(self):
        print("Them moi khach hang")

    def Edit(self):
        print("Sua thong tin khach hang")

    def Delete(self):
        print("Xoa thong tin khach hang")
