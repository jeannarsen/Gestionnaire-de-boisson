print("python lance script")

import re
import string
from tinydb import TinyDB, where
from pathlib import Path


class User: 
    
    DB = TinyDB(Path(__file__).resolve().parent / "db.json", indent=4)


    def __init__(self, first_name:str, last_name:str, adress:str, number_phone:str=""):
        self.first_name = first_name
        self.last_name = last_name
        self.adress = adress
        self.number_phone = number_phone

    def __str__(self):
        return f"{self.first_name}\n{self.last_name}\n{self.adress}\n{self.number_phone}"   
    
    def __repr__(self):
        return f"{self.full_name}\n{self.number_phone}\n{self.adress}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def db_instance(self):
        return User.DB.get((where("first_name" == self.first_name)) & (where("last_name" == self.last_name)))"

    def _check(self):
        self._check_names()
        self._check_phone_number()


    def _check_phone_number(self):
        phone_number = re.sub(r"[+()\s]*", "", self.phone_number)
        print(phone_number)
        if len(phone_number) < 10 or not phone_number.isdigit():
            raise ValueError(f"Number phone {self.phone_number} is not valid!")
        
    def _check_names(self):
        if not (self.first_name and self.last_name):
            raise ValueError("First name and last name are required!")

        special_characters = string.punctuation + string.digits
        print(special_characters)    

        for charactère in self.first_name + self.last_name:
            if charactère in special_characters:
                raise ValueError(f"nom'{self.full_name}' is not allowed in names!")

    def exists(self):
        return bool(self.db_instance)
    
    def delete(self):
        if self.exists():
            return User.DB.remove(doc_ids=[self.db_istance.db_instance])
    
    def save(self, validate_data = False):
        if validate_data:
            self._check()
    
        return User.DB.insert(self.__dict__)
    
def get_all(self):
    return [User(**user) for user in user.DB.all() ]

if __name__ =="__main__":
    from faker import Faker
    fake = Faker(locale = "fr_FR")
    for _ in range(10):
        user = User(
            first_name =fake.first_name(), 
            last_name =fake.last_name(), 
            adress = fake.address(),
            number_phone = fake.phone_number()
            )
           
        print(user)
        print("_" *10)