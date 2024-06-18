import random


strings = [
    "skibidi",
    "rizz",
    "rizzler",
    "fanum tax",
    "gyat",
    "Kai Cenat",
    "Duke Dennis",
    "Baby Gronk",
    "Livy Dunne",
    "rizzes",
    "rizzed",
    "fanum taxed",
    "mogs",
    "mogged",
    "mog",
    "beta",
    "alpha",
    "ohio",
    "only in ohio",
    "edge",
    "goon",
    "is"
]

num_times = int(input("Brainrot level?: "))


def capitalize_sentences(text):
    sentences = text.split('. ')
    new_sentences = []
    for sentence in sentences:
        if sentence:
            sentence = sentence[0].upper() + sentence[1:]
        new_sentences.append(sentence)
    return '. '.join(new_sentences)


for _ in range(num_times):
    random.shuffle(strings)

    sentence = ""
    for i, string in enumerate(strings):
        sentence += string
        if i < len(strings) - 1:
            if random.random() < 0.1:
                sentence += random.choice([". ", "! ", "? "])
            else:
                sentence += " "

    if not sentence.endswith((". ", "! ", "? ")):
        sentence += random.choice([".", "!", "?"])

    sentence = capitalize_sentences(sentence)

    print(sentence)
