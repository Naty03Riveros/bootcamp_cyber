# 1. Imprime "Hola, mundo"

print("Hola,mundo" )

# 2. Imprime "Hola, Natalia" con el nombre en una variable

nombre ="Natalia"

print("Hola,",nombre)

print("Hola, " + nombre) # con un +

# 3. Imprimir "Hola 156!" con el número en una variable

numero = 3

print( "Hola", numero, "!") # con una coma

print("Hola " + str(numero) + " !") # con un + -- este debería arrojar un error!, corrígelo con conversión

# 4. Imprimir "Me encanta comer tacos y arepas" con las comidas en variables

comida1 = "chipa"

comida2 = "sopa paraguaya"

print( "¡Me encanta comer {} y {}!".format(comida1,comida2) ) # con .format()

print(f"¡Me encanta comer {comida1} y {comida2}!")
# 5. BONUS-otros métodos 
print(" y ".join([f"¡Me encanta comer {comida1}", comida2 + "!"]))
print("¡Me encanta comer " + comida1 + " y " + comida2 + "!")

