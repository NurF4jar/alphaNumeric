# Sort alphaNumeric list Test


# function main
def main():
    alphaNumeric = [12, 9, 30, "A", "M", 99, 82, "J", "N", "B"]

    # output
    print(sort(alphaNumeric))


# sorting function
def sort(alphaNumeric):
    # convert data list to string
    new = [str(i) for i in alphaNumeric]
    new.sort()

    # convert sub data to integer
    new = [int(i) if i.isdigit() else i for i in new]

    # return value new
    return new


main()
