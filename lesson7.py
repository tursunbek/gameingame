# dict1={
#     'users':['ba','nurs','roma','tiku','nur','beka'],
#     'age':{'ba':20,
#            'nurs':17,
#            'roma':18,
#            'tiku':14,
#            'nur':25,
#            'beka':12,}
# }
# for x in dict1['users']:
#     print(x)
#     print('возраст:',dict1['age'][x])

# year=1
# while year<= 25:# условия верна то цикл продолжается
#     print(year)
#     print('happy new year')
#     year += 1

# mes=''
# while mes!='quit':# нужно вести имя пользователя после этого заканчивается
#     mes=input('напишите свое имя')
#     print('hello',mes)

active=True
while active:
    mes=input('введите сообшение.')
    if mes==input:
        active=False
    elif mes=='exit':
        active=False
    print(mes)








