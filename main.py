#1словрь
my_disk={'Galina':1862,'Anatoliy':1963,'Yana':1985}
print(my_disk)
print(my_disk['Yana'])
my_disk['Oleg']=1989#введение новой пары
print(my_disk['Oleg'])
print(my_disk.get('Galina'))
print(my_disk.get('Mariya'))
my_disk.update({'Vladimir':1987,'Anfstasiya':2014})#добавление 2х и более пар
print(my_disk)
print(my_disk.pop('Yana'))#удаление пары
print(my_disk)
#2 множество
my_set={1,2,5,8,1,4,5}
print(my_set)
my_set.update([7,'string'])#добавление 2х и более элементов
print(my_set)
my_set.discard(4)
print(my_set)
