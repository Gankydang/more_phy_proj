Moisture = 0
distance2 = 0
def on_forever():
    global Moisture, distance2
    while True:
        Moisture = pins.analog_read_pin(AnalogPin.P2)
        distance2 = grove.measure_in_centimeters_v2(DigitalPin.P0)
        if Moisture < 30:
            pins.digital_write_pin(DigitalPin.P1, 1)
        else:
            pins.digital_write_pin(DigitalPin.P1, 0)
        if distance2 < 2.1:
            basic.show_icon(IconNames.YES)
        else:
            basic.show_icon(IconNames.NO)
        
def on_button_pressed_a():
    on_forever()
input.on_button_pressed(Button.A, on_button_pressed_a)

