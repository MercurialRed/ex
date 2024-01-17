def analyze_commands(commands):
    words = ' '.join(commands).split()

    word_counts = dict.fromkeys(set(words))
    word_counts.update(map(lambda x: (x, words.count(x)), word_counts))
    
    most_used = max(word_counts, key=word_counts.get)
    least_used = min(word_counts, key=word_counts.get)
    
    return most_used, word_counts[most_used], least_used, word_counts[least_used]

commands_list = ['new game', 'new new game', 'load game', 'save game', 'setting', 'save setting', 'quit setting', 'quit game']
result = analyze_commands(commands_list)
print(result)