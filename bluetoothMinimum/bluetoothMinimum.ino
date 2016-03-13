//Code to run arduino over USB to send AT commands from serial monitor

int voltPin = 8;
int keyPin = 9; 

void setup() {
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  digitalWrite(8, HIGH);
  delay(100);
  digitalWrite(9, LOW);
  delay(2000);
  digitalWrite(voltPin, LOW);
  delay(100);
  digitalWrite(keyPin, HIGH);
  delay(100);
  digitalWrite(voltPin, HIGH);

}

void loop() {

}
