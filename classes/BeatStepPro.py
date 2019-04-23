import time
from rtmidi.midiutil import open_midiport


class BeatStepPro(object):
    def __init__(self):
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

