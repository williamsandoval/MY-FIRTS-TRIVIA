import time

import time

print ("Hola, nos vemos en un momento")

time.sleep(2)

print ("ya estoy aqui!")

x = input ("como te llamas? ")
print ("hmmm")
time.sleep(1)
print("hola",x,"juguemos una trivia")

puntaje = 0

print ("Bienvenido a la trivia sobre futbol")
print ("Pondremos a prueba tus conocimientos")
print("Tienes", puntaje, "puntos")

nombre = input("ahora escribe tu nombre: ")

print("\n Hola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")

print ("1) ¿de que pais es el FC Barcelona?")
print ("a) peru")
print ("b) china")
print ("c) españa")
print ("d) italia")

respuesta_1 = input("\nTu respuesta: ")

while respuesta_1 not in ("a", "b", "c", "d"):
  respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_1 == "c":
  puntaje += 10
  print("Muy bien", nombre,"conseguiste", puntaje,"puntos" "!")
else:
  print("Incorrecto", nombre,"conseguiste", puntaje,"puntos" "!")

print ("\n1) ¿quien tiene mas champions league?")
print ("a) lionel messi")
print ("b) karim benzema")
print ("c) tony kross")
print ("d) ronaldinho")

respuesta_2 = input("\nTu respuesta: ")

while respuesta_2 not in ("a", "b", "c", "d"):
  respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_2 == "a":
  print ("Incorrecto!", nombre, "messi solo tiene cuatro champions league")
elif respuesta_2 == "b":
  print ("Incorrecto!", nombre, "benzema solo tiene cuatro champions league")
elif respuesta_2 == "d":
  print ("Incorrecto!", nombre, "ronaldinho solo tiene dos champions league")
else:
  puntaje += 10
  print ("Muy bien", nombre, "!")

print ("Gracias por jugar la trivia", nombre,"conseguiste", puntaje, "puntos")