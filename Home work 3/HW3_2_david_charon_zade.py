"""
question 2
"""
from collections import Counter

def q1_neat_function(file):

    # changing the uppercase to lowercase as a default:
    file = file.lower()

    # spliting the file to a list of words:
    file = file.split()

    # creating a comparing string:
    sub_val_str = "qwertyuiopasdfghjklzxcvbnm"

    # creating punctuation string:
    sub_punc_str =",.?!"

    # create a popped list to see if the algorithm is working properly:
    popped = []

    # checking the requirments:
    for i in range(0, len(file)):
        if file[i][0] in sub_punc_str:
            file[i] = file[i][1:]
        elif file[i][len(file[i])-1] in sub_punc_str:
            file[i] = file[i][:len(file[i])-1]

    for word in file:
        for i in range(0, len(word)):
            if word[i] not in sub_val_str:
                popped.append(word)

    for word in popped:
        file.pop(file.index(word))



    # concatinating the list into a sring
    res = ''
    for word in file:
        res = res + word + ' '

    # result example:
    print(f"bad words: {popped}\ngood words: {res}")

    print(file)

    # opening ght dictionary:
    new_dic = 0
    with open('dictionary.txt', mode='r') as dic_file:
        new_dic = dic_file.read()
        new_dic = eval(new_dic)

    new_file = file

    x = sorted(new_file, key=str, reverse=True)
    y = list(dict.fromkeys(x))

    count_list = []

    for index in y:
        count_list.append(x.count(index))

    res_list = []

    for i in x:
        if i not in new_dic:
            new_dic[i] = ' '

    for i in range(0, len(y)):
        res_list.append((y[i], count_list[i], new_dic[y[i]]))

    print( res_list )
    with open('words.txt', mode= 'w') as resObj:
        resObj.write(repr(res_list))


with open('text.txt', mode='r') as file:
    text_str = file.read()

q1_neat_function(text_str)














