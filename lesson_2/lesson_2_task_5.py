month_to_season = input("Какой сейчас месяц?")
month_to_season = int(month_to_season)
if month_to_season in range(1,3) or month_to_season == 12:
    print("Зима")
elif month_to_season in range(3,6):
    print("Весна")
elif month_to_season in range(6,9):
    print("Лето")
elif month_to_season in range(9,13):
    print("Осень")
else:
    print("Значение должно быть от 1 до 12")