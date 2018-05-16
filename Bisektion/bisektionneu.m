%% Lösche vorher alles
clear
close all
clc

%% Starte dein main

c = 1e-10;
a = -10; % Zu ändern
b =  10; % Zu ändern


%Überprüfen, ob die Funktionswerte an den beiden Grenzen ...
... unterschiedliche Vorzeichen haben

if(f(b)*f(a)<0)
    while(abs(b-a)>c)
        %Durchlaufen der Schleife, solange die Differenz zwischen ...
        ... b und a kleiner ist als die Genauigkeit c
            
        while(abs(b-a)>c)
            % Überprüfen, ob die Funktionswerte an der unteren Grenze ...
            ... a und in der Mitte von a und b die gleiche Vorzeichen haben
                
            if(f((a+b)/2)*f(a)>0)
                % Wähle die Mitte als neue untere Grenze
                a=(a+b)/2;
            else
                % Sonst wähle die Mitte als neue obere Grenze 
                b=(a+b)/2;
            end
        end
    end
end

%Nullstelle ist der Mittelwert der beiden Grenzen
nst=(a+b)/2;
    
function f_x=f(x)
  f_x=x-5;
end
