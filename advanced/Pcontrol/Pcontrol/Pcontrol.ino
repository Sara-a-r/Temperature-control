#define PIN_LM35 A0
#define PIN_TIP120 9

// setting desired temperature
float Tref = 24;

// define P parameters
int kp = 120;
float error = 0;
float T_input;
int P_value;

void setup()
{
  // configure pin as input or output
  pinMode(PIN_LM35, INPUT);
  pinMode(PIN_TIP120, OUTPUT);
  // use the internal supply 1.1V
  analogReference(INTERNAL);
  Serial.begin(9600);
  Serial.flush();
}

void loop()
{ 
  // getting the voltage reading from the temperature sensor
  int reading = analogAvg(PIN_LM35);
  // convert the analog reading (0 to 1023) to Celsius
  T_input = (reading * 110.0) /1024.0;

  // calculate the error between the setpoint and the read value
  error = Tref - T_input;
  // calculate the P value
  P_value = kp * error;

  // define PWM range between 0 and 255
  if(P_value < 0) {P_value = 0;}
  if(P_value > 255) {P_value = 255;}
  
  // write the PWM signal to the transistor
  analogWrite(PIN_TIP120,P_value);
 
  Serial.print(T_input);
  Serial.print("x");
  Serial.print(P_value);
  Serial.print("x");
  Serial.println(error);

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
