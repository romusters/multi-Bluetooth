//Code for a bluetooth module to work standalone

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

void rebootAT(bool nowait=false){
  Serial.println("Reboot in AT mode.");
  delay(1000);
  digitalWrite(voltPin, LOW);
  delay(100);
  digitalWrite(keyPin, HIGH);
  delay(100);
  digitalWrite(voltPin, HIGH);
  delay(1000);
  
  if(nowait){  
    rebootNormal();
  } else{
    delay(15000);
  }
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
     
      if(str == "a"){
        rebootAT();
      }
      
      if(str == "n"){ 
        rebootNormal();
      }
      
      if(str == "t"){
        rebootAT(true);
        Serial.write("AT+NAME=ROBERT\r\n");
        Serial.println("AT+NAME=ROBERT\r\n");
        delay(1000);
        rebootNormal();
      }
      
      Serial.print("Length of the string is: ");
      Serial.println(str.length());
     

      while(!Kr){
        str = readData();

        if(str == "Ks#"){
          while(true){
            Serial.print("End of message, message was: ");
            Serial.println(message);
          }
        }
        if(str.length() == 3){
          letter = str.charAt(2);
          //Serial.print("Received: ");
          //Serial.println(letter);
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
      delay(2000);

      while(!KrKsKr){
        str = readData();
        
        if(str.length() == 5){
          if(str.charAt(4) == letter){
            str = "";
            KrKsKr = true;
            delay(100);
          }
        }
        delay(100);
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
        delay(100);
        //Krnew = true; //REMOVE IN FUTURE
      }
      

    delay(1000);
    //Serial.println("Running");
}
