def jugar(intento=1):
    respuesta = input("De que color es la fruta?")
    if respuesta != "naranja":
        if intento < 3:
            print ("\n Fallaste, te quedan "+str(3-intento)+" intento/s")
            intento+=1
            jugar(intento)
        else:
            print("Perdiste, mejor suerte la próxima")
    else:
        print("\nGanaste!")


def func_fibonacci(n,sum=0):
    if(n<2):
        return n
    sum = func_fibonacci(n-1,sum)+func_fibonacci(n-2,sum)
    return sum

def user_fibonacci():
    respuesta = input("Fibonacci de que numero deseas?")
    try:
        num = int(respuesta)
    except:
        print ("No ingresaste un numero, me da ammsiedad")
        return
    a = func_fibonacci(num)
    print(a)


def func_factorial(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return n*func_factorial(n-1)


def user_factorial():
    respuesta = input("Factorial de que numero deseas?")
    try:
        num = int(respuesta)
    except:
        print("No ingresaste un numero, me da ammsiedad")
        return
    a = func_factorial(num)
    print(a)

jugar()
user_fibonacci()
user_factorial()

print("\nMuchas gracias")
print("\nDavid Omar Enriquez Reyes")


