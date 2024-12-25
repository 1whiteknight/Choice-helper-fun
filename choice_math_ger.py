# Eingabetext generieren.
text = input("Trage deine Entscheidungsfrage ein.")

# Namen eingeben
name = input("Bitte gib deinen Namen ein. ")

# text/Frage ausgeben
print(text)
# Suche dir eine Zahl zwischen 1-9 aus,
print("Denke dir eine Zahl zwischen 1-9 aus! ")
# multipliziert mit 3,
print("Multipliziere die Zahl mit 3")
# dann 3 dazuzählen,
print("Addiere/Zähle 3 dazu")
# dann nochmals mit 3 multiplizieren und
print("Multipliziere das Ergebnis mit 3")
# zum Schluss die beiden Ziffern der Zahl zusammenzählen
print("Zähle die Zahlen zusammen und drücke Enter.")

list = ["1. Andreas", "2. Bart", "3. Kirsten", "4. Daniel", "5. Felix", "6. Jutta", "7. Ingrid", "8. Kain"]
# Verbindung der Listenelemente mit einem Zeilenumbruch
print("\n".join(list))
print("9. " + name)
list2 = ["10. Martin", "11. Viktor", "12. Klara", "13. Cleopatra"]
# Verbindung der Listenelemente mit einem Zeilenumbruch
print("\n".join(list2))
