#include <LiquidCrystal.h>

#define TRIG 9
#define ECHO 10
#define SPEAKER 8

LiquidCrystal lcd(7, 6, 5, 4, 3, 2);

int duration, distance;

void setup() {
  lcd.begin(16, 2);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  lcd.print("Distance: ");
  lcd.setCursor(0, 1);
}

void loop() {
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  duration = pulseIn(ECHO, HIGH);
  distance = duration / 29.1 / 2;

  if (distance <= 10) {
    tone(SPEAKER, 10000);
  } else {
    noTone(SPEAKER);
  }


  lcd.setCursor(0, 1);
  lcd.print(distance);
  lcd.print(" cm");

  delay(1000);
}