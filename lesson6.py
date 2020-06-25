# user_0={
#         'username':'eferni',
#         'first':'enrico',
#         'last':'ferm',
# }

# list=[]
# values=[]


# for key,value in user_0.items():# перебор словаря через цикл
#     list.append(key)# добавляет ключи в наш пустой список
#     values.append(value)

#     print(list)
#     print(values)
#     # print('key:',key)
    # print('values:',value)


# list1=[]

# for key in user_0.keys(): # перебор метод словаря. который дает нам только из него
#     print(key)
#     list.append(key)

#     print(list)


user_0={
    'python':'ba',
    'java':'Nurs',
    'c++':'roma',
    'js':'turs',
}

for value in sorted(user_0.values()):
    if value=='roma':
        print('roma learns c++')
    elif value=='ba':
        print('ba lesrns python')
    elif value=='turs':
        print('turs learn js')

x=True+5
print(x)