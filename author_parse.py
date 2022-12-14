import sys
import pandas as pd
import re

def txtTocsv(fileName):
    """
    This function takes command line argument as paramter and built to read every line and strip unnecessary characters such as (*+-=:;"',./|\!@#$%^&)  
    and store every word into a dictionary(in `Word:Count` format) and
    construct a dataframe from using that dictionary the prints the data to the console.
    """
    print(fileName)
    path = 'authors/' + fileName + '.txt'
    words = dict()
    with open(path, 'r') as file:
        lines = [line.strip().lower() for line in file.readlines() if line.strip()]
        pattern = ':;{}[]\\|+=-_<>,.?/!@#$%^&*()\'\"'
        for line in lines:
            for word in line.split():
                word = ''.join(filter(lambda k: k not in pattern, word))
                word = word.lstrip('“”’')
                word = word.rstrip('“”’')
                if word in words: words[word] += 1
                else: words[word] = 1
        word = words.keys()
        count = words.values()
        print('Unique words : ', len(word))
        data = {'Words': word, 'Count': count}
        df = pd.DataFrame.from_dict(data)
        print('Words,Count')
        for i in range(len(df)):
            print("{},{}".format(df['Words'][i], df['Count'][i]))

txtTocsv(sys.argv[1])