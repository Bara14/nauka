
wzrost = input(" podaj wzrost [cm]: ")
waga = input("podaj wage [kg]: ")


def bmi(wzrost, waga):

    bmi = float(waga)/((float(wzrost)/100)**2)
    print("bmi wynosi: ", float(bmi))
    float(bmi)
    if bmi > 25:
       print(f"waga za duza i wynosi {bmi}!!")

    elif bmi <18.5:
       print(f"niedowaga i wynosi {bmi}")

    elif bmi >18.5 and bmi < 24.9:
       print(f"waga ok! i wynosi {bmi}")


bmi(wzrost, waga)

