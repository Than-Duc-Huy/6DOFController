void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial3.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial3.available() > 0){
    Serial.println(Serial3.readStringUntil('\n'));
  }
}
