firstNumber = input("Podaj pierwsza liczbe: ")
secondNumber = input("Podaj druga liczbe: ")
operator = input("Podaj znak działania: + - * / : ")






def newmath (one, two, lista, operator):

    for i in lista:
        if i == operator:
            wynik = one operator two
            print(wynik)
            break

        else:
            print("nie ma takiego operatora:( : ", operator)


lista = ["+", "-", "*", "/", "aaa"]


newmath(secondNumber, firstNumber,lista, operator)





def math (first, second, znak):
    if znak == "+":
         print (float(first) + float(second))

    elif znak == "-":
        print(float(first) - float(second))

    elif znak == "*":
        print(float(first) * float(second))

    elif znak == "/":
        print(float(first) / float(second))



try:
    math(firstNumber, secondNumber, operator)
except ZeroDivisionError:
            print("Nie dzielimy prez 0!!!")

