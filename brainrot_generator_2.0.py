import random

nouns = [
    "skibidi toilet",
    "ohio",
    "rizzler",
    "alpha",
    "Livy Dunne",
    "Baby Gronk",
    "Kai Cenat",
    "Adin Ross",
    "beta",
    "fanum",
    "sigma",
]

adjectives = [
    "sigma",
    "skibidi",    
    "alpha",
    "beta"
]

verbs = [
    "mog",
    "fanum tax",
    "rizz",
    "mew",
    "edge"
]

num_times = int(input("Brainrot level?: "))

def capitalize_sentence(sentence):
    return sentence[0].upper() + sentence[1:]

def generate_sentence():
    adjective1 = random.choice(adjectives)
    adjective2 = random.choice(adjectives)
    noun1 = random.choice(nouns)
    noun2 = random.choice(nouns)
    verb = random.choice(verbs)
    verb2 = random.choice(verbs)
    punctuation = random.choice([".", "!", "?"])

    rand_num = random.random()
    if rand_num < 0.2:
        sentence = f"The {adjective1} {noun1} {verb}s the {adjective2} {noun2}{punctuation}"
    elif rand_num < 0.3:
        sentence = f"The {adjective1} {noun1} truly has the most aura{punctuation}"
    elif rand_num < 0.4:
        sentence = f"{noun1} {verb}s the {adjective2} {noun2} while {verb2}ing{punctuation}"
    elif rand_num < 0.5:
        sentence = f"{noun1} the {adjective1} truly has the most aura{punctuation}"
    elif rand_num < 0.7:
        sentence = f"{noun1} is {adjective1} and {verb}s {noun2}{punctuation}"
    elif rand_num < 0.8:
        sentence = f"The {adjective1} {noun1} and the {adjective2} {noun2} both {verb}{punctuation}"
    elif rand_num < 0.9:
        sentence = f"{noun1} can't stop {verb}ing {noun2}{punctuation}"
    else:
        sentence = f"When the {adjective1} {noun1} {verb}s, the {adjective2} {noun2} {verb2}s{punctuation}"

    return capitalize_sentence(sentence)


for _ in range(num_times):
    sentence = generate_sentence()
    print(sentence)
