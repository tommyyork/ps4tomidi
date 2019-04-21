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
        channel_a_note_on = [0x90, axes[0], axes[1]]
        channel_b_note_on = [0x91, axes[2], axes[3]]
        self.midiout.send_message(channel_a_note_on)
        self.midiout.send_message(channel_b_note_on)

        time.sleep(.01)

        channel_a_note_off = [0x80, axes[0], axes[1]]
        channel_b_note_off = [0x81, axes[2], axes[3]]

        self.midiout.send_message(channel_a_note_off)
        self.midiout.send_message(channel_b_note_off)

    def send_gate_output(self, buttons, on):
        if buttons[4] is True:
            note = 36
        elif buttons[6] is True:
            note = 37
        elif buttons[5] is True:
            note = 38
        elif buttons[7] is True:
            note = 39
        else:
            note = 0

        if on is True:
            gate_channel_note_on = [0x92, note, 64]
            self.midiout.send_message(gate_channel_note_on)
        elif on is False:
            gate_channel_note_off_1 = [0x82, 36, 64]
            gate_channel_note_off_2 = [0x82, 37, 64]
            gate_channel_note_off_3 = [0x82, 38, 64]
            gate_channel_note_off_4 = [0x82, 39, 64]
            self.midiout.send_message(gate_channel_note_off_1)
            self.midiout.send_message(gate_channel_note_off_2)
            self.midiout.send_message(gate_channel_note_off_3)
            self.midiout.send_message(gate_channel_note_off_4)


