task1 = 'Какое у тебя есть увлечения?'
ans11 = 'программирование'
ans12 = 'рисование'
ans13 = 'прыгать с парашютом'

task2 = 'Ты когда нибудь опаздывал?'
ans21 = 'никогда'
ans22 = 'почти никогда'
ans23 = 'часто'

task3 = 'Какой твой любимы предмет в школе?'
ans31 = 'физика'
ans32 = 'изо'
ans33 = 'физкультура'

task4 = 'Кем бы ты хотел стать?'
ans41 = 'пожарным'
ans42 = 'дизайнером'
ans43 = 'программистом'

print(task1)
input1 = input()
input1 = input1.lower()
print(task2)
input2 = input()
input2 = input2.lower()
print(task3)
input3 = input()
input3 = input3.lower()
print(task4)
input4 = input()
input4 = input4.lower()

if input1.find(ans11) != -1 and input2.find(ans21) != -1 and input3.find(ans31) != -1 and input4.find(ans43) != -1:
    print("Вы умный человек!")
elif input1.find(ans12) != -1 and input2.find(ans22) != -1 and input3.find(ans32) != -1 and input4.find(ans42) != -1:
    print('Вы творческий человек!')
elif input1.find(ans13) != -1 and input2.find(ans23) != -1 and input3.find(ans33) != -1 and input4.find(ans41) != -1:
    print('Вы экстримал!')
else:
    print('Вы разносторонний человек!')