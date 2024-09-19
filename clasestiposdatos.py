print("Clases v2 Jesus Daniel Flores")


class Datos:
    def __init__(self, estatura, peso):
        self.estatura = estatura
        self.peso = peso

    def mostrar_datos(self):
        print(f"Estatura: {self.estatura}, Peso: {self.peso}")

    def mi_lista(self):
        celulares = ["Samsung", "Ipad 18", "Chafa"]
        print(celulares)
        for cel in celulares:
            print(cel) 

    def mi_tupla(self):
        futbolistas = ("Messi", "Cristiano Ronaldo", "Neymar")
        print(futbolistas)
        for jugador in futbolistas:
            print(jugador)

    def mi_diccionario(self):
        frutas = {
            "manzana": "roja",
            "banana": "amarilla",
            "uva": "verde"
    }
        print(frutas)
        for fruta, color in frutas.items():
            print(f"La {fruta} es {color}.")

    def mi_set(self):
        animales = {"perro", "gato", "elefante"}
        print(animales)
        for animal in animales:
            print(animal)

    


info=Datos(1.75, 58)
info.mostrar_datos()
print("Lista de marcas de celulares Jesus Flores")
info.mi_lista()
info.mi_tupla()
info.mi_diccionario()
info.mi_set()