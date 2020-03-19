import pandas as pd

df = pd.read_csv("/Users/aakarsh.rajagopalan/Personal documents/Python projects/CoutingLettersInString/CountingLetterInACsv.csv")
print(df)

dict = {}
for i in range(len(df)):
    names = list(df['Name'][i:i+1])
    print(names[0])

    for j in names[0]:
        dict.setdefault(j, 0)
        dict[j] = dict[j] + 1
    print(dict)


