# 🔴 1RO BGU — PARCIAL 2 / SEMANA 5 (30 nov – 4 dic)
**Tema:** Poste de Alumbrado Público Automático (Sensor LDR)  
**Mediador:** David Castro  
**Modo de Clase:** Modo A — Tema Nuevo (45 min)  
**Entregable:** Captura en Tinkercad / visto bueno en kit físico + lectura serial en Classroom.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** un circuito con sensor de luz (LDR) que prenda un LED solo cuando oscurece, como un poste de calle.
* **¿Para qué me sirve en la vida?** Para automatizar luces de jardines, pasillos, faros de vehículos y pantallas que ajustan su brillo según la luz del ambiente.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"¿Quién apaga y prende los postes de luz de la calle cada noche? No hay una persona con un interruptor: usan un sensor que 've' la oscuridad. Hoy lo armamos."*
* **Propósito en pantalla:** *"Construir un circuito con sensor de luz (LDR) que prenda un LED solo cuando oscurece, como un poste de calle."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **¿Qué es una LDR?** Una resistencia que cambia su valor según la luz que recibe.
* **Conexión (Divisor de Voltaje):** 1 pata de la LDR a `5V`, la otra pata al pin **`A0`**, y desde ese mismo punto **`A0`** una resistencia de **$10\text{k}\Omega$ a `GND`**.
* **Modelación:** Leer `analogRead(A0)` en Monitor Serial, tapar la LDR con el dedo para ver cómo cambia el número y poner el `if (luz < umbral)`.

### 3. Práctica Guiada y Reto Individual (15 – 40 min)
* **15 – 25 min (Guiada):** Conectan la LDR + resistencia $10\text{k}\Omega$ + 1 LED en Pin 9 y ven los valores de luz vs. oscuridad en el Monitor Serial.
* **25 – 40 min (Reto Solos):** *"Ajusta tu umbral para que el LED prenda cuando tapas la LDR, y agrega un **segundo LED** o haz que el brillo suba gradualmente con `map()` mientras más oscuro esté."*

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **2 preguntas rápidas:**
  1. *"¿Por qué la LDR necesita una resistencia de $10\text{k}\Omega$ hacia `GND` para poder leerse en `A0`?"*
  2. *"¿Qué número marcó tu Monitor Serial con luz vs. tapado con el dedo?"*
* **Cierre:** Visto bueno en kit / subida de captura con valores reales en Classroom.

## 📢 TEXTO PARA GOOGLE CLASSROOM
```text
TÍTULO: Práctica Arduino: Poste de Alumbrado Público Automático (LDR)

PROPÓSITO: Construir un circuito con sensor de luz (LDR) que prenda un LED solo cuando oscurece, como un poste de calle.

CÓDIGO BASE:
void setup() {
  Serial.begin(9600);
  pinMode(9, OUTPUT);
}
void loop() {
  int luz = analogRead(A0);
  Serial.println(luz);
  if (luz < 400) { // Ajusta este umbral según tu lectura
    digitalWrite(9, HIGH);
  } else {
    digitalWrite(9, LOW);
  }
  delay(100);
}

ENTREGA:
1. Arma el circuito (LDR a 5V y A0 + resistencia 10k a GND + LED en Pin 9).
2. Sube 1 captura/foto funcionando y escribe en el comentario el valor exacto que marcó tu Monitor Serial con luz y en oscuridad.

Calificación: 10 puntos (Práctica de clase).
```

---

## 🎨 PROMPT PARA NOTEBOOKLM
```text
Crea una presentación estilo cómic educativo de las Tortugas Ninja en español para estudiantes de 1ro BGU (15-16 años) del Volumen 2: "Señales Analógicas y Regulación PWM", como un capítulo autoconclusivo independiente ("Poste de Alumbrado Automático (LDR)") basado en el CAPÍTULO #3 de FUENTE_1RO_BGU_PARCIAL2_COMPLETO.md.

ELENCO Y ALTERNANCIA VISUAL (CÓMIC + LÁMINA DE ESTUDIO):
Usa únicamente personajes de las Tortugas Ninja en TODAS las diapositivas: Leonardo, Donatello, Rafael y Miguel Ángel (prohibido dibujar niños genéricos, profesores o personajes externos).
- TRAMA EN 3 ACTOS: Inicio (el personaje tiene un problema concreto que solo se resuelve con este tema) -> Meollo (para ayudarlo, explican la teoría esencial con diagramas y consejos preventivos repetidos antes de construir/probar paso a paso) -> Final (logran resolver el problema inicial).
- En los bloques de HISTORIA (Portada, Problema al anochecer, Práctica y Cierre): usa viñetas dinámicas de cómic con diálogos automatizando las luminarias de la ciudad al caer la noche.
- En los bloques de TEORÍA: usa láminas explicativas profundas estilo cuadrícula comparativa ("Por qué la LDR necesita resistencia de 10 kΩ en divisor de voltaje" y "De día vs. De noche: cambio de lectura en A0 y decisión if/else"), presentadas por Donatello sin globos que tapen el circuito.

Usa las diapositivas que necesites para no comprimir conceptos, siguiendo exactamente este orden de bloques:
1. Portada y gancho inicial.
2. Propósito LEV y explicación cercana a su edad (15-16 años) de para qué les sirve usar divisores de voltaje con sensores resistivos en alumbrado público o celulares.
3. Láminas explicativas profundas de la LDR, divisor de voltaje con 10 kΩ y lectura en A0.
4. Práctica guiada paso a paso en Tinkercad y kit físico dentro de la historia.
5. Preguntas de verificación (con pista breve de comprobación) y cierre autoconclusivo.

ALCANCE ESTRICTO: Usa únicamente los conceptos y código verificado de la fuente (PROHIBIDO inventar código por tu cuenta o introducir bucles/librerías/temas avanzados no vistos en esta clase).
Prohibido poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados, "Continuará..." o adelantos del próximo capítulo (este capítulo cierra al terminar).
```
