def word_frequence(t):
    freq ={}
    word = t.split()

    for i in word:
        freq[i] = freq.get(i, 0) + 1
    
    return freq

str =input("enter the string : ")

res = word_frequence(str)

print("word frequence dictionary :" , res)
