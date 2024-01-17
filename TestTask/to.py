import re
'''1. Є два масива. Потрібно знайти елементи які присутні в першому, але відсутні в другому
2. Порахувати скільки разів слово зустрічається в певному тексті. Надати відсортований словник,
де ключ - слово, а значення - кількість його вживань. Позбутись позділових знаків'''

# 1
'''x = [1, 2, 3, 5, 7, "head", 'arm', 'leg']
y = [1, 3, 4, 'leg', 11, 'finger']
z = [i for i in x if i not in y]
#z = set(x).difference(set(y))
print(z)'''

# 2
example = "I won't run away, I won't let you down. Hold me! Take me with you, far from this world, we'll be one with our hope, one with our fate. Pure life unfolds!"
word = [i for i in example.lower() if re.findall("[a-z\s]", i)]
word = ''. join(word).split()

amount = dict.fromkeys(set(word))
amount.update(map(lambda x: (x, word.count(x)), amount))
#print(word)
s = dict(sorted(amount.items(), key=lambda item: item[1]))
print(s)


'''special_chars = set()
#special_chars.add(char for char in example if not char.isalnum() and not char.isspace())
for char in example:
    if not char.isalnum() and not char.isspace():
        special_chars.add(char)

words = ''.join(char for char in example.lower() if char not in special_chars).split()
amount = dict.fromkeys(set(words))
amount.update(map(lambda x: (x, words.count(x)), amount))
sorted_dict = dict(sorted(amount.items(), key=lambda item: item[1]))
print(sorted_dict)'''