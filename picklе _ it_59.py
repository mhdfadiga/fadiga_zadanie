import  pickle,shelve
print("Консервация списков ")
variety =["огурцы", "помидоры", "капуста"]
shape = ["целые" ,"кубиками","соломкой"]
brand = ["Главпродукт" , "Чумак", "Бондюзль"]
f = open("pickles1.dat","wb")
pickle.dump(variety,f)
pickle.dump(shape,f)
pickle.dump(brand,f)
f.close()

print("\nРасконсервация списков.")
f = open("pickles1.dat","rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)

print(variety)
print(shape)
print(brand)
f.close()

print("\nПомещение списков на полку.")
s = shelve.open("pickles2.dat")

s["variety"] = ["огурцы","помидоры", "капуста"]
s["shape"]= ["целые","кубиками", "соломкой"]
s["brand"] = ["Главпродукт","Чумак", "Бондюэль"]
s.sync()

print("\nИзвлечение списков из файла полки:")
print("торговые марки-", s["brand"])
print("фopмы -",s["shape"])
print("виды овощей-", s["variety"])
s.close()
input("\n\nHaжмитe Enter. чтобы выйти.")
