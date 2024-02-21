

# Day 1
def list_to_dict(lst,k):
    count_dict = {}
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    sorted_dict = dict(sorted(count_dict.items(), key=lambda item: item[1]))
    counter = 0
    while counter < k:
        min_value = min(sorted_dict.values())
        min_key = [key for key, value in sorted_dict.items() if value == min_value][0]
        if sorted_dict[min_key] == 1:
            del sorted_dict[min_key]
        else:
            sorted_dict[min_key] -= 1
        counter = counter + 1

    return len(sorted_dict)


# Day 2
# Given an integer n, return true if it is a power of two. Otherwise, return false.
def isPowerOfTwo(n):
        """
        :type n: int
        :rtype: bool
        """
        z = n
        if n == 1:
            return True
        if n % 2 == 0:
            while z > 1:
                z = z / 2
                if z == 1:
                    return True
                elif z % 2 != 0:
                    return False
        else:
            return False
            

# Day 3
#   Given an array nums containing n distinct numbers in the range [0, n],
#   return the only number in the range that is missing from the array.
def missingNumber(nums):
    nums.sort()
    prevNum = -1
    for numb in nums:
        if numb != prevNum+1:
            return numb-1
        else:
            prevNum = numb
    return len(nums)
    

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
    
    

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(isPowerOfTwo(16))

