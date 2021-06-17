# Modules
import pygame
import director
import scene_home
 
def main():
    dir = director.Director()
    scene = scene_home.SceneHome(dir)
    dir.change_scene(scene)
    dir.loop()
 
if __name__ == '__main__':
    pygame.init()
    main()