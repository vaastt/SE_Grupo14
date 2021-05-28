#define LEDPIN 13
#define SENSORPIN 2
#define BUTTONPIN 3
#define PI_MOTIONPIN 8
#define PI_BUTTONPIN 12
int sensorState = 0, buttonState = 0;

void setup() {

  pinMode(LEDPIN, OUTPUT);

  pinMode(SENSORPIN, INPUT);

  pinMode(BUTTONPIN, INPUT);

  pinMode(PI_MOTIONPIN, OUTPUT);
  pinMode(PI_BUTTONPIN, OUTPUT);
  Serial.begin(9600);
  
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
    digitalWrite(PI_MOTIONPIN, HIGH);
    Serial.println("DETECTED");

    
    
  } else {

    digitalWrite(LEDPIN, LOW);
    digitalWrite(PI_MOTIONPIN, LOW);
    //Serial.println("NOT DETECTED");
  
  }
  
}

void verify_button() {
  
  if (buttonState == HIGH) {
    
    digitalWrite(LEDPIN, HIGH);
    digitalWrite(PI_BUTTONPIN, HIGH);
    Serial.println("BUTTON PRESSED");
    
  } else {
  
    digitalWrite(LEDPIN, LOW);
    digitalWrite(PI_BUTTONPIN, LOW);
  }
  
}
