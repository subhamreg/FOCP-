# Write and test a function that takes a string as a parameter and returns a sorted list
# of all the unique letters used in the string. So, if the string is cheese, the list
# returned should be ['c', 'e', 'h', 's'].


def check_unique(str):
    unique_str=list(set(str)) # CONVERTING TO SET TO GET UNIQUE
    sorted_unique_str=sorted(unique_str)
    return sorted_unique_str
    
result=check_unique('cheese')
print(result)
    