Moisture = 0

def on_button_pressed_a():
    pins.digital_write_pin(DigitalPin.P1, 1)
    basic.pause(999999999)
    pins.digital_write_pin(DigitalPin.P1, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Moisture
    Moisture = pins.analog_read_pin(AnalogPin.P2)
    basic.show_string("" + str(Moisture))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global Moisture
    Moisture = pins.analog_read_pin(AnalogPin.P2)
    if Moisture < 190000000:
        pins.digital_write_pin(DigitalPin.P1, 1)
        basic.pause(9999999999)
        pins.digital_write_pin(DigitalPin.P1, 0)
    basic.pause(5000)
basic.forever(on_forever)
