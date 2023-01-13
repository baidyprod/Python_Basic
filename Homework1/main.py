a=int(input("Сторона а = "))
b=int(input("Сторона b = "))
c=int(input("Сторона c = "))

if a == 0 or b == 0 or c == 0:
    print("Таких трикутників не існує")
else:
    perimeter = a + b + c

    if a > b and a > c:
        max = a
    elif b > a and b > c:
        max = b
    else:
        max = c

    if a < b and a < c:
        min = a
    elif b < a and b < c:
        min = b
    else:
        min = c

    if perimeter < 10:
        print(min)
    elif perimeter > 20:
        print(max)
    else:
        print("Периметр = ", perimeter)
