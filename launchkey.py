import mido

# device name
output_name = "MIDIOUT2 (Launchkey Mini) 2"

# led id's
row1 = (96,     97,     98,     99,     100,    101,    102,    103)
row2 = (112,    113,    114,    115,    116,    117,    118,    119)
# round led id's
top_rled = 104
bottom_rled = 120

# wrapper for launchkey midi communication
# (only implements what's currently needed by the scripts)


class Launchkey:
    def __init__(self):
        print("connecting to launchkey")
        self.midi_out = mido.open_output(output_name)
        self.midi_out.send(mido.Message.from_bytes([0x90, 0x0C, 0x7F]))
        print("connected")

        self.rows = [row1, row2]
        self.leds = row1 + row2
        self.top_rled = top_rled
        self.bottom_rled = bottom_rled

    def disconnect(self):
        print("disconnecting from launchkey")
        self.midi_out.send(mido.Message.from_bytes([0x90, 0x0C, 0x00]))
        self.midi_out.close()

    # light up a led with a color ID
    def led(self, id, color):
        self.midi_out.send(mido.Message('note_on', channel=0,
                                        note=id, velocity=color))

    # light up a led given two color amounts
    def led_green_red(self, id, green, red):
        green = min(green, 4)
        red = min(red, 4)
        color = red + (green * 16)
        self.midi_out.send(mido.Message('note_on', channel=0,
                                        note=id, velocity=color))

    # turn off all leds
    def clear_leds(self):
        for led in self.leds:
            self.led(led, 0)
