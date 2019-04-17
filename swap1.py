s=input('Enter string:')
t=list(s)
for c in range(0,len(t),2):
    temp=t[c]
    t[c]=t[c+1]
    t[c+1]=temp
print(''.join(t))   

