#Find the First Non-Repeating Character in a String
def first_non_repeating_char(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch]+=1 
        else:
            freq[ch] = 1
    for ch in freq:
        if freq[ch] == 1:
            return ch 

    return -1 

print(first_non_repeating_char("aabbcdef")) 
        