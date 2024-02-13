# This is a sample Python script.

# Problem 1)
#   Write a function  lesser_of_two_evens that gets two integer inputs.
#   And return the lesser of two given numbers if both numbers are even,
#   but return the greater if one or both numbers are odd.
def lesser_of_two_evens(a1, a2):
    if a1 % 2 == 0 and a2 % 2 == 0:
        return min(a1,a2)
    else:
        return max(a1,a2)


# Problem 2)
#   Write a function get_pangram that gets a string to check
#   whether a string is a pangram or not.
# (Assume the string passed in does not have any punctuation).
def get_pangram(a1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter not in s:
            return "It is not a Pangram"
    return "It is a Pangram"


# Problem 3)
#   Write a function unique_elements that takes a list and returns a new list
#   with unique elements of the first list.
#       a1 - integer-array
#   And outputs an integer array, which contains unique elements of a given list

def unique_elements(a1):
    sendOut = []
    for elem in a1:
        if elem not in sendOut:
            sendOut.append(elem)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

