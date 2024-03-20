class Smartphone:
    
    def __init__(self, phone_brand, phone_model, phone_number ):
        self.phone_brand = phone_brand
        self.phone_model = phone_model
        self.phone_number = phone_number

    def sayBrand(self):
        print("Марка телефона:", self.phone_brand)

    def sayModel(self):
        print("Модель Телефона:", self.phone_model)

    def sayNumber(self):
        print("Номер телефона: +79", self.phone_number)         