int ldr0 = A4;
int ldr1 = A1;
int ldr2 = A2;
int ldr3 = A3;

int value0 = 0;
int value1 = 0;
int value2 = 0;
int value3 = 0;

//            -------- Vertical  ----------- --------- Horizontal -------
//            LSB                         MSB LSB                     MSB
int pin[16] = {23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53};

void servo(int vertical, int horizontal) {
  //  vertical += 10;
  //  horizontal += 10;

  for (int i = 0; i < 8; i++) {
    digitalWrite(pin[i], vertical % 2);
    vertical = (vertical - (vertical % 2)) / 2;
  }
  for (int i = 0; i < 8; i++) {
    digitalWrite(pin[i + 8], horizontal % 2);
    horizontal = (horizontal - (horizontal % 2)) / 2;
  }
  Serial.println();
}

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 16; i++)
    pinMode(pin[i], OUTPUT);

  pinMode(ldr0, INPUT);
  pinMode(ldr1, INPUT);
  pinMode(ldr2, INPUT);
  pinMode(ldr3, INPUT);

}
int my_speed_x = 1;
int my_speed_y = 1;
int my_x = 0;
int my_y = 0;
void loop() {

//servo(30, 90);

      servo(my_y, my_x);
      my_x += 1*my_speed_x;
      my_y += 1*my_speed_y;
      if (my_x == 0 || my_x == 160) my_speed_x *= -1;
      if (my_y == 0 || my_y == 130) my_speed_y *= -1;
      delay(175);
      Serial.print("vertical: ");
      Serial.print(my_y);
      Serial.print(", horizontal: ");
      Serial.print(my_x);
      Serial.println();
  //
}