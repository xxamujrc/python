#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x20, 16, 2); // for actual

int temp = 0;
int hum = 0;
int ph = 0;
int tds = 0;
void setup()
{
    Serial.begin(9600);
    pinMode(A0, INPUT);
    pinMode(A1, INPUT);
    pinMode(A2, INPUT);
    pinMode(A3, INPUT);
    pinMode(7, OUTPUT);
    pinMode(6, OUTPUT);
    pinMode(5, OUTPUT);
    pinMode(13, OUTPUT);
    pinMode(12, OUTPUT);

    lcd.init();
    lcd.backlight();
    //
    lcd.setCursor(6, 0);
    lcd.print("RTMS");
    lcd.setCursor(3, 1);
    lcd.print("Amurao, JRC");
    delay(2000);
    lcd.clear();
    //
    lcd.setCursor(0, 0);
    lcd.print("temp: ");
    //
    lcd.setCursor(0, 1);
    lcd.print("hum: ");
    //
    lcd.setCursor(8, 0);
    lcd.print("ph: ");
    //
    lcd.setCursor(8, 1);
    lcd.print("tds: ");
}
void loop()
{
    // sysData(data);
    int temp = map(analogRead(A0), 0, 1023, 20, 40);
    int hum = map(analogRead(A1), 0, 1023, 0, 100);
    int ph = map(analogRead(A2), 0, 1023, 0, 14);
    int tds = map(analogRead(A3), 0, 1023, 0, 3000);

    if ((temp) > 32)
        digitalWrite(7, 1);
    if ((temp) > 32)
        digitalWrite(13, 1);
    if ((temp) < 31)
        digitalWrite(7, 0);
    if ((temp) < 31)
        digitalWrite(13, 0);
    //
    if ((hum) > 71)
        digitalWrite(5, 1);
    if ((hum) < 70)
        digitalWrite(5, 0);
    //
    if ((ph) < 8)
        digitalWrite(6, 1);
    if ((ph) < 8)
        digitalWrite(12, 1);
    if ((ph) > 7)
        digitalWrite(6, 0);
    if ((ph) > 7)
        digitalWrite(12, 0);

    Serial.print(temp);
    Serial.print(','); // CSV
    Serial.print(hum);
    Serial.print(',');
    Serial.print(ph);
    Serial.print(',');
    Serial.println(tds); // <CR><LF>
    delay(200);
    lcd.setCursor(5, 0);
    lcd.print(temp);
    lcd.print(" ");
    delay(100);
    //
    lcd.setCursor(5, 1);
    lcd.print(hum);
    lcd.print(" ");
    delay(100);
    //
    lcd.setCursor(12, 0);
    lcd.print(ph);
    lcd.print(" ");
    delay(100);
    //
    lcd.setCursor(12, 1);
    lcd.print(tds);
    lcd.print(" ");
    delay(100);
}
