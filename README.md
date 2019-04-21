# ps4tomidi
PS4 controller interface to send control voltage through a midi2cv adapter

Currently set up to send pitch/velocity CV on channels 1 and 2 for the left and righthand joysticks of a PS4 controller. This gives you unipolar CV on a BeatStepPro, or perhaps bipolar CV on a midi2cv controller that supports bipolar standards (-5v to 5v volt/octave).

Should be able to `pip install` then just `python demo.py`. It'll ask you what midi interface to use, then you can go from there.

Helped by this cool Euclidean Rhythm project from [OctoEuclid](https://github.com/rupa/octoeuclid) and this Python / PS4 controller [class](https://gist.github.com/claymcleod/028386b860b75e4f5472) from [claymcleod](https://gist.github.com/claymcleod).
