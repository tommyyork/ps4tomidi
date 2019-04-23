import asyncio
from tkinter import *
import logging

import pygame

from classes import BeatStepPro
from classes import PS4Controller
from classes import Window

ps4 = PS4Controller.PS4Controller()
bsp = BeatStepPro.BeatStepPro()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s,%(msecs)d %(levelname)s: %(message)s',
    datefmt='%H:%M:%S',
)


def handle_ps4_events():
    while True:
        event = pygame.event.wait()
        axis_change = False

        button_change = False
        button_to_change = 0
        button_on = False

        if event.type == pygame.JOYAXISMOTION and ps4.axis_data[event.axis] != round(event.value, 2):
            ps4.axis_data[event.axis] = round(event.value, 2)
            axis_change = True
        elif event.type == pygame.JOYBUTTONDOWN and ps4.button_data[event.button] is False:
            ps4.button_data[event.button] = True
            button_to_change = event.button
            button_change = True
            button_on = True
        elif event.type == pygame.JOYBUTTONUP and ps4.button_data[event.button] is True:
            ps4.button_data[event.button] = False
            button_to_change = event.button
            button_change = True
            button_on = False
        # elif event.type == pygame.JOYHATMOTION and ps4.hat_data != event.value:
        #     ps4.hat_data[event.hat] = event.value
        #     hat_change = True

        def round_axis_data(axis_float):
            return max(round(64 + (axis_float * 63.5)), 1) - 1

        if axis_change is True:
            axis_values = {
                'Joy 1 X': round_axis_data(ps4.axis_data[0]),
                'Joy 1 Y': round_axis_data(-ps4.axis_data[1]),
                'Joy 2 X': round_axis_data(ps4.axis_data[2]),
                'Joy 2 Y': round_axis_data(-ps4.axis_data[3] * 63.5)
            }
            bsp.update_axis_output({
                0: Window.joystick_assignments[axis_values['Joy 1 X']],
                1: Window.joystick_assignments[axis_values['Joy 1 Y']],
                2: Window.joystick_assignments[axis_values['Joy 2 X']],
                3: Window.joystick_assignments[axis_values['Joy 2 Y']]
            })
            print('axis_change')
        elif button_change is True:
            bsp.send_gate_output(button_to_change, button_on)

        asyncio.get_event_loop().stop()


async def main():
    ps4.init()

    asyncio.create_task(handle_ps4_events())


if __name__ == "__main__":
    root = Tk()
    app = Window.Window(root)
    root.wm_title("ps4tomidi")
    root.mainloop()

    asyncio.run(main())



