" https://github.com/peturf/TileTraveller "

"""
Taka punkt sem byrjar á hnitum x, y = 1 og færa hann í gegnum völundarhús. Hann verður að vera innan 1 < x, y < 3.
Eftirfarandi hreyfingar eru ekki leyfðar (veggir):
1,1 -> má bara fara norður
2,2 -> má bara fara suður eða vestur
2,1 -> má bara fara norður
2,3 -> má bara fara vestur eða austur
3,2 -> má bara fara norður eða suður
"""

#Breytur fyrir hreyfingu leikmannsins í völundarhúsinu
x = 1
y = 1
#Strengur fyrir innslátt áttar sem ferðast á í
str_movement = ""

#while lykkja sem keyrir þangað til að x = 3 og y = 1

while x != 3 and y != 1:
    if x == 1 and y == 1:
        print("You can travel: (N)orth")
        str_movement = input("Direction: ")
        str_movement = str_movement.lower()
        while str_movement != "n":
            print("Not a valid direction!")
            str_movement = input("Direction: ")
            str_movement = str_movement.lower()
        y += 1

