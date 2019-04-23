import time
import pygame
from rtmidi.midiutil import open_midiport


class BeatStepPro(object):
    def __init__(self):
        print('bsp init')
        self.midiout, self.port_out_name = open_midiport(
            -1,
            'output',
            client_name='bsp',
            port_name='bsp output_port'
        )

    def updateOutput(self, axes):
        channelANoteOn = [0x90, axes[0], axes[1]]
        channelBNoteOn = [0x91, axes[2], axes[3]]
        self.midiout.send_message(channelANoteOn)
        self.midiout.send_message(channelBNoteOn)
        print('sending midi messages: ', channelANoteOn, channelBNoteOn)

        time.sleep(.01)

        channel_a_note_off = [0x80, axes[0], axes[1]]
        channel_b_note_off = [0x81, axes[2], axes[3]]

        self.midiout.send_message(channel_a_note_off)
        self.midiout.send_message(channel_b_note_off)

    def send_gate_output(self, button, on):
        if button == 4:
            note = 36
        elif button == 6:
            note = 37
        elif button == 5:
            note = 38
        elif button == 7:
            note = 39
        else:
            note = 0

        if on is True:
            gate_channel_note_on = [0x92, note, 64]
            self.midiout.send_message(gate_channel_note_on)
        elif on is False:
            gate_channel_note_off = [0x82, note, 64]
            self.midiout.send_message(gate_channel_note_off)

    def handle_events(self, ps4, bsp):
        print('handle ps4 events called')

        while True:
            for event in pygame.event.get():
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
                    #
                    # axis_values = {
                    #     0: channel_values[Window.Window.joystick_assignments['Joy 1 X']],
                    #     1: channel_values[Window.Window.joystick_assignments['Joy 1 Y']],
                    #     2: channel_values[Window.Window.joystick_assignments['Joy 2 X']],
                    #     3: channel_values[Window.Window.joystick_assignments['Joy 2 Y']]
                    # }
                    #
                    # print('-------------- axis_values')
                    # pprint(axis_values)
                    # print('-------------- Window.Window.joystick_assignments')
                    # pprint(Window.Window.joystick_assignments)
                    # print('--------------- Window.Window.channels')
                    # pprint(Window.Window.channels)
                    # print('------------------------------------')

                    axis_values = channel_values

                    bsp.updateOutput(axis_values)

                elif button_change is True:
                    bsp.send_gate_output(button_to_change, button_on)

