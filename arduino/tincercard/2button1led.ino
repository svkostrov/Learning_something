
#include "Arduino.h"


#define ledpin 5
#define butpin1 4
#define butpin2 3
boolean btnstate1now;
boolean btnstate2now;
boolean btnstatebefore;
boolean ledstate;
unsigned long las_press;



void setup() 
{
    pinMode(5, OUTPUT);
  	pinMode(4, INPUT_PULLUP);
  	pinMode(3, INPUT_PULLUP);
  	Serial.begin(9600);
    
}

void loop() 
{
  
 btnstate1now= digitalRead(butpin1);
 btnstate2now= digitalRead(butpin2);
 ledstate= digitalRead(ledpin);
 
  
  if (btnstate1now == LOW && millis() - las_press > 50){
    Serial.println("Pressed 1");
    ledstate = HIGH;
    digitalWrite(ledpin, ledstate);
    las_press = millis();
  }
  if (btnstate2now == LOW && millis() - las_press > 50){
    Serial.println("Pressed 2");
    ledstate = LOW;
    digitalWrite(ledpin, ledstate);
    las_press = millis();
  }
  
  // btnstatebefore= btnstatenow;
}


