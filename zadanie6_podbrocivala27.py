"""Напишите программу, которая бы «Подбрасывала» условную монету 100 раз и сообщала, сколько раз выпал
орел, а сколько
- решка. """
import random
orel =''
reska = ''
orel_sum = 0
reska_sum = 0
count = 0
while  count != 100:
    count += 1
    resultat =random.randint(1,2)
    if resultat == 1:
        orel_sum += 1
    else:
        reska_sum += 1
print("orel=",orel_sum,"reska=",reska_sum)