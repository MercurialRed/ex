# 1 


def show_most_and_least_used_item(data):
    counted_words = {}
    for element in data:
        for word in element.split():
            if word not in counted_words:
                counted_words[word] = 1
            else:
                counted_words[word] += 1

    most_used = max(counted_words, key=counted_words.get)
    least_used = min(counted_words, key=counted_words.get)

    return most_used, counted_words[most_used], least_used, counted_words[least_used]
    


input_line = ['new game', 'new new game', 'load game', 'save game', 'settings',
              'save settings', 'quit game', 'quit setting', 'quit']
result = show_most_and_least_used_item(input_line)
print(result)