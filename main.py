Moisture = 0
distance2 = 0
a_pressed = False
b_pressed = False
def on_forever():
    global Moisture, distance2
    while True:
        Moisture = pins.analog_read_pin(AnalogPin.P2)
        distance2 = grove.measure_in_centimeters_v2(DigitalPin.P0)
        if input.button_is_pressed(Button.A):
            a_pressed = True
            b_pressed = False
        elif input.button_is_pressed(Button.B):
            b_pressed = True
            a_pressed = False
        if a_pressed:
            if Moisture < 30:
                pins.digital_write_pin(DigitalPin.P1, 1)
            else:
                pins.digital_write_pin(DigitalPin.P1, 0)
            if distance2 < 3.1:
                basic.show_icon(IconNames.HAPPY)
            else:
                basic.show_icon(IconNames.SAD)
        elif b_pressed:
            basic.clear_screen()
            pins.digital_write_pin(DigitalPin.P1, 0)
        

on_forever()

