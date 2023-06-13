# Concatenacion de cadenas(Tambien conocido como interpolacion de cadenas)
# Supongamos que queremos crear una cadena que dice "subscribete a ____"
'''
youtuber = "Juanito" # Almacenamos el nombre del youtuber en una variable

# algunas formas de hacerlo 
print("Subscribete a " + youtuber)
print("Subscribete a {}".format(youtuber))
print(f"Subscribete a {youtuber}")
'''


adj = input("Adjetivo: ")
verb1 = input("Verbo: ")
verb2 = input("Verbo: ")
famous_person = input("Peronaje famoso: ")

madlib = f"La programacion en Python es tan {adj}! Me emocionamucho todo el tiempo porque\
me encanta {verb1}.Siempre mantente hidratado y {verb2} igual que {famous_person}!"

print(madlib)