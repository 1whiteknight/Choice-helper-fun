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
