def txtTocsv(fileName):
    import pandas as pd
    import re
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
#         print('Unique words : ', len(word))
        data = {'Words': word, 'Count': count}
        df = pd.DataFrame.from_dict(data)
        filename = fileName + '.csv'
        df.to_csv(filename, index=False)
        
for i in range(1, 6):
    filename = 'a' + str(i)
    txtTocsv(filename)
    filename = 'b' + str(i)
    txtTocsv(filename)
txtTocsv('ua')
txtTocsv('ub')