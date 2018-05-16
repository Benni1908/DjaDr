import numpy as np

# A = np.array([[1, 2], [3, 4]])
# A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 10]])
# A = np.array([[5., 6.], [-6., -11.]])
A = np.array([[2., 2., 3.], [4., 5., 6.], [7., 8., 10.]])
# A = np.array([[2., 2., 3.], [4., 8., 6.], [7., 8., 10.]])

# b = np.array([[5], [6]])
# b = np.array([[10], [11], [13]])
# b = np.array([[11.], [-57.]])
b = np.array([[10.], [11.], [13.]])
# b = np.array([[10.], [11.], [13.]])


# A und b in eine Matrix überführen
X = np.append(A, b, axis=1)

# Lösungsvektor definieren
y = np.zeros((A.shape[1], 1))
print(X, '\n')

## Diagonalmatrix erzeugen
# Durchlaufen der Spalten
for j in range(A.shape[1]):
    # Durchlaufen der Zeilen
    for i in range(j + 1, A.shape[0]):
        # Prüfen ob der zu eliminierende Koeffizient schon 0 ist
        if X[i, j] != 0:
            # Prüfen ob Diagonalelement 0 ist
            if X[j, j] != 0:
                # Wenn Diagonalelement ungleich 0: Subtraktion zweier Zeilen, sodass der zu eliminierende Koeffizient verschwindet
                X[i] = X[i] - X[j] * X[i, j] / X[j, j]
                print(X, '\n')
            else:
                # Wenn Diagonalelement 0 ist: Zeilentausch
                Xspeicher = X[j]
                X[j] = X[j + 1]
                X[j + 1] = Xspeicher
                A[[j, j + 1], :] = A[[j + 1, j], :]

                print(X, '\n')

print('Die Diagonalmatrix lautet:\n', X)

## Rückwärtseinsetzen
# rechte Seite des zu lösenden Gleichungssystems
bneu = X[:, -1]
# Vektor, der ensteht wenn man alle bekannten Lösungen des Lösungsvektors ins Gleichungssystem einsetzt
bab = np.zeros((A.shape[1], 1))
# Durchlaufen der Zeilen
for i in range(A.shape[0] - 1, -1, -1):
    # Durchlaufen der Spalten
    for j in range(A.shape[1] - 1, i, -1):
        # Lösungen ins Gleichungssystem einsetzen
        bab[i] = bab[i] + y[j] * X[i, j]
    # Gleichung nach Lösungsvariable umstellen
    y[i] = (bneu[i] - bab[i]) / X[i, i]
print('Der Lösungsvektor lautet:\n', y)

print('\n', np.linalg.solve(A, b))  # Überprüfen
