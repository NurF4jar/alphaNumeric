# Library python
from collections import OrderedDict


# function main
def main():
    # Input
    text = str(input("Input Your's text here ! "))

    # call the sort function
    textFreq = countFreq(text)

    # sort dict  value
    sortFreq = OrderedDict(sorted(textFreq.items()))
    print(sortFreq)


# sorting function
def countFreq(n):
    freq = {}

    # loop to count the frequensi
    for i in set(n):
        freq[i] = n.count(i)
    return freq


main()
