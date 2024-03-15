year1 = input("Какой сейчас год?")
year=int(year1)
print("Сейчас", year,"год")
if year % 4 == 0:
    print("год",year,":", True)
else:
    print("год", year,":", False)
