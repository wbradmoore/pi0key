# pi0key

This allows emulating a keyboard by plugging a pi zero w into a computer's usb port. Specifically, it allows the user to quickly define a series of keystrokes as a cli arg to the program.

Example:

```sudo python3 pi0key.py del,sleep:1,repeat:600```

Note that `sleep` instructions randomize the length of the sleep, distributed roughly around the value provided (in seconds).

Todo:
* nested repeats
* document getting pi 0 into state where it can emulate input device