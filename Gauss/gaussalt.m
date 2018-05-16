function [ x ] = gaussalt(A, b)

    % Falsche Eingaben abfangen
    if size(A,1) ~= size(A,2)
       error('A ist nicht quadratisch'); 
    end
    if rank(A) ~= size(A,1)
       error('A ist nicht regulär'); 
    end
    if size(b,1) ~= size(A,1) || size(b,2) ~= 1 
        error('A is n x n Matrix, dann muss B die Dimension n x 1 besitzen!');
    end
    
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
    
    % Übergebe A2 und b2 der bereits geschriebenen Funktion
    % rueckwaertseinsetzen (A2 ist die obere Dreiecksmatrix)
    A2 = X(:, 1:n(2)-1);
    b2 = X(:, n(2));
    
    x = rueckwaertseinsetzen(A2, b2);
    
end