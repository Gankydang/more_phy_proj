let Moisture = 0
input.onButtonPressed(Button.A, function () {
    servos.P0.run(55)
})
input.onButtonPressed(Button.B, function () {
    Moisture = pins.analogReadPin(AnalogPin.P2)
    basic.showString("" + Moisture)
})
basic.forever(function () {
    Moisture = pins.analogReadPin(AnalogPin.P2)
    if (Moisture < 10) {
        pins.digitalWritePin(DigitalPin.P1, 1)
        basic.pause(1000)
        pins.digitalWritePin(DigitalPin.P1, 0)
    }
})
