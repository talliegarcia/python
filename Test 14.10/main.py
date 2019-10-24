import csv

students_list = list()

with open('test_data.csv', encoding="utf-8") as csvfile:
    flats_csv = csv.reader(csvfile, delimiter=',')
    students_list = list(flats_csv)

print(students_list)

# TODO 1: используя множества, выведите все иностранные языки, которыми владеют студенты (без повторов). например, в таком виде:
# Английский,Украинский
header = students_list.pop(0)
language_set = set()
for student in students_list:
  language = student[1].lower().strip()
  if len(language) > 0: 
    language_set.add(language) 
print (language_set)

# TODO 2: у некоторых студентов язык не указан. Сделайте проверку на пустое значение через assert
# не забудьте добавить код перехвата и обработки исключения
for student in students_list:
  language = student[1].lower().strip()
  try:
    assert len(language)>0 
  except:
    print(student[0], "Не указан язык") 
  else:
    language_set.add(language) 
#    print (student[0], student[1])

# TODO 3: подсчитайте и выведите УНИКАЛЬНЫЕ имена студентов (т.е. те, которые встретились в списке students_list только один раз)
# например, в таком виде: Кирилл, Максим, Виталина,...
# для неуникальных имен выведите имя и количество повторов. Например:  Андрей, 2
# подсказка: решите эту задачу не "в лоб" перебором списка, а другим способом:
# 1) сделайте множество из имен,
# 2) используйте его для прохода по списку и подсчета частоты встречаемости имен
# не забудьте отделить фамилию от имени через string.split()
#for name in name_set:
#  for 
name_set = set()
name_list=list()
for student in students_list:
  name = student[0].split(" ")
  name_list.append(name[1])
  name_set.add(name[1])
print (name_set)
print (name_list)
for name in name_set:
  counter=name_list.count(name)
  if (counter == 1):
    print(name, " - уникальное имя")
  else:
    print (f"Имя {name} встречается {counter} раза")