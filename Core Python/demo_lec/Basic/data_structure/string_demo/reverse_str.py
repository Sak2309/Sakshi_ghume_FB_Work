def rev(str):
    rev_str = ''
    for char in str:
        rev_str = char + rev_str
    return rev_str

str = 'firstbit solution'
print(rev(str))

#using indexing