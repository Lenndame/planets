"""
einfach

Schreibe ein Programm, welches über einen User-Input einen Planetennamen 
einliest und die Entfernung Erde - Planet in die Ausgabe
printed. 

Falls ein unbekannter Planet eingegeben wird, soll das Programm 
den User darauf hinweisen.

Hinweis:
nutze if-else, print
wir gehen von validem Input aus
es reichen zwei Beispielplaneten mit Dummywerten aus

Beispiel
----------
Bitte gebe einen Planennamen ein: Erde 
Der Abstand des Planeten Erde zu Erde ist 0 km

Bitte gebe einen Planennamen ein: Merkur 
Der Abstand des Planeten Merkur zu Erde ist 100.000.000 km

Bitte gebe einen Planennamen ein: Melmac 
dieser Planet ist leider nicht bekannt.

"""

#----------------------------------------------------------------------------

userinput = str(input("Die Distanz zu welchem planeten möchten sie wissen? "))

planets = ["erde", "sonne", "mars", "venus", "saturn", "uranus", "neptun", "pluto", "jupiter", "merkur", "mond"] 

# Großbuchstaben für Konstante wäre besser

distance_earth = "0km"
distance_sun = "Im Mittel beträgt die Distance 149.597.870 Millionen Km"
distance_mars = "min. 55,7 Millionen Km und max. 401,3 Millionen km"
distance_venus = "min. 38,2 Millionen Km und max. 261 Millionen km"
distance_saturn = "min. 1195,5 Millionen Km und max. 1658,5 Millionen km"
distance_uranus = "min. 2581,9 Millionen Km und max. 3157,3 Millionen km"
distance_neptune = "min. 4305,9 Millionen Km und max. 4687,3 Millionen km"
distance_jupiter = "min. 588,5 Millionen Km und max. 968,1 Millionen km"
distance_merkur = "min. 77,3 Millionen Km und max. 221,9 Millionen km"
distance_pluto = "min. 4284,7 Millionen Km und max. 7528 Millionen km"
distance_moon = "min. 0,36 Millionen Km und max. 0,41 Millionen km"

if userinput.lower in planets:
    if userinput == "Erde":
        print(distance_earth)
    elif userinput == "Sonne":
        print(distance_sun)
    elif userinput == "Mars":
        print(distance_mars)
    elif userinput == "Venus":
        print(distance_venus)
    elif userinput == "Saturn":
        print(distance_saturn)
    elif userinput == "Uranus":
        print(distance_uranus)
    elif userinput == "Neptun":
        print(distance_neptune)
    elif userinput == "Pluto":
        print(distance_pluto)
    elif userinput == "Jupiter":
        print(distance_jupiter)
    elif userinput == "Merkur":
        print(distance_merkur)
    elif userinput == "Mond":
        print(distance_moon)
else:
    print("Dieser Planet ist leider nicht bekannt")
    