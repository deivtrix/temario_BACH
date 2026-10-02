// ========================================================
// PROYECTO DE PRUEBA: VELXIO / ARDUINO SIMULATOR
// Docente: David Castro T.
// ========================================================

const int pinBoton = 2;   // Pulsador conectado al Pin 2
const int pinLED = 12;    // LED Verde conectado al Pin 12

void setup() {
  Serial.begin(9600);
  
  // Usamos INPUT_PULLUP interno para no requerir resistencia externa en el botón
  pinMode(pinBoton, INPUT_PULLUP);
  pinMode(pinLED, OUTPUT);

  Serial.println("==========================================");
  Serial.println(" ¡CIRCUITO DE PRUEBA LISTO Y FUNCIONANDO! ");
  Serial.println(" Haz clic en el boton rojo para interactuar ");
  Serial.println("==========================================");
}

void loop() {
  int estadoBoton = digitalRead(pinBoton);

  // Con INPUT_PULLUP: LOW = Presionado, HIGH = Suelto
  if (estadoBoton == LOW) {
    digitalWrite(pinLED, HIGH);
    Serial.println("[EVENTO] -> Boton presionado: LED ENCENDIDO");
    delay(150); // Pequeña pausa para no saturar la consola
  } else {
    digitalWrite(pinLED, LOW);
  }
}

