import time

from rtmidi.midiutil import open_midiport


class BeatStepPro(object):

    def __init__(self):
        self.midiin, self.port_in_name = open_midiport(
            -1,
            'input',
            client_name='bsp',
            port_name='bsp input_port'
        )
        self.midiin.ignore_types(timing=False)
        self.midiout, self.port_out_name = open_midiport(
            -1,
            'output',
            client_name='bsp',
            port_name='bsp output_port'
        )

    def play_c(self):
        note_on = [0x90, 60, 112]  # channel 1, middle C, velocity 112
        note_off = [0x80, 60, 0]
        self.midiout.send_message(note_on)
        time.sleep(0.15)
        self.midiout.send_message(note_off)