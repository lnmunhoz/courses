dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
if dividendo < divisor:
    print("Dividendo precisa ser maior que o divisor!")
else:
    mdc = divisor
    resto = dividendo % divisor
    while resto > 0:
        mdc = resto
        resto = dividendo % resto
    print(mdc)
    
       



