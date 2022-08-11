def on_forever():
    while True:
        Moisture = pins.analog_read_pin(AnalogPin.P2)
        distance2 = grove.measure_in_centimeters_v2(DigitalPin.P0)
        
        if input.button_is_pressed(Button.A):
            a_pressed = True
            b_pressed = False
        elif input.button_is_pressed(Button.B):
            b_pressed = True
            a_pressed = False
            
        if a_pressed: # Activate the water pump if button A is pressed
            if Moisture < 30: # Start pumping water if the moisture is below a certain level
                pins.digital_write_pin(DigitalPin.P1, 1)
            else:
                pins.digital_write_pin(DigitalPin.P1, 0)
                
            if distance2 < 3.34: # Displays smiley face if there is water in the water pump
                basic.show_icon(IconNames.HAPPY)
            else: # If not, display sad face
                basic.show_icon(IconNames.SAD)
                
        elif b_pressed: # Deactivate the water pump if button B is pressed
            basic.clear_screen()
            pins.digital_write_pin(DigitalPin.P1, 0)
        

on_forever()

