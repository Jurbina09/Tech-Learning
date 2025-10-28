# TASK 1 - Create a variable that is the sum of two numbers
x=3+1 
 
# TASK 2 - Create an array and then create a new variable that is equal to the last element in the array
num_list=[1,2,3,4,5,6,7,8,9]
x=num_list[-1]
 
# TASK 3 - Create a conditional statement that will log "success" to the console with a truthy statement, and it will also log "error" with a falsely statement
if x == True:
    print("success")
else:
    print("error")
 
# TASK 4 - Create a loop that will log to the console exactly 4 times
#loop that runs 4 times
for x in range(4):
    print(f"x")

"""
TASK 5 - Create a function called max that returns the biggest number in a given array
 
Examples:
 
max([1,27,1,5])
 
Output: 27
 
max([-9000, 237891, 2779, 0, 32.7, 9])
 
Output: 237891
"""
def max(numbers: list):
    temp=numbers[0]
    for x in range(len(numbers)):
        if temp < numbers[x]:
            temp=numbers[x]
    return temp

print(max([-9000, 237891, 2779, 0, 32.7, 9]))

"""
TASK 6 - Create a function called sum that returns the sum of numbers from a given array
 
Examples:
 
sum([1,2,3,4]);
 
Output: 10
 
sum([32.7, -45.5, 0, 31])
 
Output: 18.2
"""
def sum(numbers: list):
    answer=0
    for x in range(len(numbers)):
        answer+=numbers[x]
    return answer

"""
TASK 7 - Create a function called reverseString that reverses a string and returns the reversed string
 
Examples:
 
reverseString("Hello world")
 
Output: "dlrow olleH"
 
reverseString("My name is Collin")
 
Output: "nilloC si eman yM"
"""
def reverseString(phrase: str):
    return phrase[::-1]

print(reverseString("Hello World"))
"""
TASK 8 - Create a function called reverseArray that reverses the order of elements in an array and returns it
 
Examples:
 
reverseArray([1,2,3,4,5])
 
Output: [5,4,3,2,1]
 
reverseArray(["Hello", "my", 5, true])
 
Output: [true, 5, "my", "Hello"]
"""
def reverseArray(items: list):
    temp_list=[]
    temp_list.append(items[::-1])
    return temp_list

print(reverseArray([1,2,3,4,5]))
 
"""
TASK 9 - Create a function called sortNumbers that orders an array of
integers, floating point, or negative numbers from smallest to greatest and returns the array
 
Examples:
 
sortNumbers([5,7,2,8])
 
Output: [2,5,7,8]
 
sortNumbers([-3, 4.5, 2.1, -67, 987])
 
Output: [-67, -3, 2.1, 4.5, 987]
"""
def sortNumbers(numlist):
    reps=len(numlist)-1
    for x in range(reps):
        for i in range(reps-x):  
            if numlist[i] > numlist[i+1]:
                numlist[i], numlist[i+1] = numlist[i+1], numlist[i]
    return numlist
print(sortNumbers([-3, 4.5, 2.1, -67, 987]))
"""
TASK 10 - Create a function called firstOccurrence that searches for a specific number and it's
first occurrence in an array, if the number is found, return
the index that the number is at. if it is not found, return "Number not found". The function
should have two parameters: an array and a number to search for
 
Examples:
 
firstOccurrence([1,3,7,2, -4], 7)
 
Output: "First occurrence of 7 was found at index 2"
 
firstOccurrence([-3, 3, 3, 6, 1], 3)
 
Output: "First occurrence of 3 was found at index 1"
 
firstOccurrence([3.7, -2, 6, 90, 1], 798)
 
Output: "798 was not found"
"""
def firstOccurance(numbers: list, target: int):
    if target in numbers:
        index=numbers.index(target)
    else:
        print(f"{target} was not found")
        return
    print(f"First occurance of {target} was found at index {index}")

