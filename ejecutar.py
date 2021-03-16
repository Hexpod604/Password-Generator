#Vamos a hacer un creador de contraseñas con Python

import random #Importamos "random"

#Definimos todas las letras, números y simbolos que tendrá nuestra contraseña

minus = "abcdefghijklmnñopqrstuvwxyz" #Definimos las minúsculas
mayus = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ" #Definimos las mayúsculas
numeros = "0123456789" #Definimos los números
simbolos = "[]{}()*:;.,-_#%$¿?¡!" #Definimos los símbolos

todo = minus + mayus + numeros + simbolos #Juntamos las minúsculas, mayúsculas, números y símbolos

largo = 32 #Seleccionamos la longitud de nuestra contraseña
contraseña = "".join(random.sample(todo, largo)) #Creamos una contraseña aleatoria con lo seleccionado anteriormente
print("Contraseña: " +  contraseña) #Escribimos nuestra contraseña en el terminal

#Espero que les sirva, Cualquier duda / pregunta, Hablenme por Discord: https://discord.gg/Qh8p6TWZbJ
