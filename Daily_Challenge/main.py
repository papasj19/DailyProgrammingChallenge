# This is a sample Python script.

# Day 1
#   Create a function named filter_list that takes a list of non-negative
#   integers and strings and returns a new list without the strings.
#   The function should maintain the original order of the integers in the list.
def filter_list(a):
    sendOut = []
    counter = 0
    types = [type(x) for x in a]
    for elem in types:
        if int is elem: 
            sendOut.append(a[counter])
        counter = counter + 1
    return sendOut








# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

