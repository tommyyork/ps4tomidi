import tkinter as tk


class Window(tk.Frame):

    cv_outputs = {
        0: 'Channel A - Pitch',
        1: 'Channel A - Velocity',
        2: 'Channel B - Pitch',
        3: 'Channel B - Velocity'
    }

    joystick_assignments = {}

    menus = {}
    labels = {}

    def __init__(self, master=None):
        print(list(self.cv_outputs.values()))

        tk.Frame.__init__(self, master)
        self.master = master
        self.frame = tk.Frame(self.master)

        for idx, val in enumerate(['Joy 1 X', 'Joy 1 Y', 'Joy 2 X', 'Joy 2 Y']):
            self.joystick_assignments[val] = tk.StringVar(master)
            self.joystick_assignments[val].set(self.cv_outputs[idx])

            self.menus[val] = tk.OptionMenu(master, self.joystick_assignments[val], *list(self.cv_outputs.values()))
            self.menus[val].grid(column=1, row=idx)

            self.labels[val] = tk.Label(master, text=val)
            self.labels[val].grid(column=0, row=idx)

        button = tk.Button(master, text="QUIT", command=master.quit)
        button.grid()

