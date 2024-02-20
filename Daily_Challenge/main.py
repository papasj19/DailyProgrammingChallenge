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
    # Write code here
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
    # Write code here
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




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

