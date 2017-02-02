//Uses TMP36
int sensorPin = 0;
 
void setup()
{
  Serial.begin(9600);
}
 
void loop()
{
 int reading = analogRead(sensorPin);  
 
 // converting reading to voltage for 5.0v arduino, for 3.3v arduino use 3.3
 float voltage = reading * 5.0;
 voltage /= 1024.0; 
 
 // calc the temperature in c
 float temperatureC = (voltage - 0.5) * 100 ;

 // convert to Fahrenheit
 float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;

 Serial.println(temperatureF);
 
 delay(2000); //wait 2 sec                 
}
