import nltk
from itertools import permutations
from collections import OrderedDict

english_vocab = set(w for w in nltk.corpus.words.words())

while(True):
    x = input("Enter your letters or enter q to quit: ")
    if(x=='q'):
        break

    words = []

    j = 0
    for i in range(len(x)+1, 3, -1):
        for p in permutations(x, len(x)-j):
            str = ''.join(p)
            if(str in english_vocab):
                words.append(str)
        j+=1

    output = list(OrderedDict.fromkeys(words))

    print('output:')
    for word in output:
        print(word)
