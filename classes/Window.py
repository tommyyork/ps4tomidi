import tkinter as tk


class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.frame = tk.Frame(self.master)
        choices = { 'Channel A - Pitch', 'Channel A - Velocity', 'Channel B - Pitch', 'Channel B - velocity' }

        joy1_x_setting = tk.StringVar(master)
        joy1_x_setting.set('Channel A - Pitch')

        popupMenu_joy1_y = tk.OptionMenu(master, joy1_x_setting, *choices)
        popupMenu_joy1_y.grid(column=1, row=0)

        joy1_y_setting = tk.StringVar(master)
        joy1_y_setting.set('Channel A - Velocity')

        popupMenu_joy2_x = tk.OptionMenu(master, joy1_y_setting, *choices)
        popupMenu_joy2_x.grid(column=1, row=1)

        joy2_x_setting = tk.StringVar(master)
        joy2_x_setting.set('Channel B - Pitch')

        popupMenu_joy2_y = tk.OptionMenu(master, joy2_x_setting, *choices)
        popupMenu_joy2_y.grid(column=1, row=2)

        joy2_y_setting = tk.StringVar(master)
        joy2_y_setting.set('Channel B - Velocity')

        popupMenu_joy2_y = tk.OptionMenu(master, joy2_y_setting, *choices)
        popupMenu_joy2_y.grid(column=1, row=3)

        # listbox2 = tk.Listbox(master)
        # for item in ["one", "two", "three", "four"]:
        #     listbox2.insert(tk.END, item)
        # listbox2.grid(column=1, row=1)
        #
        # # on change dropdown value
        # def change_dropdown(*args, tkvar):
        #     print(tkvar.get())
        #
        # # link function to change dropdown
        # joy1_x_setting.trace('w', change_dropdown)
        # joy1_y_setting.trace('w', change_dropdown)
        # joy2_x_setting.trace('w', change_dropdown)
        # joy2_y_setting.trace('w', change_dropdown)

        label_joy1_x = tk.Label(master, text="Joy1 X")
        label_joy1_x.grid(column=0, row=0)

        label_joy1_y = tk.Label(master, text="Joy1 Y")
        label_joy1_y.grid(column=0, row=1)

        label_joy2_x = tk.Label(master, text="Joy2 X")
        label_joy2_x.grid(column=0, row=2)

        label_joy2_y = tk.Label(master, text="Joy2 Y")
        label_joy2_y.grid(column=0, row=3)
        #
        # label_l1 = tk.Label(master, text="L1 Trigger")
        # label_l1.grid(column=0, row=4)
        #
        # label_l2 = tk.Label(master, text="L2 Trigger")
        # label_l2.grid(column=0, row=5)
        #
        # label_r1 = tk.Label(master, text="R1 Trigger")
        # label_r1.grid(column=0, row=6)
        #
        # label_r2 = tk.Label(master, text="R2 Trigger")
        # label_r2.grid(column=0, row=7)

        button = tk.Button(master, text="QUIT", command=master.quit)
        button.grid()

