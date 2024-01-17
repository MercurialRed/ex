def analyze_commands(commands):
    word = ' '.join(commands).split()
    counted_word = dict.fromkeys(set(word))
    #counted_word.update(map(lambda x: (x, word.count(x)), counted_word))
    counted_word.update({x: word.count(x) for x in counted_word})
    '''for x in counted_word:
        counted_word.update({x: word.count(x)})'''

    most_used = max(counted_word, key=counted_word.get)
    least_used = min(counted_word, key=counted_word.get)
    return most_used, counted_word[most_used], least_used, counted_word[least_used]


commands_list = ['new game', 'new new game', 'load game', 'save game', 'setting', 'save setting', 'quit setting', 'quit game']
result = analyze_commands(commands_list)
print(result)