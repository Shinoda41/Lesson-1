from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Xiaomi", "Mi 6", "+79123456789"))
catalog.append(Smartphone("Samsung", "Galaxy S21", "+79234567890"))
catalog.append(Smartphone("Apple", "iPhone 6", "+79587699307"))
catalog.append(Smartphone("Google", "Pixel 4", "+79456789012"))
catalog.append(Smartphone("Nokia", "3310", "+79567890123"))

for phone in catalog:
    print(f"{phone.phone_brand} - {phone.phone_model}. {phone.phone_number}")