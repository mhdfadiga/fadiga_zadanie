""" Напишите программу- симулятор пирожка с «сюрпризом»,
- которая бы при запуске отображала один из
пяти различных «Сюрпризов», выбранный случайным образом.  """
import  random
number = random.randint(1,5)
if number == 1:
    print("anannas ")
elif number == 2:
    print("mabgo")
elif number == 3:
    print("orange")
elif number == 4:
    print("apple")
else:
    print("juice")