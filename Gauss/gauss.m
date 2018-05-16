function [ x ] = gauss(A, b)

    X = [A b];
    n = size(X);
    
    % Durchlaufe Phasen von Gauss, um eine obere Dreiecksmatrix zu erhalten
    for i = 1:n(1)-1
        
        % Zeilen unterhalb des Pivot-Elements durchlaufen
        for j = i+1:n(1)
 
            % Überprüfen, ob X(j,i) nicht schon Null ist
            if(X(j,i) ~= 0)
                
                % Prüfen, ob Pivot-Element gleich Null ist
                if(X(i,i) == 0)

                    % Durchlaufe die Einträge unterhalb des Pivot-Elements
                    for k = i+1:n(1)

                        % Ist das Eintrag ungleich Null ...
                        if( X(k,i) ~= 0 )
                            % ... tausche die beiden
                            tempZeile = X(i,:);
                            X(i,:) = X(k,:);
                            X(k,:) = tempZeile;
                           break;
                        end
                    end
                end
            
                X(j,:) = X(j,:) - X(j,i) / X(i,i) * X(i,:);
            end
        end
    end
    
    % Übergebe A2 und b2 Funktion rueckwaertseinsetzen (A2 ist die obere Dreiecksmatrix)
     
    A2 = X(:, 1:n(2)-1);
    b2 = X(:, n(2));
    
    x = rueckwaertseinsetzen(A2, b2);
    
end


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