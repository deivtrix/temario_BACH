// ==========================================
// SIMULACIÓN VELXIO / WOKWI: 1RO BGU
// PRÁCTICA: SIRENA POLICIAL CON BOOLEANOS
// ==========================================

// Pines de los LEDs Rojos
const int rojo1 = 6;
const int rojo2 = 7;

// Pines de los LEDs Azules
const int azul1 = 12;
const int azul2 = 13;

// Variables de estado booleano
const bool encendido = true;
const bool apagado = false;

void setup() {
  pinMode(rojo1, OUTPUT);
  pinMode(rojo2, OUTPUT);
  pinMode(azul1, OUTPUT);
  pinMode(azul2, OUTPUT);
}

void loop() {
  // FASE 1: Destello Rojo (Rojos activos, Azules apagados)
  digitalWrite(rojo1, encendido);
  digitalWrite(rojo2, encendido);
  digitalWrite(azul1, apagado);
  digitalWrite(azul2, apagado);
  delay(300);

  // FASE 2: Destello Azul (Rojos apagados, Azules activos)
  digitalWrite(rojo1, apagado);
  digitalWrite(rojo2, apagado);
  digitalWrite(azul1, encendido);
  digitalWrite(azul2, encendido);
  delay(300);
}
