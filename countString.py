# Library python
from collections import OrderedDict


def main():
    text = str(input("Input Your's text here ! "))
    textFreq = countFreq(text)

    # sort dict  value
    sortFreq = OrderedDict(sorted(textFreq.items()))
    print(sortFreq)


def countFreq(n):
    freq = {}
    for i in set(n):
        freq[i] = n.count(i)
    return freq


main()
