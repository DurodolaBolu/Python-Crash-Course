def extract_alph(string):
    alph=""
    for alphabet in string:
        if alphabet.isalpha():
            alph += alphabet
    return alph

name='my name is bolu and i was 30 years old 1990'
print(extract_alph(name))