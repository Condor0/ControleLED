void setup() {
  Serial.begin(115200);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
}

void loop() {
  if (Serial.available()>0){
    int dado = Serial.read();
    if (dado == '2'){
      digitalWrite(2, HIGH);
    }
    if (dado == '3'){
      digitalWrite(3, HIGH);
      }
    if (dado == '4'){
      digitalWrite(4, HIGH);
    }
    else if (dado  == '5'){
      digitalWrite(2, LOW);
    }
    else if (dado  == '6'){
      digitalWrite(3, LOW);
  }
    else if (dado == '7'){
      digitalWrite(4, LOW);
    }
  }
}
