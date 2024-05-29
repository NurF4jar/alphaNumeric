# main function
def pattern_count():
    # Input word & combination
    word = str(input("Input the Word! "))
    combi = str(input("Input the combination! "))

    # call & print countCombination function
    print(countCombination(word, combi))


# function to count all combination from the word
def countCombination(word, combi):
    count = word.count(combi)
    return count


pattern_count()
