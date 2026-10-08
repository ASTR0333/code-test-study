def is_bored(S):
    sentences = [s.strip() for s in re.split(r'[.?!]', S) if s]
    boredom_count = sum(1 for sentence in sentences if sentence.startswith('I '))
    return boredom_count

import re