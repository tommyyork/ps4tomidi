import time
from pprint import pprint
from rtmidi.midiutil import open_midiport


class BeatStepPro(object):

    def __init__(self):
        self.midiout, self.port_out_name = open_midiport(
            -1,
            'output',
            client_name='bsp',
            port_name='bsp output_port'
        )

    def update_axis_output(self, axes):
        #
        # pprint(self.axis_data)
        # pprint(axes)

        channel_a_note_on = [0x90, axes[0], axes[1]]
        channel_b_note_on = [0x91, axes[2], axes[3]]
        self.midiout.send_message(channel_a_note_on)
        self.midiout.send_message(channel_b_note_on)
        print('sending CV/Velocity on channels A/B: ', channel_a_note_on, channel_b_note_on)

        time.sleep(.01)

        channel_a_note_off = [0x80, axes[0], axes[1]]
        channel_b_note_off = [0x81, axes[2], axes[3]]

        self.midiout.send_message(channel_a_note_off)
        self.midiout.send_message(channel_b_note_off)

    def send_gate_output(self, joypad):
        if joypad[0] == (-1, 0):
            note = 36
        elif joypad[0] == (0, -1):
            note = 37
        elif joypad[0] == (1, 0):
            note = 38
        elif joypad[0] == (0, 1):
            note = 39
        else:
            note = 0

        gate_channel_note_on = [0x92, note, 64]
        print('sending gate message', gate_channel_note_on)
        self.midiout.send_message(gate_channel_note_on)

        time.sleep(0.01)

        gate_channel_note_off = [0x82, note, 64]
        self.midiout.send_message(gate_channel_note_off)


