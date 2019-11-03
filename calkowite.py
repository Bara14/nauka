number = int(input("Podaj liczbe calkowita: "))
print(f"Liczby calkowite nieparzyste, niewiększe od {number} to: ")
for i in range(number+1):
    if i % 2 != 0:
        print(i)
