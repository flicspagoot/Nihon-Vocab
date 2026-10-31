words = {
    "konnichiwa": "Hello",
    "Arigato": "Thank you",
    "mizu": "Water",
    "sakura": "Cherry Blossom",
    "gohan": "Rice",
}

for japanese, english in words.items():
    answer = input(f"What is the English word for '{japanese}'? ")
    if answer.strip().lower() == english.lower():
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is '{english}'.")