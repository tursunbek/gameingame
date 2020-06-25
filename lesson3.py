# # Функция for и перебор спика
# magicians=['alice','david','carolina']
# for magician in magicians:
#     print('my name is '+ magician.upper())
# numbers=[2,3,4,5,6,7,8,9]
# squares=[]
# for number in numbers:
#     squares.append(number**2) #возводит а квадрат и добавляет в пустой список
#     print(squares)
for x in range(20):# генератор числовой последовательности с нуля до 9
    print(x)
x=int(input('введите диапозон чисел'))
numbers_list=list(range(1,x))# переслиятн от 1 до 14 горизонтальна с пробелом
print(sum(numbers_list))# команда сум добавляет 1+2+3+4 и тд

