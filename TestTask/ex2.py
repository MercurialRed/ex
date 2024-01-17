# Task 2.
# input line: ['new game', 'new new game', 'load game', 'save game', 'setting', 'quit', 'quit setting', 'quit game']
# output line: [game: 5]
#              [load: 1]

def count_min_max(data):
    a = {}
    b=[]
    for element in data:
        for word in element.split():
            b.append(word)
            c = b.count(word)
    print(c)

input_line = ['new game', 'new new game', 'load game', 'save game', 'setting', 'quit', 'quit setting', 'quit game']
result = count_min_max(input_line)
print(result)



'''def find_most_least_common_words(input_list):
    all_words = ' '.join(input_list).split()
    print(all_words)
    word_counts = {word: all_words.count(word) for word in set(all_words)}
    print(word_counts)
    most_common_word = max(word_counts, key=word_counts.get)
    least_common_word = min(word_counts, key=word_counts.get)

    return most_common_word, least_common_word

# Example usage:
your_list = ['new game', 'new new game', 'load game', 'save game', 'save setting', 'quit', 'quit setting', 'quit game']
most_common, least_common = find_most_least_common_words(your_list)

print(f"Most common word: {most_common}")
print(f"Least common word: {least_common}")


def count_min_max(data):
    data

    print(data)

input_line = ['new game', 'new new game', 'load game', 'save game', 'setting', 'quit', 'quit setting', 'quit game']
count_min_max(input_line)'''

