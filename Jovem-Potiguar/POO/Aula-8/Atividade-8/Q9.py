
class Animal:
    def fazer_som(self):
        print("Som genérico")

class Cachorro(Animal):
    def fazer_som(self):
        super().fazer_som()
        print("Au Au")

cachorro = Cachorro()
cachorro.fazer_som()