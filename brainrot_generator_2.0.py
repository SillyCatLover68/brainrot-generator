import random

nouns = [
    "skibidi toilet",
    "ohio",
    "rizzler",
    "Livy Dunne",
    "Baby Gronk",
    "Kai Cenat",
    "Adin Ross",
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
    "edge",
    "goon"
]

num_times = int(input("Brainrot level?: "))


def capitalize_sentence(sentence):
    return sentence[0].upper() + sentence[1:]


def generate_sentence():
    unique_nouns = random.sample(nouns, 2)
    unique_adjectives = random.sample(adjectives, 2)
    unique_verbs = random.sample(verbs, 2)
    punctuation = random.choice([".", "!", "?"])

    rand_num = random.random()
    if rand_num < 0.2:
        sentence = f"The {unique_adjectives[0]} {unique_nouns[0]} {unique_verbs[0]}s the {unique_adjectives[1]} {unique_nouns[1]}{punctuation}"
        
    elif rand_num < 0.3:
        sentence = f"The {unique_adjectives[0]} {unique_nouns[0]} truly has the most aura{punctuation}"
        
    elif rand_num < 0.4:
        sentence = f"{unique_nouns[0]} {unique_verbs[0]}s the {unique_adjectives[1]} {unique_nouns[1]} while {unique_verbs[1]}ing{punctuation}"
        
    elif rand_num < 0.5:
        sentence = f"{unique_nouns[0]} the {unique_adjectives[0]} truly has the most aura{punctuation}"
        
    elif rand_num < 0.7:
        sentence = f"{unique_nouns[0]} is {unique_adjectives[0]} and {unique_verbs[0]}s {unique_nouns[1]}{punctuation}"
        
    elif rand_num < 0.8:
        sentence = f"The {unique_adjectives[0]} {unique_nouns[0]} and the {unique_adjectives[1]} {unique_nouns[1]} both {unique_verbs[0]}{punctuation}"
        
    elif rand_num < 0.9:
        sentence = f"{unique_nouns[0]} can't stop {unique_verbs[0]}ing {unique_nouns[1]}{punctuation}"
        
    else:
        sentence = f"When the {unique_adjectives[0]} {unique_nouns[0]} {unique_verbs[0]}s, the {unique_adjectives[1]} {unique_nouns[1]} {unique_verbs[1]}s{punctuation}"

    return capitalize_sentence(sentence)


for _ in range(num_times):
    sentence = generate_sentence()
    print(sentence)
