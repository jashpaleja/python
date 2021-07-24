try:
    a=int(input("AGE:"))
    print(a)
    income= 200000
    risk=income/a
    print(risk)
except ZeroDivisionError:
    print('age cannot be zero')
except ValueError:
    print("invalid input")
