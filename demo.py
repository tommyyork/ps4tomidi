import pygame

from classes import BeatStepPro
from classes import PS4Controller

ps4 = PS4Controller.PS4Controller()
bsp = BeatStepPro.BeatStepPro()

ps4.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            ps4.axis_data[event.axis] = round(event.value, 2)
        elif event.type == pygame.JOYBUTTONDOWN:
            ps4.button_data[event.button] = True
        elif event.type == pygame.JOYBUTTONUP:
            ps4.button_data[event.button] = False
        elif event.type == pygame.JOYHATMOTION:
            ps4.hat_data[event.hat] = event.value

        # if ps4.hat_data[0][0] == 1:
        #     print('Attempting to play C.')
        #     bsp.play_c()

        x1 = max(round(64 + (ps4.axis_data[0] * 63.5)), 1) - 1
        y1 = max(round(64 + (-ps4.axis_data[1] * 63.5)), 1) - 1
        x2 = max(round(64 + (ps4.axis_data[2] * 63.5)), 1) - 1
        y2 = max(round(64 + (-ps4.axis_data[3] * 63.5)), 1) - 1

        bsp.updateAxes({0: x1, 1: y1, 2: x2, 3: y2})
        bsp.updateOutput()
