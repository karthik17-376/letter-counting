sentence='Mississippi'
sl = sentence.lower()

d = {}.fromkeys([x for x in sl],0)
for char in sl:
    d[char] += 1
    
print(d) 
