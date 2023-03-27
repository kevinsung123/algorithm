def main():
    # Dictionary of strings and ints
    wordsFreqDict = {
        "hello": 56,
        "at": 23,
        "test": 43,
        "teaa": 46,
        "this": 43
    }

    '''
    sort dictionary elements by key
    '''
    print("**** Sort Dictionary by Key *******")

    '''
     Iterate over a sorted list of keys and select value from dictionary for each key
     and print the key value pairs in sorted order of keys
    '''
    print(wordsFreqDict.keys())
    for key in sorted(wordsFreqDict.keys()):
        print(key, " :: ", wordsFreqDict[key])

    print("***************")

    '''
     Iterate over a  list of tuple i.e. key / value pairs, sorted by default 0th index i.e. key
     and print the key value pairs in sorted order of keys
    '''
    print(wordsFreqDict.items())
    for elem in sorted(wordsFreqDict.items()):
        print(elem[0], " ::", elem[1])

    print("***************")

    # Print the sorted key value pairs of dictionary using list comprehension
    [print(key, " :: ", value) for (key, value) in sorted(wordsFreqDict.items())]

    print("***************")

    print("Sort dictionary contents by value in reverse Order")

    '''
    Iterate over the list of tuples sorted by 0th index i.e. value in reverse order 
    '''
    for elem in sorted(wordsFreqDict.items(), reverse=True):
        print(elem[0], " ::", elem[1])

    print("***************")

    print("Sort by Key using Custom Comparator : Sort by length of key string")
    listofTuples = sorted(wordsFreqDict.items(), key=lambda x: len(x[0]))

    for elem in listofTuples:
        print(elem[0], " ::", elem[1])

    '''
    Sort dictionary elements by value
    '''

    print("**** SORT BY VALUE *******")

    # Create a list of tuples sorted by index 1 i.e. value field
    listofTuples = sorted(wordsFreqDict.items(), key=lambda x: x[1])

    # Iterate over the sorted sequence
    for elem in listofTuples:
        print(elem[0], " ::", elem[1])

    print("*************************")

    # Use List comprehension to print the contents of dictionary , sorted by value
    [print(key, " :: ", value) for (key, value) in sorted(wordsFreqDict.items(), key=lambda x: x[1])]

    print("**** SORT BY VALUE In Reverse Order *******")

    # Create a list of tuples sorted by index 1 i.e. value field
    listofTuples = sorted(wordsFreqDict.items(), reverse=True, key=lambda x: x[1])

    # Iterate over the sorted sequence
    for elem in listofTuples:
        print(elem[0], " ::", elem[1])


if __name__ == '__main__':
    main()
