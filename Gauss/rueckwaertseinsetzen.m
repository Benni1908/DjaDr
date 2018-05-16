function [x] = rueckwaertseinsetzen(A, b)

    n = length(A);
    x = zeros(n, 1);
    
    %{
    Die For-Schleife läuft von n (= Länge der Matrix A) abwärts bis 1
    
    (1) If-Bedingung
        Ist i kleiner als n, wird jeder Eintrag der Matrix A, der sich in 
        der Zeile i rechts von dem Feld A(i,i) befinden
            A(i,i+1) , ... , A (i,n)
        mit dem entsprechenden Eintrag des Vektors x multipliziert. D.h.
        der Eintrag in der k-ten Spalte wird mit dem k-ten Eintrag des
        Vektors x multipliziert:
            A(i,i+1) * x(i+1)
            ...
            A(i,n) * x(n)
        Dies geschieht durch den Befehl: A(i, i+1: L) * x(i+1 : L, 1)
    
        Die Summe von dem Ganzem
            A(i,i+1) * x(i+1) + ... + A(i,n) * x(n)
        wird von dem Eintrag b(i) abgezogen. Das Ergebnis dieser
        Subtraktion wird in b(i) selbst gespeichert.
    
    (2) x(i)
        Der Eintrag x(i) lässt sich durch die Divison von b(i) und dem Feld
        A(i,i) berechnen.

    %}
    
    for i = n: -1 : 1
        
        if i < n
           b(i) = b(i) - sum( A(i, i+1: n) * x(i+1 : n, 1) ); 
        end
        
        x(i) = b(i) / A(i, i);

    end    
end