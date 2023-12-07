### Dates ###

# Modules
from datetime import datetime, time, date # Nos trae la fecha, hora, tiempo

for i in range(0,61):
    now = datetime.now()
    print(f' La hora es : {now.hour} : {now.minute} : {now.second}')
    # time.sleep(1)

current_time = time(hour = 13, second=15 )
print(current_time)

current_date = date(2012, day=12, month=12) 
print(type(current_date))

current_date = date.today()
print(current_date)

# Sintaxis de comprension de listas
# [nueva_expresion for elemento in iterable]

my_list = [0,0,'pepe',3,4,3,6,8,4,10,3]
print(my_list)

my_range = range(11)
print(list(my_range))

my_list2 = [i for i in range(11)]
print(my_list2)

for i in my_list:
    if i == my_list[2]:
        print(i)
    else:
        print("NO")

my_list2 = [i + 1 for i in range(5)]
print(my_list2)

my_list2 = [i * i for i in range(5)]
print(my_list2)

my_list2 = [i * 3 for i in range(5)]
print(my_list2)