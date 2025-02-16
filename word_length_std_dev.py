text = "My Cat"

def create_list(string):
    my_list = []
    n = 0
    p = 0
    string += ' '
    while n < len(string):
        while p <= len(string):
            if ' ' in string[n:p-1]:
                my_list.append(string[n:p-1])
                break
            else:
                p += 1
'''This function creates a list from the text provided as an argument. Each word in the text is translated as an element in the list. We can use this list to later iterate through each word'''

def find_avg(list):
    x = 0
    total = 0
    while x < len(list):
        total += len(list[x])
        x += 1
    avg = total / len(list)
    return avg
'''This funds the average length of each word by taking the total number of letters in the list and dividingit by the number of words in the list. This gives us a value of letters per word that will serve as the mean.'''

def word_length_std_dev(string):
    list = create_list(string)
    x = 0
    sum = 0
    avg = find_avg(list)
    while x < len(list):
        sum += (len(list[x])-avg) ** 2
        x += 1
    sum /= (len(list) - 1)
    sum = sum ** 0.5
    return sum
'''The function counts the number of letters each word has, then subtracts it by the mean of letters in each word.The sum of theses differences are squared and added together, then divided by the sum of words minus one.
This total is then square-rooted in order to get the standard deviation'''

answer = word_length_std_dev(text)