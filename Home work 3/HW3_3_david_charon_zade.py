# this library can convert an integer to its numerical meaning
import inflect

# opening the needed text file
with open('words.txt', mode='r') as file:
    words = file.read()

# evaluating the string into it's former meaning
words = eval(words)

# using popped to store the bad elements:
popped = []

# starting to build our elements with the followong logic:
   # if the number in each element at the second place [1] is greater than 1 or the amount of elements at the list on the third place in the element is bigger than one:
   # append popped with words[i]
for i in range(0, len(words)):
    if words[i][1] > 1 or len(words[i][2]) > 1:
        popped.append(words[i])

# leaving the original words file untouched, because he contains the good combinations also.
# for word in popped:
#     words.pop(words.index(word))

# creating an object for inflect
p = inflect.engine()

# creating a temp string to store only numerical values which should be displayed as words later on.
temp = []

# appending temp with word[0:2], because they are needed to display on the console later on
for word in popped:
    temp.append([word[0], word[1]])

# now we will append the * number * of the elements in the list of each element in popped.
for i in range(0, len(temp)):
    if len(popped[i][2]) > 1 and popped[i][2] != ' ':
        temp[i].append(len(popped[i][2]))

# printing our list with the up-dated numerical values to words on the console
for word in temp:
    if len(word) == 2:
        print(f" (*) '{word[0]}' because it appears at least {p.number_to_words(word[1])} times")

    elif len(word) == 3:
        if word[1] == 1:
            print(f" (*) '{word[0]}' because it belongs to at least {p.number_to_words(word[2])} categories ")

        else:
            print(f" (*) '{word[0]}'  because it belongs to at least {p.number_to_words(word[2])} categories and because it appears at least {p.number_to_words(word[1])} times ")

