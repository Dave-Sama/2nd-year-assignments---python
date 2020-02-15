from tkinter import filedialog
from tkinter import *
"""
1'st part
"""

# root = Tk()
# root.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
# print(root.filename)
# txt = open(root.filename, 'r')
# lala = txt.read()
# lala = lala.lower()
# Label(root, text=lala).pack()
#
# root.mainloop()

def neat_function(raw_file):

    # converting files to a string:
    proper_list = raw_file.read()

    # changing the uppercase to lowercase as a default:
    proper_list = proper_list.lower()

    # spliting cities to list of words:
    proper_list = proper_list.split()

    # removing the duplicates:
    for i in range(0, len(proper_list)):
        for j in range(i + 1, len(proper_list)):
            if proper_list[i] == proper_list[j]:
                print(f"removed: {proper_list[j]}")
                proper_list.pop(j)
                j += 1
            i += 1

    # closing the file:
    raw_file.close()

    # printing the file to text it's correctness:
    print(proper_list)

    # returning the manufactured list:
    return proper_list


# opening cities:
files = open(file="cities.txt", mode='r')
cities = neat_function(files)


# opening colors:
files = open(file="colors.txt", mode='r')
colors = neat_function(files)


# opening fruits:
files = open(file="fruit.txt", mode='r')
fruits = neat_function(files)


# openings names:
files = open(file="names.txt", mode='r')
names = neat_function(files)

# concatenating the list's into one list:
new_str = cities + colors + fruits + names

# creating new dictionary:

my_dict = {}

# adding the right keys into the dictionary:
for word in new_str:
    if word in my_dict.keys():
        continue
    else:
        my_dict[word] = []

for key in my_dict:
    if key in cities:
        x = 'cities'
        my_dict[key].append(x)

    if key in colors:
        x = 'colors'
        my_dict[key].append(x)

    if key in fruits:
        x = 'fruits'
        my_dict[key].append(x)

    if key in names:
        x = 'names'
        my_dict[key].append(x)


# for example:
print(my_dict['orange'])

with open('dictionary.txt', mode='w') as file:
    file.write(repr(my_dict))



