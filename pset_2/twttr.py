def main():
    word = input("Input: ")
    new_word = vowel_remove(word)
    print(f"Output: {new_word}")
def vowel_remove(m):
    vowel = 'aeiou'
    result = ''.join([char for char in m if char not in vowel])
    return result

main()
