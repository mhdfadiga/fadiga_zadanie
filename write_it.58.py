print("Coздaю текстовый файл методом write() . ")
tex_file = open("write_it_58_8.txt","w",encoding='utf-8')
tex_file.write("Строка 1 \n")
tex_file.write("Строка 2 \n")
tex_file.write(" В этой Строке достался  номер 3 \n")
tex_file.close()
print("\nЧитaю вновь созданный файл.")
text_file = open("write_it_58_8.txt","r", encoding='utf-8')
print(text_file.read())
text_file.close()

print("\nСоздаю ;екстовый файл методом wri tel i nes (). ")
tex_file = open("write_it_58_8.txt0","w",encoding='utf-8')
lines = ["Строка 1\n",
        "Это строка 2\n",
        "Этой строке достался номер 3\n"]

tex_file.writelines(lines)
tex_file.close()


print("\nЧитaю вновь созданный файл.")
text_file = open("write_it_58_8.txt", "r", encoding='utf-8')
print(text_file.read())
text_file.close()
input("\n\nHaжмитe Enter. чтобы выйти.")
