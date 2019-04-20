from classes import BeatStepPro
from classes import PS4Controller

ps4 = PS4Controller.PS4Controller()
BeatStepPro = BeatStepPro.BeatStepPro()

# print(ps4)
# print(BeatStepPro)

ps4.init()
ps4.listen()