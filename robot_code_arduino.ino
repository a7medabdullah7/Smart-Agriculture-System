// 🔌 تعريف الأرجل
#define ENA 5
#define IN1 6
#define IN2 7

#define ENB 9
#define IN3 10
#define IN4 11

char data;

void setup() {
  Serial.begin(9600);

  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);

  pinMode(ENB, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);

  stopMotors();
}

// 🚀 حركة للأمام
void forward() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);

  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);

  analogWrite(ENA, 180);
  analogWrite(ENB, 180);
}

// 🛑 توقف
void stopMotors() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);

  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
}

// 🔥 حركة قصيرة ذكية (أهم جزء)
void moveForwardShort() {
  forward();
  delay(700);   // يتحرك 0.7 ثانية
  stopMotors();
}

void loop() {
  if (Serial.available()) {
    data = Serial.read();

    if (data == '1') {
      // 🔴 فيه مرض → يتحرك شوية ويقف
      moveForwardShort();
    }
    else if (data == '0') {
      // 🟢 سليم → يقف
      stopMotors();
    }
  }
}   ابعتلي كود الاردوينو معدل