# coding: utf-8
import PyYAML  as yl

with open("config.yml", 'r') as stream:
    try:
        # Chargement du fichiers
        config = yl.load(stream)

        # Récupération des personnes
        persons = config["persons"]

        # Lecture des personnes une à une
        for person in config["persons"]:
            print(person["name"])
            print(person["firstName"])
            print(person["hero"])
            print("==========")

    except yl.YAMLError as ex:
        print("YAML FILE HAS SYNTAX ERROR :")
        print(ex)