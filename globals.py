

# Chess "File"
cols = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

# Chess "Rank"
rows = {1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1, 8: 0}

# Chess columns
files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


def make_color_text(black):
    if black is 1:
        return 'xxxxx'
    return 'ooooo'
