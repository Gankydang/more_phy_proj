distance = 0

def on_forever():
    Moisture = pins.analog_read_pin(AnalogPin.P2)
    distance = grove.measure_in_centimeters_v2(DigitalPin.P0)
    basic.show_number(distance)
    if Moisture < 10:
        pins.digital_write_pin(DigitalPin.P1, 1)
    else:
        pins.digital_write_pin(DigitalPin.P1, 0)
basic.forever(on_forever)
