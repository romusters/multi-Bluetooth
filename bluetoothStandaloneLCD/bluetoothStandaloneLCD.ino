// code for LCD
#include <Wire.h>
#include <Adafruit_RGBLCDShield.h>
#include <utility/Adafruit_MCP23017.h>
#define WHITE 0x7
Adafruit_RGBLCDShield lcd = Adafruit_RGBLCDShield();

//Code for a bluetooth module to work standalone
int voltPin = 8;
int keyPin = 9;

//Time to send an acknowledgement, if this is lower then the response time from the sender, the sender will send less acknowledgements
int t = 100;

void setup() {
  Serial.begin(38400);
  lcd.begin(16, 2);
  lcd.print("MAS is awesome!");
  lcd.setBacklight(WHITE);
  pinMode(voltPin, OUTPUT);//Code for a bluetooth module to work standalone
  pinMode(keyPin, OUTPUT);
  digitalWrite(voltPin, LOW);
  delay(100);
  digitalWrite(keyPin, LOW);
  delay(100);
  digitalWrite(voltPin, HIGH); 
  delay(100);
  Serial.println("Start listening");
}


String readData(){
  String str = "";
  if(Serial.available() > 0){  
    delay(3);
    while (Serial.available () > 0) {
      str += char(Serial.read ());
    }
  }
  str.trim();
  return str;
}


String str = "";
char letter;   
int i = 0;
bool Kr = false;
bool KrKsKr = false;
bool Krnew = false;

String message = "";

void loop() {
    
      while(!Kr){
        str = readData();
        
        // Listen for special endline character
        if(str == "Ks#"){
          Serial.print("End of message, message was: ");
          lcd.begin(16, 2);
          lcd.print(message);
          Serial.println(message);
          while(true){
            //To stop the process
          }
        }
        
        if(str.length() == 3){
          letter = str.charAt(2);
          Serial.write("Kr");
          Serial.write(letter);
          Serial.write("\r\n");
          str = "";
          Kr = true;
          Krnew = false;
          delay(100);
        }
        delay(100);
      }
      delay(t);

      while(!KrKsKr){
        str = readData();
        
        if(str.length() == 5){
          if(str.charAt(4) == letter){
            str = "";
            KrKsKr = true;
            delay(100);
          }
        }
        delay(t);
      }
      
      while(!Krnew){
        Serial.write("KrKsKr");
        Serial.write(letter);
        Serial.write("\r\n");
        delay(10);
        str = readData();
        if(str.length() == 3) {
          message += letter;
          letter = str.charAt(2);
          Krnew = true;
          i += 1;
          Serial.println("New letter received");
          Kr = false;
          KrKsKr = false;
          delay(100);
        }
        delay(t);
      }
      
    delay(1000);
}
