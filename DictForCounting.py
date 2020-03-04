while True:
    # take input from user
    text = input("enter the string you\n")

    # initializing a dictionary to store the character and count
    char = {}
    #starting the for loop
    for i in text.lower():

        #using set default value to assign a default value to key that doesnt exist.
        #without this, the KeyError will be thrown
        char.setdefault(i,0)

        #using conidtional statements to increment the count of character
        if text.lower().count(i)>0:
            char[i]=char[i]+1
    print(char)
    response = input("Do you want to do this again?? y/n or yes/no")
    if response.lower() == 'y' or response.lower() == 'yes':
        continue
    else:
        print("you've chosen to exit!! Bye!")
        break

