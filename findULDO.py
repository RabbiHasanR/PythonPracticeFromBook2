str=input('Enter a string:')
s1=''
s2=''
s3=''
s4=''
for c in str:
    if c.isupper():
        s1+=c
    if c.islower():
        s2+=c
    if c.isdigit():
        s3+=c
    if not c.isdigit() and not c.isupper() and not c.islower():
        s4+=c

print(s1,'\n',s2,'\n',s3,'\n',s4)   
        
    
