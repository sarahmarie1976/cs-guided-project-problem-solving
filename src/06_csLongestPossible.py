"""
Given two strings that include only lowercase alpha characters, str_1 and str_2, write a function that returns a new sorted string that contains any character (only once) that appeared in str_1 or str_2.

Examples:

csLongestPossible("aabbbcccdef", "xxyyzzz") -> "abcdefxyz"
csLongestPossible("abc", "abc") -> "abc"
[execution time limit] 4 seconds (py3)

[input] string str_1

[input] string str_2

[output] string

"""
def csLongestPossible(str_1, str_2):
    # two strings that have only lowercase letters 
    # combine both strings 
    # but with no duplicate letters

    unique_str1 = set(str_1)
    unique_str2 = set(str_2)
    # combine str_1 and str_2 
    unique_str1.update(unique_str2)

    # pass in the variable with both strings
    s = list(unique_str1)
    s.sort()
    

    

    # diff_element = unique_str1 - unique_str2
    # output = str_1 + str(diff_element)
    # return output
    return "".join(s)
    



    


print(csLongestPossible("aabbbcccdef", "xxyyzzz"))  
print(csLongestPossible("abc", "abc"))



