# 🔴 1RO BGU — PARCIAL 2 / SEMANA 4 (23 – 27 nov)
**Tema:** Atenuador de Brillo LED (`map()` + PWM `analogWrite`) *(Individual 2)*  
**Mediador:** David Castro  
**Modo de Clase:** Modo A — Tema Nuevo (45 min)  
**Entregable:** Captura en Tinkercad / visto bueno en kit físico + reto de velocidad en Classroom.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Modificar** el brillo de un LED suavemente con el potenciómetro, como el brillo de un celular.
* **¿Para qué me sirve en la vida?** Así funcionan los reguladores de luz (*dimmers*), el brillo de la pantalla del celular y el control de velocidad de motores.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"La semana pasada sus LEDs solo tenían dos estados: apagado o prendido al 100%. ¿Cómo hacemos para que un LED suba su brillo suavecito como la pantalla del teléfono?"*
* **Propósito en pantalla:** *"Modificar el brillo de un LED suavemente con el potenciómetro, como el brillo de un celular."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **Pines PWM (`~`):** En Arduino UNO son los pines **3, 5, 6, 9, 10, 11**. Aceptan valores de **0 a 255** con `analogWrite(pin, brillo);`.
* **Función `map()`:** Convierte el rango del potenciómetro (`0–1023`) al rango PWM (`0–255`):
  `int brillo = map(valor, 0, 1023, 0, 255);`
* **Modelación:** Conectar Potenciómetro en `A0` y 1 LED en Pin `~9`, cargar código y girar la perilla.

### 3. Práctica Guiada y Reto Individual (15 – 40 min)
* **15 – 25 min (Guiada):** Todos arman y prueban el código base del atenuador en Tinkercad (o kit físico).
* **25 – 40 min (Reto Solos):** *"Agrega un segundo LED en el Pin `~10` que haga exactamente lo contrario: cuando uno sube al máximo de brillo, el otro baja a cero (`255 - brillo`)."*

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **2 preguntas rápidas:**
  1. *"¿Qué símbolo tienen en la placa los pines que soportan `analogWrite()`?"*
  2. *"¿Por qué usamos `map(valor, 0, 1023, 0, 255)`?"*
* **Cierre:** Subir captura con nota de nombre o recibir visto bueno en kit físico.

## 📢 TEXTO PARA GOOGLE CLASSROOM
```text
TÍTULO: Actividad Individual 2: Atenuador de Brillo LED (map y PWM)

PROPÓSITO: Modificar el brillo de un LED suavemente con el potenciómetro, como el brillo de un celular.

CÓDIGO BASE:
void setup() {
  pinMode(9, OUTPUT);
}
void loop() {
  int valor = analogRead(A0);
  int brillo = map(valor, 0, 1023, 0, 255);
  analogWrite(9, brillo);
}

RETO INDIVIDUAL:
1. Agrega un segundo LED en el pin PWM ~10.
2. Haz que funcione invertido (cuando el pin 9 brilla al máximo, el pin 10 se apaga: analogWrite(10, 255 - brillo);).
3. Sube 1 captura con tu nombre en una Nota Virtual o comentario del código.

Calificación: 10 puntos (Actividad Individual 2).
```

---

## 🎨 PROMPT PARA NOTEBOOKLM
```text
Crea una presentación estilo cómic educativo de las Tortugas Ninja en español para estudiantes de 1ro BGU (15-16 años) del Volumen 2: "Señales Analógicas y Regulación PWM", como un capítulo autoconclusivo independiente ("Atenuador de Brillo PWM con map()", etiqueta 👤 ACTIVIDAD INDIVIDUAL 2) basado en el CAPÍTULO #2 de FUENTE_1RO_BGU_PARCIAL2_COMPLETO.md.

ELENCO Y ALTERNANCIA VISUAL (CÓMIC + LÁMINA DE ESTUDIO):
Usa únicamente personajes de las Tortugas Ninja en TODAS las diapositivas: Leonardo, Donatello, Rafael, Miguel Ángel y Destructor (prohibido dibujar niños genéricos, profesores o personajes externos).
- En los bloques de HISTORIA (Portada, Conflicto, Reto y Cierre): usa viñetas dinámicas de cómic con diálogos regulando sigilosamente la intensidad de las luces en una infiltración nocturna.
- En los bloques de TEORÍA: usa láminas explicativas profundas estilo cuadrícula comparativa ("Qué es PWM: pulsos rápidos ON/OFF con analogWrite 0-255" y "Por qué necesitamos map(valor, 0, 1023, 0, 255)"), con ondas cuadradas y diagramas claros presentados por Donatello sin globos que tapen las fórmulas.

Usa las diapositivas que necesites para no comprimir conceptos, siguiendo exactamente este orden de bloques:
1. Portada y gancho inicial con etiqueta 👤 ACTIVIDAD INDIVIDUAL.
2. Propósito LEV y explicación cercana a su edad (15-16 años) de para qué sirve PWM en reguladores de brillo de pantallas, motores y luces inteligentes.
3. Láminas explicativas profundas de PWM (pines ~) y la función map().
4. Enunciado claro de la actividad individual en Tinkercad y kit físico + 1 consejo (PROHIBIDO regalar el código final del reto).
5. Verificación y cierre autoconclusivo.

Prohibido poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados, "Continuará..." o adelantos del próximo capítulo (este capítulo cierra al terminar).
```
