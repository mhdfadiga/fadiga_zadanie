def birthday1(name,age):
    print( "С днем рождения ",name,"!", " Вам сегодня исполняется",age," не так пи? n")

def birthday2(name = "Товарищ иванов", age = 1):
    print("С днем рождения ", name, "!", " Вам сегодня исполняется", age, " не так пи? n")



birthday1("товариц иванов",1)
birthday1(1,"Товариц иванов")
birthday1( name = "товарищ Иванов",age = 1)
birthday1(age = 1, name = "товарищ Иванов")
birthday2()
birthday2(name= "Катя")
birthday2(age = 12)
birthday2( name = "Катя", age = 12)
birthday2( "Катя",12)


input("\n\nHaжмитe Enter. чтобы выйти.")

