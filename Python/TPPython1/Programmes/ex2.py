#!/usr/bin/python3
# coding: utf-8

from random import seed
from random import randint

class Classe():
    def __init__(self):
        self.eleves = []

    def addEleve(self, humain):
        if isinstance(humain, Humain):
            self.eleves.append(humain)

    def avg(self, subject):
        avg = 0
        elvCount = 0
        for eleve in self.eleves:
            if subject in eleve.notes.Dict:
                avg += eleve.notes.Dict.get(subject)
                elvCount += 1
        return avg / elvCount

    def minGrade(self, subject):
        val = None
        for eleve in self.eleves:
            if subject in eleve.notes.Dict:
                if val is None:
                    val = eleve.notes.Dict.get(subject)
                else:
                    if eleve.notes.Dict.get(subject) < val:
                        val = eleve.notes.Dict.get(subject)
        return val

    def maxGrade(self, subject):
        val = None
        for eleve in self.eleves:
            if subject in eleve.notes.Dict:
                if val is None:
                    val = eleve.notes.Dict.get(subject)
                else:
                    if eleve.notes.Dict.get(subject) > val:
                        val = eleve.notes.Dict.get(subject)
        return val

class Humain():
    def __init__(self, nom, age = None, notes = None):
        self.nom = nom
        self.age = age
        self.notes = notes

    def setNom(self, nom):
        self.nom = nom

    def setAge(self, age):
        self.age = age

    def setNotes(self, notes):
        if isinstance(notes, Bulletin):
            self.notes = notes

class Bulletin():
    def __init__(self):
        self.Dict = {}

    def addGrade(self, nom, note):
        self.Dict[nom] = note

def main():

    seed(3456789)

    matieres = ["maths", "français", "histoire", "EPS", "JAVA"]
    classe = Classe()
    tab = []
    for a in range(0, 10):
        bulletin = Bulletin()
        for matiere in matieres:
            bulletin.addGrade(matiere, randint(0, 20))
        classe.addEleve(Humain("roger" + str(a), 10 + a * 2, bulletin))

    for matiere in matieres:
        print("______________" + matiere + "______________")
        avg = classe.avg(matiere)
        print("avg en " + matiere + " : " + str(avg))
        max = classe.maxGrade(matiere)
        print("max en " + matiere + " : " + str(max))
        min = classe.minGrade(matiere)
        print("min en " + matiere + " : " + str(min))


if __name__ == '__main__':
    main()