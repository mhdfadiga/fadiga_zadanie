from  livewires import games
games.init(screen_width = 640 ,  screen_height = 480 , fps = 10)
wall_image = games.load_image("wall.jpg", transparent = False)
games.Screen.background = wall_image
games.Screen.mainloop()