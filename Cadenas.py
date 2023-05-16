#Ejercicio 1
#Usando la función de impresión, imprima su nombre completo

x= "Exequiel Gozategui"
print(x)


#Ejercicio 2
#Se puede imprimir en múltiples líneas usando tres apóstrofes ‘ ‘ ‘ y escribiendo el mensaje sobre más de una línea.
#Imprima su nombre de nuevo completo, pero esta vez usando una línea por cada parte

print('''Exequiel
Gozategui''')

#Ejercicio 3
#Hay otra forma de imprimir sobre múltiples líneas sin los ‘ ‘ ‘. Uno inserta el carácter especial \n donde se debe tomar una nueva línea adentro
#de la cadena que uno quiere imprimir.
#Imprima su nombre de nuevo, con una parte por línea utilizando esta técnica.
print("Exequiel \n Gozategui ")


#Ejercicio 4
#Guarde su nombre en la variable NombreCompleto
NombreCompleto="Exequiel Gozategui"

#Ejercicio 5
#Utilice una variable asignada como entrada por el usuario para almacenar su mail
Mail= input("Igrese su mail")

#Ejercicio 6
#Determine el tamaño de una variable por su cantidad de caracteres incluyendo espacios. ¿Cuántos caracteres hay en nombre completo?
print(len(NombreCompleto))


#Ejercicio 7
#Imprima el 5to carácter de su nombre

print(NombreCompleto[5])

#Ejercicio 8
#Imprima solo su nombre, usando dla impresión de rango de caracteres de una variable
print(NombreCompleto[0:8])

#Ejercicio 9
#Imprima el mes de su cumpleaños Todo en Mayúscula

MesCumple="Junio"
print(MesCumple.upper())

#Ejercicio 10
#Imprima su nombre con minúscula, excepto la letra inicial y su apellido todo con mayúscula
print(NombreCompleto.capitalize())
#Ejercicio 11
#Cree dos variables, una para su nombre y otra para su apellido
#Ahora busque su apellido, dentro de su nombre completo, usando el comando Find
Nombre= "Exequiel"
Apellido="Gozategui"
print(NombreCompleto.find(Apellido))

#Ejercicio 12
#En su nombre completo (nombre y apellido), reemplace su nombre por su Nick
nick="Goza"
print(NombreCompleto.replace(Nombre,nick))

#Ejercicio 13
#Concatene su sobrenombre a su nombre completo
print(nick+NombreCompleto)

#Ejercicio 14
#Utilice el comando strip para eliminar los espacios de la variable cadenaconespacios = “ CESIT, MAIPU “
cadenaconespacios = " CESIT, MAIPU "
print(cadenaconespacios.strip())


#Ejercicio 15
#Utilice el comando split para crear una lista, a partir de una variable que contenga a sus amigos como: AmigosdeSuNombre
#Recuerde definir un espacio como separador
#Ej: AmigosdeSilvina= “Pablo, Carina, Florencia, Andrea, Silvana”

AmigosMios= "Tizi, Capo, Capo2, Tizi2"
separador= " "
comandoSplit= AmigosMios.split(separador)
print("mi lista de amigos es",comandoSplit )


#DESAFÍO
#CADENAS
#Dada la variable python, nombredelestudiante = “Este es el trabajo de: apellido, nombre”
#Escriba un programa para editar la variable, de modo que contenga su nombre, en el formato ‘apellido, nombre’
#Utilice las funciones para la modificación de cadenas de caracteres provistas por Python.
#A continuación debe imprimir la variable.
#Ejemplo: “Este es el trabajo de: Juan Perez”

nombredelestudiante= "Este es el trabado de: apellido, nombre"
nombredelestudiante1="Este es el trabajo de: Gozategui, Exequiel"
Estudiante= nombredelestudiante.replace(nombredelestudiante,nombredelestudiante1)
print(Estudiante)

