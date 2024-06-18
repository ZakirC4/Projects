#include <Adafruit_LiquidCrystal.h>
// #include <LiquidCrystal.h>

#define SPEAKER 8
#define TRIG 9
#define ECHO 10

Adafruit_LiquidCrystal lcd(0);
// LiquidCrystal lcd(7, 6, 5, 4, 3, 2);

int duration, distance;

void setup() {
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  lcd.begin(16, 2);
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
    tone(SPEAKER, 1000);
  } else {
    noTone(SPEAKER);
  }


  lcd.setCursor(0, 1);
  lcd.print(distance);
  lcd.print(" cm");

  delay(500);
}
