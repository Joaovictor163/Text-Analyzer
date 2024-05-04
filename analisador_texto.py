from collections import Counter
import string

def analyze_text(text):
    """
    Analyzes the provided text and calculates word count, word frequency,
    and letter frequency.
    :param text: text to be analyzed
    :return: tuple: word count, word frequency, and letter frequency
    """
    treatment = str.maketrans('', '', string.punctuation)
    treated_text = text.translate(treatment)
    treated_text = treated_text.lower()
    words = treated_text.split()
    word_count = Counter(words)
    length = len(words)
    letter_count = Counter(treated_text)

    return word_count, length, letter_count


word_count, length, letter_count = analyze_text('Hello world!, this is a test. Hello again')
print(f'word count: {word_count}')
print(f'number of words: {length}')
print(f'number of letters: {letter_count}')

