room_list = [ #Квест про Дениса
["Подземелье", 5, 1, None, None],
["Коридор", 6, 2, None, 0],
["Оружейная", 7, 3, None, 1],
["Заброшенная лаборатория", None, None, 4, 2],
["Подвал Дениса", 3, None, None, None],
["Спальня", None, 6, 0, None],
["Холл", 8, 7, 1, 5],
["Кухня", None, None, 2, 6],
["Балкон", None, None, 6, None]]
current_room = 0
cardinal_directions = ["на север","на восток","на юг","на запад"]
discription = [
"-Вы находитесь в пыльном подземельи поместья.\n-Тут невероятно воняет, но вы видите открытые двери.",
"-Вы находитесь в огромном и роскошном, но запущенном до мурашек по коже коридоре.\n-Здесь стоило-бы провести ремонт.",
"-Вы забрели в старую оружейную.\n-Здесь находится достаточно оружия, чтобы совершить королевский переворот!",
"-Вы зашли в заброшенную лабораторию.\n-Здесь повсюду самогонные апараты, и пробирки с кислотой.\n-Так-же есть дневник, в нём написанно что это подготовка к некому обряду - 'Spirta Diena', чтобы это не значило...",
"-Вы заходите в подвал...\n-Невозможно описать словами какие жуткие эксперементы на людях проводил этот больной ублюдок.\n-Денис... я тебя найду!",
"-Вы заходите в спальню\n-Обычная спальня хозяев поместья, но спать на этой кровати я бы не стал.",
"-Вы заходите в холл\n-Вы чувствуете как с какой-то из сторон дует ветер, видимо выход близко.",
"-Вы зашли на кухню.\n-На удивление кухня убрана, и в духовке даже что-то готовится\n-Мне кажется это еда отравлена, как я вычитал в дневнике в одной из комнат, здесь работает поваром некий Лазуритный Берег\n-Не доверяю я этому прозвищу.",
"\n\n\n-Вы добрались до балкона!\nВы уже чувствуете вкус свободы! Но вдруг в глазах резко темнеет, и вы падаете без сознания с жуткой головной болью...\n\n\n\n   To be continued..."]
def check(a):
    global current_room
    str = a.lower()    
    if str == "север":
        if room_list[current_room][1] != None:
            current_room = room_list[current_room][1]
        else:
            print("Здесь нет прохода.")
    elif str == "восток":
        if room_list[current_room][2] != None:
            current_room = room_list[current_room][2]  
        else:
            print("Здесь нет прохода.")       
    elif str == "юг":
        if room_list[current_room][3] != None:
            current_room = room_list[current_room][3]
        elif current_room == 4:
            print("------------- ДЕНИС ГЕЙ -------------")
        else:
            print("Здесь нет прохода.")      
    elif str == "запад":
        if room_list[current_room][4] != None:
            current_room = room_list[current_room][4]   
        else:
            print("Здесь нет прохода.")      
    else:
        print("Здесь нет прохода.") 
while current_room !=8:
    rooms = ""
    print()
    print(discription[current_room])
    for i in range(4):
        if room_list[current_room][i+1] != None:
            rooms += f" {cardinal_directions[i]} и"
    rooms = rooms[0:len(rooms)-2]
    print(f"Переходы ведут{rooms}.")
    a = input(str("В каком направлении идти? "))
    check(a)
print(discription[current_room])
