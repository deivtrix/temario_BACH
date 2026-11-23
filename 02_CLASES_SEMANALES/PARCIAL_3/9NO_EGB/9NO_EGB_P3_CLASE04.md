# 📗 9NO EGB — PARCIAL 3 / CLASE 4
**Tema:** Control de Motores DC y Velocidad ($0\text{–}255$) (`👤 ACTIVIDAD INDIVIDUAL 2`)  
**Mediador:** David Castro  
**Modo de Clase:** Modo A — Tema Nuevo + Individual (45 min)

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Controlar** la dirección y velocidad de los motores del mBot en mBlock 5 para que avance, retroceda y gire con precisión.
* **¿Para qué me sirve en la vida?** Es la base de la robótica móvil: controlar tracción diferencial (dos ruedas independientes) como en aspiradoras robot o rovers.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Hoy hacemos que el mBot ruede. Para girar, una rueda avanza y la otra frena o retrocede."*
* **Propósito en pantalla:** *"Controlar la dirección y velocidad de los motores del mBot en mBlock 5 para que avance, retroceda y gire con precisión."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* Bloques de **Acción:** `avanzar a potencia X% durante Y seg`, `girar izquierda/derecha`, `detener movimiento`.
* Explicar rango de potencia/velocidad y cómo el **tiempo** define la distancia recorrida.

### 3. Práctica Individual (15 – 40 min)
* Programan en mBlock 5 una maniobra de **avanzar 2s $\rightarrow$ girar 90° $\rightarrow$ retroceder 1s $\rightarrow$ detenerse** y la prueban en el mBot.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
1. *"¿Cómo logra girar un robot de 2 ruedas si no tiene volante como un carro?"*
2. *"¿Qué bloque es obligatorio al final para que el mBot no siga rodando infinito?"*

---

## 🎨 PROMPT PARA NOTEBOOKLM
```text
Crea una presentación estilo cómic educativo de Super Mario en español para estudiantes de 9no EGB (13-14 años) del Volumen 3: "Navegación y Robótica Móvil", como un capítulo autoconclusivo independiente ("Reto Pista Cuadrada 50x50", etiqueta 👥 ACTIVIDAD GRUPAL) basado en el punto 4 de FUENTE_9NO_EGB_PARCIAL3_COMPLETO.md.

ELENCO Y ALTERNANCIA VISUAL (CÓMIC + LÁMINA DE ESTUDIO):
Usa únicamente personajes de Super Mario en TODAS las diapositivas: Mario, Luigi, Toad y Bowser (prohibido dibujar niños genéricos, profesores o personajes externos).
- TRAMA EN 3 ACTOS: Inicio (el personaje tiene un problema concreto que solo se resuelve con este tema) -> Meollo (para ayudarlo, explican la teoría esencial con diagramas y consejos preventivos repetidos antes de construir/probar paso a paso) -> Final (logran resolver el problema inicial).
- En los bloques de HISTORIA (Portada, Conflicto/Versus, Reto y Cierre): usa viñetas dinámicas de cómic con diálogos en el circuito cuadrado de Bowser.
- En los bloques de TEORÍA: usa láminas explicativas profundas estilo cuadrícula comparativa ("Simulación ideal vs. Pista física con fricción y desgaste de batería" y "Código largo vs. Bucle repetir 4 veces"), presentadas por Toad sin globos que tapen el diagrama.

Usa las diapositivas que necesites para no comprimir conceptos, siguiendo exactamente este orden de bloques:
1. Portada y gancho de desafío con etiqueta 👥 ACTIVIDAD GRUPAL.
2. Propósito LEV y explicación cercana a su edad (13-14 años) de para qué les sirve calibrar un sistema físico real frente a fricción y batería en lugar de confiar solo en teoría.
3. Lámina explicativa profunda de calibración iterativa y bucle repetir 4 veces.
4. Enunciado claro del reto grupal en pista cuadrada real de 50x50 cm + 1 consejo (PROHIBIDO regalar tiempos exactos ni código resuelto).
5. Cierre autoconclusivo.

ALCANCE ESTRICTO: Usa únicamente los conceptos y código verificado de la fuente (PROHIBIDO inventar código por tu cuenta o introducir bucles/librerías/temas avanzados no vistos en esta clase).
Prohibido poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados, "Continuará..." o adelantos del próximo capítulo (este capítulo cierra al terminar).
```
