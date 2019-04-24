import asyncio
import pygame
import wx
from wxasync import AsyncBind, WxAsyncApp, StartCoroutine

from classes import BeatStepPro
from classes import PS4Controller

ps4 = PS4Controller.PS4Controller()
bsp = BeatStepPro.BeatStepPro()

async def main():
    ps4.init()
    asyncio.create_task(handle_ps4_events())

class TestFrame(wx.Frame):
    def __init__(self, parent=None):
        super(TestFrame, self).__init__(parent)
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        #
        # vbox.Add(self.display, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)
        #
        # gs = wx.FlexGridSizer(4, 2, 15, 15)
        #
        # a1 = wx.StaticText()
        #
        # gs.AddMany( [(wx.Button(self, label='Cls'), 0, wx.EXPAND),
        #     (wx.Button(self, label='Bck'), 0, wx.EXPAND),
        #     (wx.StaticText(self), wx.EXPAND),
        #     (wx.Button(self, label='Close'), 0, wx.EXPAND),
        #     (wx.Button(self, label='7'), 0, wx.EXPAND),
        #     (wx.Button(self, label='8'), 0, wx.EXPAND),
        #     (wx.Button(self, label='9'), 0, wx.EXPAND),
        #     (wx.Button(self, label='/'), 0, wx.EXPAND),
        #     (wx.Button(self, label='4'), 0, wx.EXPAND),
        #     (wx.Button(self, label='5'), 0, wx.EXPAND),
        #     (wx.Button(self, label='6'), 0, wx.EXPAND),
        #     (wx.Button(self, label='*'), 0, wx.EXPAND),
        #     (wx.Button(self, label='1'), 0, wx.EXPAND),
        #     (wx.Button(self, label='2'), 0, wx.EXPAND),
        #     (wx.Button(self, label='3'), 0, wx.EXPAND),
        #     (wx.Button(self, label='-'), 0, wx.EXPAND),
        #     (wx.Button(self, label='0'), 0, wx.EXPAND),
        #     (wx.Button(self, label='.'), 0, wx.EXPAND),
        #     (wx.Button(self, label='='), 0, wx.EXPAND),
        #     (wx.Button(self, label='+'), 0, wx.EXPAND) ])
        #
        # vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        # self.SetSizer(vbox)
        # self.Layout()



async def handle_ps4_events():
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
            print('got joy button down event')
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
                0: channel_values[ps4.joystick_assignments['Joy 1 X']],
                1: channel_values[ps4.joystick_assignments['Joy 1 Y']],
                2: channel_values[ps4.joystick_assignments['Joy 2 X']],
                3: channel_values[ps4.joystick_assignments['Joy 2 Y']]
            }

            bsp.updateOutput(axis_values)

        elif button_change is True:
            bsp.send_gate_output(button_to_change, button_on)

        asyncio.get_event_loop().stop()


if __name__ == "__main__":
    app = WxAsyncApp()
    frame = TestFrame()
    frame.Show()
    app.SetTopWindow(frame)

    asyncio.run(main())
