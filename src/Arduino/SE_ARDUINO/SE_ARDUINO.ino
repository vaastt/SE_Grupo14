#define LEDPIN 13
#define SENSORPIN 2
#define BUTTONPIN 3
//#include <SoftwareSerial.h>

//SoftwareSerial piSer(7,8);
int sensorState = 0, buttonState = 0;

void setup() {

  pinMode(LEDPIN, OUTPUT);

  pinMode(SENSORPIN, INPUT);

  pinMode(BUTTONPIN, INPUT);


  Serial.begin(9600);
  //piSer.begin(9600);
}

void loop() {

  sensorState = digitalRead(SENSORPIN); 

  if(buttonState != HIGH)
    verify_sensor();

  buttonState = digitalRead(BUTTONPIN); 

  if(sensorState != HIGH)
    verify_button();


}

void verify_sensor() {
  if(sensorState == HIGH) {   
    
    digitalWrite(LEDPIN, HIGH);

    Serial.println("MOTION_DETECTED");
    //piSer.println("MD");
    delay(1000);
    
  } else {

    digitalWrite(LEDPIN, LOW);

    //Serial.println("MOTION_NOT_DETECTED");
  
  }
  
}

void verify_button() {
  if (buttonState == HIGH) {
    
    digitalWrite(LEDPIN, HIGH);

    Serial.println("BUTTON_PRESSED");
    //piSer.println("BP");
    delay(1000);
  } else {
    digitalWrite(LEDPIN, LOW);
  }
  
}
