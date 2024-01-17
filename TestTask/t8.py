def analyze_commands(data):
    word = ' '.join(data).split()
    amount = dict.fromkeys(set(word))
    amount.update(map(lambda x: (x, word.count(x)), amount))

    most_used = max(amount, key=amount.get)
    least_used = min(amount, key=amount.get)
    return most_used, amount[most_used], least_used, amount[least_used]


commands_list = ['new game', 'new new game', 'load game', 'save game', 'setting', 'save setting', 'quit setting', 'quit game']
result = analyze_commands(commands_list)
print(result)