def count_croatian_letters(word):
    croatian_letters = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]
    for letter in croatian_letters:
        word = word.replace(letter, "*")  
    return len(word)


word = input().strip()
print(count_croatian_letters(word))
