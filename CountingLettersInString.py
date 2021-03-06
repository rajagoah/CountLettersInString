def test_dict():
    sr = {'name':'AR', 'age':28, 'height': 6}

    #displaying the keys in this dictionary
    print(sr.keys())

    #priting the values in this dictionary
    print(sr.values())

    #printing both the keys and values in the dictionary, in the form of tuples
    print(sr.items())

    #iterating through the dictionary using for loop
    print("using for loop to output keys in the dictionary")
    for k in sr.keys():
        print(k)

    print("using for loop to output values in the dictionary")
    for k in sr.values():
        print(k)

    print("using for loop to output keys and value pairs in the dictionary")
    for k in sr.items():
        print(k)

    #handling the keyError exception with an accurate error message:
    try:
        print(sr['weight'])
    except KeyError:
        print('the key doesnt exist')

    #using the get() method to determine if a key exists or not. It takes 2 arguments: the key and the default value if the key doesnt exist
    #Using this method, the try execpt block will never be executed
    try:
        print(sr.get('weight','No such key'))
    except KeyError:
        print('The key doesnt exist')

    #adding a key to the dictionary if it doesnt exist
    try:
        if 'weight' not in sr:
            sr['weight'] = 75
        print("Checking if the newly added key exists in the dictionary")
        print(sr.keys())
    except KeyError:
        print('The key doesnt exist')

    #adding a key using the setdefault() method instead of using the if else condition
    try:
        sr.setdefault('hair color','black')
        print("Checking if the newly added key exists in the dictionary")
        print(sr.keys())
    except KeyError:
        print('The key doesnt exist')

def CountingLetters(test_str):
    print("**************** Entering the Counting Letters function ****************\n")
    #now using all the above operators to count the occurence of letters in string
    #accepting input from user
    str = test_str
    try:
        #initializing a dictionary to store the key value pair
        test_str_dict = {}

        for character in str.lower():
            test_str_dict.setdefault(character,0)
            test_str_dict[character] = test_str_dict[character] + 1
        return test_str_dict
    except KeyError:
        print('The key doesnt exist')


if __name__=="__main__":
    while True:
        test_str = input("****************please enter the string you want the character occurrences counted****************\n")
        print("****************Sending the text to the CountingLetter function****************\n")
        test_str_dict = CountingLetters(test_str)
        print(test_str_dict)
        response = input("**************** Do you want to continue ?? Y/N ****************\n")

        if response.lower() == 'y' or response.lower() == 'yes':
            continue
        else:
            break





