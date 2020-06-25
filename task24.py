text1='XaBaJkhА'
total=len(text1)
lower_letters=0
upper_letters=0
for letter in list(text1):
    if letter.islower():
        lower_letters+=1
    elif letter.isupper():
        upper_letters+=1

print('процент маленьких букв: ',lower_letters*100/total)
print('процент больших букв: ',upper_letters*100/total)
