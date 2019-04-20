import time
from rtmidi.midiutil import open_midiport


class BeatStepPro(object):

    axes = {0: 64,
            1: 64,
            2: 64,
            3: 64}

    def __init__(self):
        self.midiout, self.port_out_name = open_midiport(
            -1,
            'output',
            client_name='bsp',
            port_name='bsp output_port'
        )

    def updateAxes(self, newAxes):
        self.axes = newAxes

    def updateOutput(self):
        channelANoteOn = [0x90, self.axes[0], self.axes[1]]
        channelBNoteOn = [0x91, self.axes[2], self.axes[3]]
        self.midiout.send_message(channelANoteOn)
        self.midiout.send_message(channelBNoteOn)
        print('sending midi messages: ', channelANoteOn, channelBNoteOn)

        time.sleep(.01)

        channelANoteOff = [0x80, self.axes[0], self.axes[1]]
        channelBNoteOff = [0x81, self.axes[2], self.axes[3]]
        #
        self.midiout.send_message(channelANoteOff)
        self.midiout.send_message(channelBNoteOff)


