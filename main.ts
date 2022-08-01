let Moisture = 0
let distance2 = 0
function on_forever() {
    
    while (true) {
        Moisture = pins.analogReadPin(AnalogPin.P2)
        distance2 = grove.measureInCentimetersV2(DigitalPin.P0)
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
        
    }
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    on_forever()
})
