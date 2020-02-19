def palindrome2(word):

    reverse_word = word[::-1]
    if reverse_word == word:
        return True

    return False


def palindrome(word):
    reverse_letter = []

    for letter in word:
        reverse_letter.insert(0, letter)

    reverse_word = ''.join(reverse_letter)
    print(reverse_word)
    if reverse_word == word:
        return True

    return False


if __name__ == "__main__":
    word = str(input('Escribe una palabra: '))
    result = palindrome2(word)

    if result is True:
        print('{} si es un palindromo'.format(word))
    else:
        print('{} no es un palindromo'.format(word))
