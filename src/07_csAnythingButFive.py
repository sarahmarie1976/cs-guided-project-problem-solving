"""
"Given a start integer and an ending integer (both inclusive), write a function that returns the count (not the sum) of all integers in the range (except integers that contain the digit 5)."

Examples:

csAnythingButFive(1, 5) -> 1, 2, 3, 4, -> 4 (there are 4 integers in the range that do not contain the digit 5)
csAnythingButFive(1, 9) -> 1, 2, 3, 4, 6, 7, 8, 9 -> 8
csAnythingButFive(4, 17) -> 4,6,7,8,9,10,11,12,13,14,16,17 -> 12
Notes:

The output can contain the digit 5.
The start number will always be less than the end number (both numbers can also be negative).
[execution time limit] 4 seconds (py3)

[input] integer start

[input] integer end

[output] integer

"""



def csAnythingButFive(start, end):

    minStart = start
    maxEnd = end
    counter = 0
    maxEnd = maxEnd + 1
   
    mylist = list(range(minStart,maxEnd))   

    for x in mylist:
        if "5" in str(x):
            counter = counter + 1
       
    # fives = mylist.count("5")
    counted = len(mylist)

    result = int(counted) - int(counter)
    
    return result

    


print(csAnythingButFive(1, 5))
print(csAnythingButFive(1, 9))
print(csAnythingButFive(4, 17)) 
print(csAnythingButFive(6, 20)) 
