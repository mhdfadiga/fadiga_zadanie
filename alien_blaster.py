class player(object):
    def blast(self,enemy):
        print("Игpoк стреляет во врага.\n")
        enemy.die()
class Alien(object):
    def die(self):

        print("""Tяжeлo дыша. пришелец произносит: 'Ну, вот и все. Спета моя песенка. 
              Уже и в глазах темнеет ... Передай полутора миллионам моих личинок. что я любилих
            Прощай. безжалостный мир.""")

        print("\t\tгибeль пришельца\n")
hello = player()
invader = Alien()
hello.blast(invader)
input("\n\nHaжмитe Enter. чтобы выйти.")
