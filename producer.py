from typing import Optional


class Producer:
    id = ""
    name = ""
    address = ""

    def __init__(self,
                 p_id: str,
                 p_name: str,
                 p_address: str
                 ):
        self.code = p_id
        self.name = p_name
        self.address = p_address

    def Display(self):
        print("Hien thi nha cung cap")
        print(self.id)
        print(self.name)
        print(self.address)

    def Add(self):
        print("Them nha cung cap")

    def Edit(self):
        print("Sua nha cung cap")

    def Delete(self):
        print("Xoa nha cung cap")
