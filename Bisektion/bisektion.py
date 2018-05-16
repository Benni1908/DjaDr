import numpy as np

c = 1e-10
# a = -10  # Zu aendern
# b = 10  # Zu aendern
a = input("Geben Sie die untere Grenze an: ")
a = int(a)
b = input("Geben Sie die obere Grenze an: ")
b = int(b)

def f(x):
    erg = x - 5
    return erg

# Überpruefen, ob die Funktionswerte an den beiden Grenzen
# unterschiedliche Vorzeichen haben

if f(b) * f(a) < 0:
    while abs(b - a) > c:
        # Durchlaufen der Schleife, solange die Differenz zwischen
        # b und a kleiner ist als die Genauigkeit c

        while (abs(b - a) > c):
            # Überprüfen, ob die Funktionswerte an der unteren Grenze
            # a und in der Mitte von a und b die gleiche Vorzeichen haben

            if f((a + b) / 2) * f(a) > 0:
                # Wähle die Mitte als neue untere Grenze
                a = (a + b) / 2
            else:
                # Sonst wähle die Mitte als neue obere Grenze
                b = (a + b) / 2

# Nullstelle ist der Mittelwert der beiden Grenzen
nst = (a + b) / 2

print(nst)
