import os

###########################################################################################################
# Programa para verificar que si se toma un número y se lo eleva al cuadrado y al número que de esta ope- #
# ción se suma sus digitos elevando cada dígito al cuadrado y sumándolos con los digitos del cubo del     #
# número que se tomó al inicio, el programa mostrará el valor solo si se cumple que la suma de los proce- #
# sos anteriores es igual a dicho número.                                                                 #
# Por ejemplo:                                                                                            #
# Se toma al número 4; este número se lo eleva al cuadrado 4**2 = 16; los digitos del 16 se elevan al     #
# cubo así 1**3 + 6**3; ahora se eleva al cubo el número tomado al inicio 4, entonces queda 4**3 = 64     #
# los digitos de este número se suman con los anteriores así:                                             #
# 1**3 + 6**3 + 6 + 4 = 227. En caso de coincidir la suma anterior con el número tomado al inicio, se     #
# muestra en la pantalla.                                                                                 #
###########################################################################################################

os.system('cls')

# Solicitando un número máximo para realizar la prueba
limit = int(input('Ingrese un número límite: '))

# Creando las variables para guardar el cuadrado y el cubo del número
square = 0
cube = 0

# Funciones para sumar los dígitos
def sum_of_digits_square(number2):
    square_sum = 0
    # Convirtiendo a string para que lo pueda iterar
    conversion2 = str(number2)
    for k in conversion2:
        square_sum = square_sum + int(k)**3
    return square_sum

def sum_of_digits_cubs(number1):
    cubes_sum = 0
    # Convirtiendo a string para que lo pueda iterar
    conversion1 = str(number1)
    for j in conversion1:
        cubes_sum = cubes_sum + int(j)
    return cubes_sum

    
def total(value1,value2):
    return (value1 + value2)


for i in range(1,limit):
    square = i**2
    cube = i**3
    val1 = sum_of_digits_square(square)
    val2 = sum_of_digits_cubs(cube)
    if(total(val1,val2) == i):
        print(i)
    else:
        continue

