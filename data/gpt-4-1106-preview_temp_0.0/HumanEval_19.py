def sort_numbers(numbers: str) -> str:
    word_to_num = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    num_to_word = {v: k for k, v in word_to_num.items()}
    number_list = numbers.split()
    sorted_numbers = sorted(number_list, key=lambda word: word_to_num[word])
    sorted_numbers_str = ' '.join(num_to_word[num] for num in sorted_numbers)
    return sorted_numbers_str
