nombre = input("Ingrese su nombre: ")
print(f"Hola, {nombre}!bienvenido a PYthon")

num1 =5
num2 =3
print(f"La suma de {num1} y {num2} es: {num1 + num2}")
print(f"La resta de {num1} y {num2} es: {num1 - num2}")
print(f"La multiplicación de {num1} y {num2} es: {num1 * num2}")
print(f"La división de {num1} y {num2} es: {num1 / num2}")

tempsu=float(input("Ingrese la temperatura en grados Celsius: "))
print(f"La temperatura en Fahrenheit es: {tempsu * 9/5 + 32} °F")

nombre = ("Edwin")
apellido= ("bebesander")
edad= int(21)
print(f"Mi nombre es {nombre} {apellido} y tengo {edad} años.")

numusuario=int(input("Ingrese un número entero: "))
if numusuario % 2 == 0:
   print(f"El número {numusuario} es par.")
else:
    print(f"El número {numusuario} es impar.") 

numusuario1=int(input("Ingrese un número : "))
numusuario2=int(input("Ingrese un número : "))
numusuario3=int(input("Ingrese un número : "))
if numusuario1 >= numusuario2 and numusuario1 >= numusuario3:
    print(f"El número mayor es: {numusuario1}")
elif numusuario2 >= numusuario1 and numusuario2 >= numusuario3:
    print(f"El número mayor es: {numusuario2}")
else:
    print(f"El número mayor es: {numusuario3}")

for i in range(1, 11):
    print(i)

for x in range(1,51):
    
     numero = 1
     suma = 0 
     while numero <= 50:
         suma += numero
numero += 1
print(f"La suma de los números del 1 al 50 es: {suma}") 

contraseña="bbsomi"
if contraseña == "bbsomi":
    print("Acceso concedido.")
else:
    print("Acceso denegado.")

    class animal():
        def comer():
            print("El animal está comiendo.")

    class gato(animal):
        def maullar():
            print("miau miau")

    tomas = gato()
    tomas.maullar
    tomas.comer
     
