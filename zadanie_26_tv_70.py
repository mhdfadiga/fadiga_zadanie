'''Создайте программу, имитирующую телевизор как объект. У пользователя должна быть возможность вводить
номер канала, а также увеличивать и уменьшать громкость. Программа допжна следить за тем, чтобы номер
канала и уровень громкости оставались в допустимых пределах. '''
class TV:
    def __init__(self):
        self.channel = 1
        self.volume = 5

    def change_channel(self, new_channel):
        if 1 <= new_channel <= 100:
            self.channel = new_channel
            print("Switched to channel", self.channel)
        else:
            print("Invalid channel number")

    def increase_volume(self):
        if self.volume < 10:
            self.volume += 1
            print("Volume increased to", self.volume)
        else:
            print("Maximum volume reached")

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print("Volume decreased to", self.volume)
        else:
            print("Minimum volume reached")

tv = TV()

while True:
    print("nTV Menu:")
    print("1 - Change Channel")
    print("2 - Increase Volume")
    print("3 - Decrease Volume")
    print("0 - Turn Off")

    choice = input("Enter your choice: ")

    if choice == "0":
        print("TV turned off.")
        break
    elif choice == "1":
        new_channel = int(input("Enter the channel number (1-100): "))
        tv.change_channel(new_channel)
    elif choice == "2":
        tv.increase_volume()
    elif choice == "3":
        tv.decrease_volume()
    else:
        print("Invalid choice")