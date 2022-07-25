let distance = 0
basic.forever(function on_forever() {
    let Moisture = pins.analogReadPin(AnalogPin.P2)
    let distance = grove.measureInCentimetersV2(DigitalPin.P0)
    basic.showNumber(distance)
    if (Moisture < 10) {
        pins.digitalWritePin(DigitalPin.P1, 1)
    } else {
        pins.digitalWritePin(DigitalPin.P1, 0)
    }
    
})
