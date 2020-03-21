char response;
int led = 9;

void setup() {
  Serial.begin(9600);
  pinMode(9, OUTPUT);
}


void loop() {
  while (Serial.available()) {
    response = Serial.read();
    if (response == 'y') {
      digitalWrite(9, HIGH);
    } else if (response == 'n') {

      digitalWrite(9, LOW);
    }
    Serial.flush();
  }

}
