// ==========================================
// SIMULACIÓN VELXIO / WOKWI: 3RO BGU
// PRÁCTICA: BANDA TRANSPORTADORA CON TRANSISTOR NPN
// ==========================================

const int pinMotor = 2;       // Base del transistor NPN 2N2222
const bool avanza = true;     // Banda en marcha
const bool frena = false;     // Banda detenida

void setup() {
  pinMode(pinMotor, OUTPUT);
}

void loop() {
  // La Banda Transportadora avanza (3 segundos)
  digitalWrite(pinMotor, avanza);
  delay(3000);

  // La Banda se detiene para empaque (1 segundo)
  digitalWrite(pinMotor, frena);
  delay(1000);
}
