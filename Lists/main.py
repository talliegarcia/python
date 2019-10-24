# 1) Измените структуру данных, используемую для хранения данных о квартире. Сейчас квартира = список. Сделайте вместо этого квартира = словарь следующего вида: flat_info = {"id":flat[0], "rooms":flat[1], "type":flat[2], "price":flat[11]}. В задании используйте поля: идентификатор квартиры на ЦИАН, количество комнат, тип (новостройка или вторичка), стоимость

# 2) Подсчитайте количество новостроек, расположенных у каждого из метро
import csv

# читаем информацию о квартирах в список flats_list
flats_list = list()
with open('output.csv', encoding="utf-8") as csvfile:
  flats_csv = csv.reader(csvfile, delimiter=';')
  flats_list = list(flats_csv)

# убираем заголовок
header = flats_list.pop(0)

# создаем словарь с информацией о квартирах
# TODO 1: добавьте код, который генерирует новую структуру данных с информацией о квартире - словарь вместо списка
    # ваш код...
    # не забудьте сделать проверку типа и преобразовать то, что можно, в числа
subway_dict = {}
for flat in flats_list:
  subway = flat[3].replace("м.", "")
  subway_dict.setdefault(subway, [])
  flat_info = {"id":int(flat[0]), "rooms":flat[1], "type":flat[2], "price":int(flat[11])}
  subway_dict[subway].append(flat_info)

# TODO 2: подсчитайте и выведите на печать количество новостроек, расположенных рядом с каждым из метро. Используйте вариант прохода по словарю, который вам больше нравится
counter =0
for k, v in subway_dict.items():
  count = 0
  for i, j in enumerate(v):
    if ('новостройка' in v[i].values()):
      count+=1
      counter+=1
  print (f'У метро {k} - {count} новостроек')
print(f'Всего новостроек {counter}')

