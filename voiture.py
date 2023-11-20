# coding: utf-8
import os


class Voiture:
    def __init__(self):
        self._nom = "ferrai"
        self.roues = 4
    def get_nom(self):
        print("récupérer le nom de la voiture")
        return self._nom
    def set_nom(self,x):
        print("changement non de la voiture")
        self._nom = "peugeot"
    voiture=property(get_nom, set_nom)



class Car(object):
    roues = 4
    moteur = 1
    def __init__(self):
        self._nom = "A determiner"
    def allumer(self):
        print ("voiture demare")

class voitureSport(Car):
    def __init__(self):
        self._nom = "Ferrari"
    def allumer(self):
        Car.allumer(self)
        print ("voiture de sport demare")


user = "bra"
def mon_decorateur(fonction):
    def autre_fonction():
        print("action refusé")
        if user != "br":
            return autre_fonction()
    return fonction
@mon_decorateur
def do_that():
    print("exécution des instructions")



class MonIter():
    current = 0
    def __init__(self, stop):
        self.stop = stop
    def __iter__(self):
        return self


liste = [1,2,3,5,4,58,6,9,8,74,58,96]
for i in liste :
    print(i)


class MonIter():
    i = 0
    def __init__(self, stop):
        self.stop=stop

    def __iter__(self):
        return self

    def next(self):
        self.i = i+1

        if self.i > self.stop:
            raise StopIteration
        if self.i == 5:
            print("deja 5 eme tour")

        return self.i

for j in MonIter(10):
    print(j)

    def generateur():
        yield "a"
        yield "b"
        yield ("c")

    i=generateur()
    for j in i:
        print(j)

def gene(n):
    for i in range(n):
        if i == 5:
            print("5 eme position")
        yield i+1

j= gene(10)
for i in j:
    print(i)

import re
m = re.search(r"Bienvenue chez (?P<chezqui>\w+) ! Tu as (?P<age>\d) ans", "Bienvenue chez olivier ! Tu as 32 ans")
if m is not None:
    print(m.group('chezqui'))
    print(m.group('age'))

print(re.findall("([0-9]+)","Bonjour 111 aurevoir 222"))
print(re.match("GR(.)?S","GRIS"))
print(re.match("GR(.)+S","GRIS"))
print(re.match("GR(I)+S","GRIS"))

fichier = open("C:/Administratif/caf/data.txt","a")
print(fichier)
fichier.write("\nBonjour")
fichier.close()

with open("C:/Administratif/caf/data.txt","r") as fichier:
   print(fichier.read())
    fichier.write("\nBrahim")

import mmap
import os
with open("data_6.txt","a") as file:
    size = file.seek(0,2)
    file.seek(0)
    file.write("bonjour")
    file.write("\nbrahim")
    os.chmod("data_6.txt",777)
    mm = mmap.mmap(file.fileno(),size)
    content = mm.read()
    print(content)
    file.close()


with open("C:/Administratif/caf/data_3.txt", "a") as file:
    file.write("bonjour")
    file.write("\nbrahim")
    file.close()
