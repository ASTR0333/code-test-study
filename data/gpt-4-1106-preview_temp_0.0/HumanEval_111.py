from collections import Counter

def histogram(test):
    if not test:
        return {}
    
    # Split the string into words and count the occurrences
    word_counts = Counter(test.split())
    
    # Find the maximum count
    max_count = max(word_counts.values())
    
    # Return a dictionary with only the letters with the maximum count
    return {letter: count for letter, count in word_counts.items() if count == max_count}
