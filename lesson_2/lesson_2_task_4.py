n1 = input("Назовите число")
n = int(n1)
for x in range(1, n):
    if x % 3 == 0 and x % 5 == 0:
        print("FlizzBuzz")
    elif x % 5 == 0:
        print("Blizz")
    elif x % 3 == 0:
        print("Flizz")
    else:
        print(x)

