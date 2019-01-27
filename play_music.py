import pygame
import os
import time

# 获取当前目录绝对路径
dir_path = os.path.dirname(os.path.abspath(__file__))
# print('当前目录绝对路径:', dir_path)

# currentPwd = os.getcwd()
# print(currentPwd)
# file= currentPwd[0] + '/test.'
pygame.mixer.init()
track = pygame.mixer.music.load(dir_path + '/test.mp3')

pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.2)

time.sleep(3)
pygame.mixer.music.stop()

