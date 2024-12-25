print("Chose 1 for English or 2 for German. \n Wählen Sie 1 für Englisch oder 2 für Deutsch.")
language = input()
if language == "1":
    print("English")
    # Here is the code for the first program
    # Generate input text.
    text = input("Enter your decision question. ")

    # input name
    name = input("Please enter your name. ")

    # text/print question
    print(text)
    # Choose a number between 1-9,
    print("Think of a number between 1-9! ")
    # multiplied by 3,
    print("Multiply the number by 3")
    # then add 3,
    print("Add/count 3")
    # then multiply by 3 again and
    print("Multiply the result by 3")
    # Finally, add the two digits of the number together
    print("Add up the numbers and check the list. ")

    list = ["1. Andreas", "2. Bart", "3. Kirsten", "4. Daniel", "5. Felix", "6. Jutta", "7. Ingrid", "8. Kain"]
    # Connection of the list elements with a line break
    print("\n".join(list))
    print("9. " + name)
    list2 = ["10. Martin", "11. Viktor", "12. Klara", "13. Cleopatra"]
    # Connection of the list elements with a line break
    print("\n".join(list2))
elif language == "2":
    print("Deutsch")
    # Here is the code for the second program
    # Eingabetext generieren.
    text = input("Trage deine Entscheidungsfrage ein. ")

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
    print("Zähle die Zahlen zusammen und prüfe die Liste. ")

    list = ["1. Andreas", "2. Bart", "3. Kirsten", "4. Daniel", "5. Felix", "6. Jutta", "7. Ingrid", "8. Kain"]
    # Verbindung der Listenelemente mit einem Zeilenumbruch
    print("\n".join(list))
    print("9. " + name)
    list2 = ["10. Martin", "11. Viktor", "12. Klara", "13. Cleopatra"]
    # Verbindung der Listenelemente mit einem Zeilenumbruch
    print("\n".join(list2))
else:
    print("Wrong input! Please chose 1 or 2. \n Ungültige Eingabe! Bitte wählen Sie 1 oder 2.")
