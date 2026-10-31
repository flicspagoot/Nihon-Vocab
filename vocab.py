import json

with open("Vocab.json", "r") as f:
    words = json.load(f)

for word in words:
    answer = input(f"What is the meaning of '{word['romaji']}' mean? ")
    if answer.strip().lower() == word['english'].lower():
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is '{word['english']}'.")