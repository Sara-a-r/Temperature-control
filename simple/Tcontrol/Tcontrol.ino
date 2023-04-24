#define PIN_LM35 A0

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  // getting the voltage reading from the temperature sensor
  int reading = analogRead(PIN_LM35);
  // convert the analog reading (0 to 1023) to Celsius
  float Troom = (reading * 500.0) /1024.0;
  // getting Arduino Temperature
  float Tref = GetTemp();
  
  // controlling T output
  float Tcontrol = Troom;
  float error = Tref - Tcontrol;

  if (Tcontrol != Tref) {
    Tcontrol = Tcontrol + error;
    }

  Serial.print(Tcontrol);
  Serial.print("x");
  Serial.print(Tref);
  Serial.print("x");
  Serial.print(Troom);
  Serial.print("\n");
  // delay between readings
  delay(1000);
}


//------------------------------------------------------------
// Function to get T from the internal temperature sensor
// ATmega 328 type

double GetTemp(void)
{
  unsigned int wADC;
  double t;

  // The internal temperature has to be used
  // with the internal reference of 1.1V.
  // Channel 8 can not be selected with
  // the analogRead function yet.

  // Set the internal reference and mux.
  ADMUX = (_BV(REFS1) | _BV(REFS0) | _BV(MUX3));
  ADCSRA |= _BV(ADEN);  // enable the ADC

  delay(20);            // wait for voltages to become stable.

  ADCSRA |= _BV(ADSC);  // Start the ADC

  // Detect end-of-conversion
  while (bit_is_set(ADCSRA,ADSC));

  // Reading register "ADCW" takes care of how to read ADCL and ADCH.
  wADC = ADCW;

  // The offset of 324.31 could be wrong. It is just an indication.
  t = (wADC - 324.31 ) / 1.22;

  // The returned temperature is in degrees Celcius.
  return (t);
}
