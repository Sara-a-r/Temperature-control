#define PIN_LM35 A0
#define PIN_TIP120 9

// setting desired temperature
float Tref = 25;
int ON = 1;
int OFF = 0;

void setup()
{
  // configure pin as input or output
  pinMode(PIN_LM35, INPUT);
  pinMode(PIN_TIP120, OUTPUT);
  analogReference(INTERNAL);
  Serial.begin(9600);
  Serial.flush();
}

void loop()
{
  // getting the voltage reading from the temperature sensor
  int reading = analogAvg(PIN_LM35);
  // convert the analog reading (0 to 1023) to Celsius
  float Troom = (reading * 110.0) /1024.0;
  
  // controlling T output
  if (Troom < Tref) {
    digitalWrite(PIN_TIP120, HIGH);
    Serial.print(ON);
    } else {
    digitalWrite(PIN_TIP120, LOW);
    Serial.print(OFF);
  }

  Serial.print("x");
  Serial.print(Troom);
  Serial.print("\n");
  
  // delay between readings
  delay(1000);
  
  Serial.flush();
  
}

// function to average readings (more stable)

int analogAvg(int sensorPin)
 {
 unsigned int total=0;
 for(int n=0; n<64; n++ )
    total += analogRead(PIN_LM35);
 return total/64;
 }
