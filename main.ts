let Moisture = 0
let distance2 = 0
let a_pressed = false
let b_pressed = false
function on_forever() {
    let a_pressed: boolean;
    let b_pressed: boolean;
    
    while (true) {
        Moisture = pins.analogReadPin(AnalogPin.P2)
        distance2 = grove.measureInCentimetersV2(DigitalPin.P0)
        if (input.buttonIsPressed(Button.A)) {
            a_pressed = true
            b_pressed = false
        } else if (input.buttonIsPressed(Button.B)) {
            b_pressed = true
            a_pressed = false
        }
        
        if (a_pressed) {
            if (Moisture < 30) {
                pins.digitalWritePin(DigitalPin.P1, 1)
            } else {
                pins.digitalWritePin(DigitalPin.P1, 0)
            }
            
            if (distance2 < 2.1) {
                basic.showIcon(IconNames.Yes)
            } else {
                basic.showIcon(IconNames.No)
            }
            
        } else if (b_pressed) {
            basic.clearScreen()
            pins.digitalWritePin(DigitalPin.P1, 0)
        }
        
    }
}

on_forever()
