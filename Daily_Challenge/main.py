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
    
# Day 2
#   Write a function count_festivals that takes a list of integers as input,
#   where each integer represents the number of festivals attended by a person in a particular year.
#
#   The function should return the total number of festivals attended
#   by all the people in the list.
def count_festivals(festivals):
    return sum(festivals)
  
  
# Day 3
#  Write a function named check_space that gets string as input
#  and returns True if the given string contains any spaces,
#  otherwise False. It should also return False if the string is empty.
def check_space(s):
    if not s or " " not in s:
        return False
    else:
        return True
    
    
#   Day 4
# Create a function named identify_animal_sound that takes one argument:
# sound (a string) - the recorded sound to be analyzed and identified.
# Inside the function, analyze the provided sound and determine if it matches the sound of a known wild animal.
# You are provided with a list of known animal sounds
#  (e.g., lion's roar, elephant's trumpet, bird's chirp) for the purpose of this challenge.
# Return the name of the first wild animal if the sound matches a known animal sound.
# If it doesn't match any known animal sound, return "Unknown."
known_animal_sounds = {
    "lion": ["roar", "growl", "grunt"],
    "elephant": ["trumpet", "roar", "snort"],
    "bird": ["chirp", "whistle", "tweet"],
}

def identify_animal_sound(sound):
    counter = 0
    while counter < 3:
        if known_animal_sounds["lion"][counter] == sound:
            return "lion"
        elif known_animal_sounds["elephant"][counter] == sound:
            return "elephant"
        elif known_animal_sounds["bird"][counter] == sound:
            return "bird"
        counter = counter + 1
    return "Unknown"



# Day 5
# Create a function named tri_area that returns the area of a triangle based on its base and height.
#
# The formula for calculating the area of a triangle is (base * height) / 2.
# The function should take two arguments, the base and height, and return the calculated area.
def tri_area(base, height):
    return int((base*height)/2)
    

# Day 6
# Given two integers left and right that represent the range [left, right],
# return the bitwise AND of all numbers in this range, inclusive.
def rangeBitwiseAnd(left, right):
    tester = []
    z = left
    while z <= right:
        tester.append(z)
        z = z + 1
    result = left
    for num in tester:
        result &= num
        print(result)
    return result

# Day 7
# Create a function named entangle_qubits that takes a list of integers as input,
# representing the states of qubits. The function should return the result o
# entangling the qubits by applying the XOR operation between adjacent qubits,
# iterating from left to right, and creating new entangled qubits.
def entangle_qubits(qubits):
    counter = 0
    leng = len(qubits)
    done = []
    if len(qubits) == 1:
        return qubits
    while counter < leng-1:
        done.append(qubits[counter] ^ qubits[counter+1])
        counter = counter + 1
    return done



# Day 8
# Write a Python function named is_interesting that will check if a given
# list of integers taken at different times throughout the day represent
# the intensity of the sunset. To be considered interesting,
# the list should be non-increasing; that is, every next number is
# less or equal to (but not just less than) the previous.
# Additionally, the sunset should reach at least the value 50 in
# order to be considered interesting.
#
# The function should return True if the list is interesting,
# and False otherwise.
def is_interesting(numbers):
    prev = 100000
    firstFlag = False
    hitFifty = False
    interesting = False
    for number in numbers:
        if number <= prev:
            if 59 >= number >= 50 and firstFlag:
                hitFifty = True
            prev = number
        else:
            return False
        firstFlag = True
    if hitFifty:
        return True
    else:
        return False


# Day 9
#  Write a function named random_int that gets to integers as an arguments,
#  a and b, the function should return a random integer that falls within
#  the range of a and b (inclusive).
def random_int(a,b):
    begin = a
    nums = []
    while begin <= b:
        nums.append(begin)
        begin = begin + 1
    return random.choice(nums)


# Day 10
def calculate_vacant_area(beach):
    counter = 0
    for sec in beach:
        for spot in sec:
            if spot == 'S':
                counter = counter + 1
    return counter


# Day 11
# Write a function min_max that takes a list of integers and
# returns a list containing the minimum and maximum values, in that order.
def min_max(nums):
    nums.sort()
    return [nums[0],nums[-1]]
    
    
# Day 12
#  Write a function extract_domain(url) that takes a string url as input
#  and returns the domain name (including the subdomain if present) without
#  the http:// or https:// part. The function should be case-insensitive
#  and should handle both http:// and https:// URLs.
def extract_domain(url):
    broken = url.split('/')
    goodWords = []
    for word in broken:
        if not "http" in word and word:
            goodWords.append(word.lower())
    if len(goodWords) > 1:
        for goodw in goodWords:
            if "www" in goodw or "co" in goodw:
                return goodw
    else:
        return goodWords.pop(0)


# Day 13
#  Write a function find_odd_occurrence(arr) that takes a list of integers
#  as input and returns the number that occurs an odd number of times.
#  The input list will always contain only one number that occurs an odd
#  number of times, while all others occur an even number of times.
def find_odd_occurrence(arr):
    res = {}
    for num in arr:
        if num not in res:
            res[num] = 1
        else:
            res[num] = res[num] + 1
    for numb in res:
        if res[numb] % 2 != 0:
            return numb


# Day 14
def arrayStringsAreEqual(word1, word2):
    """
    :type word1: List[str]
    :type word2: List[str]
    :rtype: bool
    """
    wordOne = ''.join(word1)
    wordTwo = ''.join(word2)
    return wordOne == wordTwo


# Day 15
def countCharacters(words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        goodW = []
        for wrd in words:
            counter = 0
            leng = len(wrd)
            for let in wrd:
                if let in chars:
                    counter = counter + 1
                else:
                    counter = 0
            if counter == leng:
                goodW.append(len(wrd))
        return sum(goodW)


# Day 16
# Write a python function named check_alphabet_order that takes a string
# as input and return True if the letters of the input string are in
# alphabetical order, and False otherwise.
def check_alphabet_order(a):
    # Write code here
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True


# Day 17
# Write a function named ctoa that provides the ASCII value of a
# given character.
def ctoa(x):
    return ord(x)


# Day 18
# Write a function sum_of_two_values(arr, target) that takes a list of
# numbers arr and a target number target as input and returns a
# tuple of two numbers that add up to the target number, if such a pair exists.
# If no such pair exists, the function should return [].
def sum_of_two_values(arr, target):
    # Write code here
    for val in arr:
        otherVal = target - val
        if otherVal in arr:
            ind1 = arr.index(val)
            ind2 = arr.index(otherVal)
            if ind1 != ind2:
                return [val,otherVal]
            else:
                otherValOccur = arr.count(val)
                if otherValOccur > 1:
                    ind2 = arr.index(otherVal,ind1)
                    return [val,arr.pop(ind2)]
    return []




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

