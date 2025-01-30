# 2 Öva på funktioner och moduler

Samla ihop dina funktioner så att de ligger i en eller flera moduler. Importera och anropa dem från main.py, så att main-filen bara innehåller funktionsanrop.

***

1 Skriv en funktion som tar en sträng som parameter. När den anropas ska den skriva ut strängen och "är en fena på programmering". Exempel:\
my_function("David") → "David är en riktig hacker"

***

2a Skriv en funktion med namnet "eko". När den anropas med en sträng ska den upprepa strängen, och skriva ut resultatet. Exempel:\
eko("hej") → skriver ut "hejhej"

2b Lägg till en parameter "count", som avgör hur många ekon som ska skapas. Exempel:\
eko("hej", 3) → skriver ut "hejhejhej"
 
***

3 Följande kod ska sluta loopa efter 5 varv. Flytta den in i en funktion och justera den enligt kommentaren.\
end = 5\
y = 1\
for x in range(1, 100):\
&nbsp;&nbsp;&nbsp;&nbsp;y *= 2\
&nbsp;&nbsp;&nbsp;&nbsp;# avsluta loopen med en if-sats här\
print(y)

***

4 Skriv en funktion med namnet last. Den ska ta en lista som parameter och returnera det sista elementet i listan.\
last([1, 2, 3]) → 3

***

5 Skriv en funktion med namnet cut_edges. Den ska ta en lista som parameter. När den anropas ska den returnera en ny lista, där den har tagit bort första och sista elementet.\
cut_edges([1, 2, 3, 4]) → [2, 3]

***

6 Lös felen i koden.\
def increase(x):\
&nbsp;&nbsp;&nbsp;&nbsp;return x\
&nbsp;&nbsp;&nbsp;&nbsp;x += 1

print(increase(1))

***

7 Bygg en funktion med namnet average. Den ska ta parametrar: x och y. Båda ska vara tal.\
Funktionen ska returnera medelvärdet. Till exempel så räknar man ut medelvärdet av 4 och 8 genom med formeln: (4 + 8) / 2, vilket blir 6.\
Tips: det kan vara enklare att använda fler variabler.

***

8 Gör en funktion som kan skriva ut innehållet i en lista lite snyggare. Först ska funktionen tala om ifall listan är tom, eller hur många element den har. Sedan ska funktionen skriva ut elementen i en punktlista. Exempel:\
pretty_print(["a", "b", 3.14])\
Listan har 3 element:\
1. a
2. b
3. 3.14

***

## Student == Jan Berglund

### Programmering med Python, 20yhp
