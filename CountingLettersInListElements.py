import pandas as pd

#reading the csv file using pandas
df = pd.read_csv("/Users/aakarsh.rajagopalan/Personal documents/Python projects/CoutingLettersInString/CountingLetterInACsv.csv")

#printing the dataframe onto console for user to see the data
print(df)

#initializing a dictionary to be used to store the character counts
dict = {}

#creating a loop to iterate through each element in the dataframe
for i in range(len(df)):

    #isolating the items in the dataframe, element by element and storing it in a variable.
    #Converting the output of the inner bracket to a list as it is output as an ndarry
    names = list(df['Name'][i:i+1])

    #priting the value at index 0. please note that 0 is hardcoded because at any instance in time, within the loop, there will be only 1 element
    print(names[0])

    #creating a loop to reach each character at index 0
    for j in names[0]:
        dict.setdefault(j, 0)
        dict[j] = dict[j] + 1
    print(dict)
    
    #resetting the dictionary to an empty dictionary
    dict.clear()


