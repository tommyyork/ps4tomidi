import pygame

from classes import BeatStepPro
from classes import PS4Controller

ps4 = PS4Controller.PS4Controller()
BeatStepPro = BeatStepPro.BeatStepPro()

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

        # Insert your code on what you would like to happen for each event here!
        # In the current setup, I have the state simply printing out to the screen.
        #
        # os.system('clear')
        # pprint.pprint(self.button_data)
        # pprint.pprint(self.axis_data)
        # pprint.pprint(ps4.hat_data[0][0])

        if ps4.hat_data[0][0] == 1:
            print('Attempting to play C.')
            BeatStepPro.play_c()