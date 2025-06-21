def pedir_cantidad_de_notas():
    while True:
        try:
            cantidad = int(input("Ingresa la cantidad de notas: "))
            if cantidad >= 2:
                break
            else:
                print("Debes ingresar al menos 2 notas.")
        except:
            print("Valor invalido. Solo puedes ingresar numeros.")
    return cantidad

cantidad = pedir_cantidad_de_notas()

def pedir_notas():
    contador = 0
    lista_notas = []
    while contador < cantidad:
        try:
            nota = float(input(f"Ingresa tu nota N°{contador+1}: "))
            if nota >= 1 and nota <= 7:
                lista_notas.append(nota)
                contador += 1
            else:
                print("El rango de notas permitido es 1-7.")
        except:
            print("Valor invalido. Solo puede ingresar numeros.")
    return lista_notas

lista_notas = pedir_notas()

def calcular_promedio():
    suma = 0
    for i in(lista_notas):
        suma += i
    promedio = suma / len(lista_notas)
    print(f"El promedio de tus notas es {promedio}.")

calcular_promedio()