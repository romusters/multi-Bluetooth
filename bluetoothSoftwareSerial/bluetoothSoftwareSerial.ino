//Code which is not working because I think the library below does not work with the bluetooth module

#include <SoftwareSerial.h>

int rx = 10;
int tx = 11;

SoftwareSerial BTSerial(rx, tx); // RX | TX


int voltPin = 8;
int keyPin = 9;

void setup() {
  Serial.begin(38400);

  pinMode(voltPin, OUTPUT);
  pinMode(keyPin, OUTPUT);
  digitalWrite(voltPin, LOW);
  delay(100);
  digitalWrite(keyPin, LOW);
  delay(100);
  digitalWrite(voltPin, HIGH); 
  delay(100);

}

void rebootNormal(){
  Serial.println("Reboot in normal mode.");
  delay(1000);
  digitalWrite(voltPin, LOW);
  delay(1000);
  digitalWrite(keyPin, LOW);
  delay(1000);
  digitalWrite(voltPin, HIGH);
  delay(1000);
}

void rebootAT(){
  Serial.println("Reboot in AT mode.");
  delay(1000);
  digitalWrite(voltPin, LOW);
  delay(100);
  digitalWrite(keyPin, HIGH);
  delay(100);
  digitalWrite(voltPin, HIGH);
  delay(1000);
  
}


String str = "";
    

void loop() {
    if(Serial.available() > 0){  
      delay(3);
      while (Serial.available () > 0) {
        str += char(Serial.read ());
      }
      str.trim();
      Serial.println(str);
      
      if(str == "a"){
        rebootAT();
      }
      
      if(str == "n"){ 
        rebootNormal();
      }
      
      if(str == "t"){
        rebootAT();
        Serial.write("AT+NAME=ROBERT\r\n");
        delay(1000);
        rebootNormal();
      }
      str = "";
    }
    delay(1000);
    Serial.println("Running");
}
