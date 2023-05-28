/*
 * Firmata is a generic protocol for communicating with microcontrollers
 * from software on a host computer. It is intended to work with
 * any host computer software package.
 *
 * To download a host software package, please click on the following link
 * to open the list of Firmata client libraries in your default browser.
 *
 * https://github.com/firmata/arduino#firmata-client-libraries
 */

/* This firmware supports as many analog ports as possible, all analog inputs,
 * four PWM outputs, and two with servo support.
 *
 * This example code is in the public domain.
 */
#include <Servo.h>
#include <LiquidCrystal.h>
#include <Firmata.h>
#include <SharpIR.h>


/*==============================================================================
 * GLOBAL VARIABLES
 *============================================================================*/

#define IRPin A0
#define model 1080

SharpIR mySensor = SharpIR(IRPin, model);

/* servos */
Servo servo9, servo10; // one instance per pin
/* analog inputs */
int analogInputsToReport = 0; // bitwise array to store pin reporting
int analogPin = 0; // counter for reading analog pins

/* timer variables */
unsigned long currentMillis;     // store the current value from millis()
unsigned long previousMillis;    // for comparison with currentMillis

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

// setup Firmata variables, communication
int lastLine = 1;


/*==============================================================================
 * FUNCTIONS
 *============================================================================*/




void stringDataCallback(char *stringData){
   if ( lastLine ) {
     lastLine = 0;
     lcd.clear();
   } else {
     lastLine = 1;
     lcd.setCursor(0,1);
   }
   lcd.print(stringData);
}


void analogWriteCallback(byte pin, int value)
{
  switch (pin) {
    case 9: servo9.write(value); break;
    case 10: servo10.write(value); break;
    case 3:
    case 5:
    case 6:
    case 11: // PWM pins
      analogWrite(pin, value);
      break;
  }
}
// -----------------------------------------------------------------------------
// sets bits in a bit array (int) to toggle the reporting of the analogIns
void reportAnalogCallback(byte pin, int value)
{
  if (value == 0) {
    analogInputsToReport = analogInputsToReport & ~ (1 << pin);
  }
  else { // everything but 0 enables reporting of that pin
    analogInputsToReport = analogInputsToReport | (1 << pin);
  }
  // TODO: save status to EEPROM here, if changed
}

/*==============================================================================
 * SETUP()
 *============================================================================*/
void setup()
{
  
  Firmata.setFirmwareVersion( FIRMATA_MAJOR_VERSION, FIRMATA_MINOR_VERSION );
  Firmata.attach(ANALOG_MESSAGE, analogWriteCallback);
  Firmata.attach(REPORT_ANALOG, reportAnalogCallback);
  Firmata.attach( STRING_DATA, stringDataCallback);

  lcd.begin(16,2);
  servo9.attach(9);
  servo10.attach(10);
  Firmata.begin(57600);

  Serial.begin(9600);
}

/*==============================================================================
 * LOOP()
 *============================================================================*/
void loop()
{

  Serial.print("Mean distance: ");
  Serial.print(distance_cm);
  Serial.println(" cm");

  while (Firmata.available())
    Firmata.processInput();
  currentMillis = millis();
  if (currentMillis - previousMillis > 20) {
    previousMillis += 20;                   // run this every 20ms
    for (analogPin = 0; analogPin < TOTAL_ANALOG_PINS; analogPin++) {
      if ( analogInputsToReport & (1 << analogPin) )
        Firmata.sendAnalog(analogPin, analogRead(analogPin));
    }
  }
}

