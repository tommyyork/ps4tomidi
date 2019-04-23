import asyncio
from tkinter import *
import pygame
from pprint import pprint
import threading
from functools import partial

from classes import BeatStepPro
from classes import PS4Controller
from classes import Window

ps4 = PS4Controller.PS4Controller()
bsp = BeatStepPro.BeatStepPro()

def handle_ps4_events():
    while True:
        event = pygame.event.wait()

        button_change = False
        button_to_change = 0
        button_on = False
        axis_change = True

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
            channel_values = {
                'Channel A - Pitch': round_axis_data(ps4.axis_data[0]),
                'Channel A - Velocity': round_axis_data(-ps4.axis_data[1]),
                'Channel B - Pitch': round_axis_data(ps4.axis_data[2]),
                'Channel B - Velocity': round_axis_data(-ps4.axis_data[3]),
            }

            axis_values = {
                0: channel_values[Window.Window.joystick_assignments['Joy 1 X']],
                1: channel_values[Window.Window.joystick_assignments['Joy 1 Y']],
                2: channel_values[Window.Window.joystick_assignments['Joy 2 X']],
                3: channel_values[Window.Window.joystick_assignments['Joy 2 Y']]
            }

            print('-------------- axis_values')
            pprint(axis_values)
            print('-------------- Window.Window.joystick_assignments')
            pprint(Window.Window.joystick_assignments)
            print('--------------- Window.Window.channels')
            pprint(Window.Window.channels)
            print('------------------------------------')

            bsp.updateOutput(axis_values)

        elif button_change is True:
            bsp.send_gate_output(button_to_change, button_on)

        asyncio.get_event_loop().stop()


async def updater(tk_root, interval_time=.2):
    while True:
        print('updater run')
        # tk_root.update_idletasks()
        tk_root.update()
        # tk_root.mainloop()
        await asyncio.sleep(interval_time)


async def main(tk_root):
    ps4.init()

    # asyncio.create_task(updater(tk_root))
    asyncio.create_task(handle_ps4_events())
    threading.Thread.__init__(tk_root.mainloop())
    # asyncio.run()
    # threading.Thread.__init__(handle_ps4_events())



if __name__ == "__main__":
    root = Tk()
    print('root = Tk()')
    app = Window.Window(root)
    root.wm_title("ps4tomidi")

    asyncio.run(main(root))
