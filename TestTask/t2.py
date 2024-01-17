# input ['new game', 'new new game', 'load game', 'save game', 'setting', 'save setting', 'quit setting', 'quit game']
# output ['Most: game: 4']
#        ['Least: 'load: 1']


def count_times_present(test_array):

    counted_words = {}
    for element in test_array:
        for word in element.split():
            if word in counted_words:
                counted_words[word] += 1
            else:
                counted_words[word] = 1
    
    most_used = max(counted_words, key=counted_words.get)
    least_used = min(counted_words, key=counted_words.get)
    
    return most_used, counted_words[most_used], least_used, counted_words[least_used]

input_list = ['new game', 'new new game', 'load game', 'save game', 'setting', 'save setting', 'quit setting', 'quit game']
result = count_times_present(input_list)
print(result)