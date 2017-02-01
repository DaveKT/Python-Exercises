
String output = "";

void setup() {
  Serial.begin(9600); 
}

void loop() {
  // put your main code here, to run repeatedly:
  int x = 1;
  while (true) {
    long randomnumber = random(20);
    output = x;
    output = output + ",";
    output = output + randomnumber;
    Serial.println(output);
    x++;
    delay(500);
  }

}
