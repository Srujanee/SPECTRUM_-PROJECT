word = input()#taking word inTERship.speCTrum.coM
word1=''
for i in word:
    if(i.isupper())==True:
        word1+=(i.lower())
    elif(i.islower())==True:
        word1+=(i.upper())
    elif(i.isspace())==True:
        world1+=i
print(word1)        
        

