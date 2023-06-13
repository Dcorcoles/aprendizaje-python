# Concatenacion de cadenas(Tambien conocido como interpolacion de cadenas)
# Supongamos que queremos crear una cadena que dice "subscribete a ____"
'''
youtuber = "Juanito" # Almacenamos el nombre del youtuber en una variable

# algunas formas de hacerlo 
print("Subscribete a " + youtuber)
print("Subscribete a {}".format(youtuber))
print(f"Subscribete a {youtuber}")
'''


adj = input("Inserta un Adjetivo: ")
verb1 = input("Inserta un Verbo: ")
verb2 = input("Inserta otro Verbo: ")
famous_person = input("Inserta el nombre de un Peronaje famoso: ")

madlib = f"La programacion en Python es tan {adj}! Me emociona mucho todo el tiempo porque\
 me encanta {verb1}.Siempre mantente hidratado y {verb2} igual que {famous_person}!"

print(madlib)