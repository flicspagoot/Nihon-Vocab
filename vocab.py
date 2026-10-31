import json

with open("Vocab.json", "r") as f:
    words = json.load(f)

level = input("Which N level?: ").strip().upper()
level_words = [word for word in words if word["level"] == level]
if not level_words:
    print(f"No words found for level {level}.")
else:
    for word in level_words:
        answer = input(f"What is the meaning of '{word['romaji']}' mean? ")
        if answer.strip().lower() == word['english'].lower():
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is '{word['english']}'.")