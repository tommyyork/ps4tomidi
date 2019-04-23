import tkinter as tk
from functools import partial
from pprint import pprint


class Window(tk.Frame):

    channels = {
        'Channel A - Pitch': {
            'midi_channel': 0x90,
            'output_value': 64,
        },
        'Channel A - Velocity': {
            'midi_channel': 0x90,
            'output_value': 64,
        },
        'Channel B - Pitch': {
            'midi_channel': 0x91,
            'output_value': 64,
        },
        'Channel B - Velocity': {
            'midi_channel': 0x91,
            'output_value': 64,
        }
    }

    joystick_assignments = {
        'Joy 1 X': 'Channel A - Pitch',
        'Joy 1 Y': 'Channel A - Velocity',
        'Joy 2 X': 'Channel B - Pitch',
        'Joy 2 Y': 'Channel B - Velocity'
    }

    menu_names = joystick_assignments.keys()
    menu_string_vars = {}

    menus = {}
    labels = {}

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.frame = tk.Frame(self.master)

        for idx, val in enumerate(self.menu_names):
            self.menu_string_vars[val] = tk.StringVar(master)
            self.menu_string_vars[val].set(self.joystick_assignments[val])

            self.menus[val] = tk.OptionMenu(
                master,
                self.menu_string_vars[val],
                *list(self.joystick_assignments.values())
            )
            self.menus[val].grid(column=1, row=idx)

            self.labels[val] = tk.Label(master, text=val)
            self.labels[val].grid(column=0, row=idx)

            self.menu_string_vars[val].trace('w', partial(self.change_dropdown, val, self.joystick_assignments))

        button = tk.Button(master, text="QUIT", command=master.quit)
        button.grid()

    def change_dropdown(self, val, joystick_assignments, *args):
        joystick_assignments[val] = (self.menu_string_vars[val].get())
        pprint(joystick_assignments)
