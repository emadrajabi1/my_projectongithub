def analyze_text() -> None:
    """
    Analyze a sentence and compute basic text statistics.
    """
    sentence: str = input('Enter a sentence: ').strip()

    char_count: int = len(sentence)
    word_count: int = len(sentence.split())

    vowels: set[str] = {'a', 'e', 'i', 'o', 'u'}
    vowel_count: int = sum(1 for char in sentence.lower() if char in vowels)

    print('\nSentence:', sentence)
    print('-' * 30)
    print('Characters :', char_count)
    print('Words      :', word_count)
    print('Vowels     :', vowel_count)
    print('-' * 30)


if __name__ == "__main__":
    analyze_text()