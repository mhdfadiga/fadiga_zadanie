print(""" \t\t\t\t\t\t\t\t\t\t\t\tРантье 
Программа подсчитывает ваши ежемесячные расходы . Эту статистику нужно знать. чтобы 
у вас не закончились деньги и вам не пришлось искать работу. 
Введите суммы расходов по всем статьям . перечисляемым ниже . Вы богаты - так не мелочитесь. пишите суммы в долларах. без центов. 
 """)
car = int(input("Техническое обслуживание машины 'Ламборгини':"))
rent = int(input("Съем роскошной квартиры на Манхэттене:"))
jet = int(input("Apeндa самолета:"))
gifts =int(input("Подарки:"))
food = int(input("Oбeды и ужины в ресторанах: "))
staff = int(input("Жалованье прислуги (дворецкий. повар. водитель. секретарь):"))
gunu = int(input("Плата личному психоаналитику:"))
game = int(input("Компьютерные игры:"))
total = car + rent + jet + gifts + food + staff + gunu + game
print("\nОбщая сумма:",total)
input("\n\nHaжмитe Enteг. чтобы выйти.")