from typing import Optional
import datetime


class Invoice:
    id = ""
    species = ""
    name = ""
    date = datetime.date
    people_confirm = ""
    price = 0.0

    def __init__(self,
                 i_id: str,
                 i_species: str,
                 i_name: str,
                 i_date: datetime.date,
                 i_people_confirm: str,
                 i_price: float
                 ):
        self.species = i_species
        self.id = i_id
        self.name = i_name
        self.date = i_date
        self.people_confirm = i_people_confirm
        self.price = i_price

    def Display(self):
        print(self.id)
        print(self.species)
        print(self.name)
        print(self.date)
        print(self.people_confirm)
        print(self.price)

    def Add(self):
        print("Them hoa don")

    def Edit(self):
        print("Sua hoa don")

    def Delete(self):
        print("Xoa hoa don")


class ImportInvoice(Invoice):
    producer = ""

    def __init__(self,
                 i_id: str,
                 i_species: str,
                 i_name: str,
                 i_date: datetime.date,
                 i_people_confirm: str,
                 i_price: float,
                 i_producer: str
                 ):
        super().__init__(
            i_id,
            i_species,
            i_name,
            i_date,
            i_people_confirm,
            i_price
        )
        self.producer = i_producer

    def Display(self):
        super().Display()
        print(self.producer)


class ExportInvoice(Invoice):
    name_customer = ""
    address_customer = ""
    phone_customer = ""

    def __init__(self,
                 i_id: str,
                 i_species: str,
                 i_name: str,
                 i_date: datetime.date,
                 i_people_confirm: str,
                 i_price: 0.0,
                 i_name_customer: str,
                 i_address_customer: str,
                 i_phone_customer: str
                 ):
        super().__init__(
            i_id,
            i_species,
            i_name,
            i_date,
            i_people_confirm,
            i_price
        )
        self.name_customer = i_name_customer
        self.address_customer = i_address_customer
        self.phone_customer = i_phone_customer

    def Display(self):
        super().Display()
        print(self.name_customer)
        print(self.address_customer)
        print(self.phone_customer)
