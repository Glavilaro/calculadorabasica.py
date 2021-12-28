while 1:
 x=float(input("indica el valor de x:"))
 y=float(input("indica el valor de y:"))
 print("selecciona la operacion que desee realizar:")
 print("1. sumar")
 print("2.restar")
 print("3.multiplicar")
 print("4.dividir")
 print("5.raiz")

 n=int(input("selecciona una opcion: ",))

 if n==1:
    resultado=x+y
    print(resultado)
 elif n == 2:
    resultado=x-y
    print(resultado)
 elif n==3:
    resultado=x*y
    print(resultado)
 elif n==4 and y!=0:
    resultado=x/y
    print(resultado)
 elif n==5:
    resultado=x**y
    print(resultado)






