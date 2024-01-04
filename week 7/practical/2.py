# Write and test three functions that each take two words (strings) as parameters and
# return sorted lists (as defined above) representing respectively:
# Letters that appear in at least one of the two words.
# Letters that appear in both words.
# Letters that appear in either word, but not in both.
# Hint: These could all be done programmatically, but consider carefully what topic we
# have been discussing this week! Each function can be exactly one line.

# Letters that appear in at least one of the two words.
def func_1(para_1, para_2):
    unique_str=list(set(para_1) | set(para_2))
    sorted_unique_str=sorted(unique_str)
    return sorted_unique_str

print(func_1('sub', 'rat'))

# Letters that appear in both words.
def func_1(para_1, para_2):
    unique_str=list(set(para_1) & set(para_2))
    sorted_unique_str=sorted(unique_str)
    return sorted_unique_str

print(func_1('st', 'ttt'))

# Letters that appear in either word, but not in both.
def func_1(para_1, para_2):
    unique_str=list(set(para_1) - set(para_2))
    sorted_unique_str=sorted(unique_str)
    return sorted_unique_str

print(func_1('st', 'ttt'))

    
    