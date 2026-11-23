# 🔴 1RO BGU — PARCIAL 2 / SEMANA 6 (7 – 11 dic)
**Tema:** Theremin Musical Controlado por Luz (LDR + Buzzer `tone()`) *(Grupal Físico)*  
**Mediador:** David Castro  
**Modo de Clase:** Modo A/B — Mini-teoría (10 min) + Montaje Grupal Físico (30 min) + Cierre (5 min)  
**Entregable:** Visto bueno en vivo + Informe corto anti-IA grupal (con foto y parámetros) en Classroom.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Construir** un instrumento musical (Theremin) que cambia de sonido al tapar la luz con la mano.
* **¿Para qué me sirve en la vida?** Muestra cómo un sensor analógico puede controlar actuadores distintos a las luces, como alarmas sonoras, sintetizadores o sensores de proximidad.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Hoy vamos a construir un instrumento musical que se toca sin tocarlo: solo moviendo la mano encima de un sensor de luz. Se llama Theremin."*
* **Propósito en pantalla:** *"Construir un instrumento musical (Theremin) que cambia de sonido al tapar la luz con la mano."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **Mismo circuito LDR de la semana pasada** (`A0` + $10\text{k}\Omega$ a GND) + **1 Buzzer** conectado al Pin `8` y `GND`.
* **Lógica clave:**
  `int nota = map(luz, 100, 900, 150, 2000);`  
  `tone(8, nota);`
* Proyectar la simulación funcionando en Tinkercad para que vean cómo suena al mover la luz.

### 3. Trabajo Grupal Físico con Intervención del Mediador (15 – 40 min)
* **Instrucción:** En grupos con su kit físico Arduino, arman la LDR + Buzzer, calibran los valores reales de luz del aula en el Monitor Serial y ajustan `map()` para que suene grave al tapar y agudo con luz.
* **Tu rol:** Ayudas a diferenciar si el buzzer es activo o pasivo y a calibrar el rango de `map()` según la luz del laboratorio.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **2 preguntas rápidas:**
  1. *"¿Qué hace la función `tone(8, nota)`?"*
  2. *"¿Por qué tuvimos que cambiar los números de entrada en `map()` según la luz del aula?"*
* **Cierre:** Demostración en vivo en mesa + entrega de foto grupal y parámetros en Classroom.

## 📢 TEXTO PARA GOOGLE CLASSROOM
```text
TÍTULO: Actividad Grupal Física: Theremin Musical con Luz (LDR + Buzzer)

PROPÓSITO: Construir un instrumento musical (Theremin) que cambia de sonido al tapar la luz con la mano.

CÓDIGO BASE:
void setup() {
  Serial.begin(9600);
}
void loop() {
  int luz = analogRead(A0);
  int nota = map(luz, 100, 900, 200, 2000); // Ajustar según tu lectura real
  tone(8, nota);
  delay(20);
}

INSTRUCCIONES (En grupos):
1. Armen el circuito físico (LDR en A0 con 10k a GND + Buzzer en Pin 8 y GND).
2. Calibren el map() según la luz real del laboratorio.
3. Suban 1 foto del circuito con un papel con sus nombres e indiquen en el comentario:
   - ¿Qué valores mínimo y máximo marcó su LDR?
   - ¿Qué pasaba con el sonido al acercar y alejar la mano?

Calificación: 10 puntos (Actividad Grupal Física).
```

---

## 🎨 PROMPT PARA NOTEBOOKLM
```text
Crea una presentación estilo cómic educativo de las Tortugas Ninja en español para estudiantes de 1ro BGU (15-16 años) del Volumen 2: "Señales Analógicas y Regulación PWM", como un capítulo autoconclusivo independiente ("Theremin Musical con Luz", etiqueta 👥 ACTIVIDAD GRUPAL) basado en el CAPÍTULO #4 de FUENTE_1RO_BGU_PARCIAL2_COMPLETO.md.

ELENCO Y ALTERNANCIA VISUAL (CÓMIC + LÁMINA DE ESTUDIO):
Usa únicamente personajes de las Tortugas Ninja en TODAS las diapositivas: Leonardo, Donatello, Rafael, Miguel Ángel y Krang (prohibido dibujar niños genéricos, profesores o personajes externos).
- TRAMA EN 3 ACTOS: Inicio (el personaje tiene un problema concreto que solo se resuelve con este tema) -> Meollo (para ayudarlo, explican la teoría esencial con diagramas y consejos preventivos repetidos antes de construir/probar paso a paso) -> Final (logran resolver el problema inicial).
- En los bloques de HISTORIA (Portada, Desafío sonoro, Reto y Cierre): usa viñetas dinámicas de cómic con diálogos creando un instrumento musical sin contacto controlado por sombra y luz.
- En los bloques de TEORÍA: usa láminas explicativas profundas ("Función tone(pin, frecuencia) y mapeo de luz 0-1023 a rango audible en Hz"), con diagramas claros presentados por Donatello sin globos que tapen la sintaxis.

Usa las diapositivas que necesites para no comprimir conceptos, siguiendo exactamente este orden de bloques:
1. Portada y gancho inicial con etiqueta 👥 ACTIVIDAD GRUPAL.
2. Propósito LEV y explicación cercana a su edad (15-16 años) de para qué sirve convertir la lectura de un sensor en frecuencias sonoras o alarmas variables.
3. Lámina explicativa profunda de tone() y mapeo de frecuencias.
4. Enunciado claro de la actividad grupal física + 1 consejo de montaje (PROHIBIDO dar el código resuelto del reto).
5. Verificación y cierre autoconclusivo.

ALCANCE ESTRICTO: Usa únicamente los conceptos y código verificado de la fuente (PROHIBIDO inventar código por tu cuenta o introducir bucles/librerías/temas avanzados no vistos en esta clase).
Prohibido poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados, "Continuará..." o adelantos del próximo capítulo (este capítulo cierra al terminar).
```
