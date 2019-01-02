from typing import Optional
import datetime


class Product:
    id = ""
    species = ""
    producer = ""
    date_added = datetime.date

    def __init__(self,
                 p_id: str,
                 p_species:str,
                 p_producer:str,
                 p_date:Optional[datetime.date]
                 ):
        self.id = p_id
        self.species = p_species
        self.producer = p_producer
        self.date_added = p_date

    def Display(self):
        print(self.id)
        print(self.species)
        print(self.producer)
        print(self.date_added)

    def Add(self):
        print("Them moi san pham")

    def Edit(self):
        print("Sua thong tin san pham")

    def Delete(self):
        print("Xoa san pham")


class ProductDetails(Product):
    species_details = ""
    size = 0
    color = ""

    def __init__(self,
                 p_id: str,
                 p_species: str,
                 p_producer: str,
                 p_date: Optional[datetime.date],
                 pd_species: str,
                 pd_size: int,
                 pd_color: str,
                 ):
        super().__init__(p_id, p_species, p_producer, p_date)
        self.species_details = pd_species
        self.size = pd_size
        self.color = pd_color

    def Display(self):
        super().Display()
        print(self.species_details)
        print(self.size)
        print(self.color)
