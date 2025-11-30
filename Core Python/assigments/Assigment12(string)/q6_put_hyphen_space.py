def space(str):
    new_str = ""
    for ch in str:
        if(ch == " "):
            new_str += "--"
        else:
            new_str += ch
    return new_str
string = "hi i am sakshi"

res = space(string)
print("modified string : ",res)