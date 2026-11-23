# 📗 9NO EGB — PARCIAL 3 / CLASE 7
**Tema:** Sensor Sigue-Líneas (IR) en Pista Negra (`🛠️ REFUERZO`)  
**Mediador:** David Castro  
**Modo de Clase:** Modo A/B — Mini-teoría (10 min) + Práctica en Pista (30 min) + Cierre (5 min)

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Aplicar** el sensor infrarrojo (IR) del mBot para que siga una línea negra sobre fondo blanco automáticamente.
* **¿Para qué me sirve en la vida?** Así se guían los robots transportadores en bodegas y fábricas siguiendo líneas en el suelo.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"En las fábricas, los robots siguen caminos pintados en el piso. Hoy probamos el sensor sigue-líneas de nuestro mBot."*
* **Propósito en pantalla:** *"Aplicar el sensor infrarrojo (IR) del mBot para que siga una línea negra sobre fondo blanco automáticamente."*

### 2. Teoría Corta (05 – 15 min)
* Los 2 ojos infrarrojos detectan blanco (refleja luz = `1`) vs. negro (absorbe luz = `0`).
* Lógica simple: ambos en negro $\rightarrow$ avanzar; se sale a la izquierda $\rightarrow$ corregir a la derecha; se sale a la derecha $\rightarrow$ corregir a la izquierda.

### 3. Práctica en Pista (`🛠️ REFUERZO`, 15 – 40 min)
* Prueban el algoritmo sigue-líneas sobre la pista de cinta negra y ajustan velocidad baja para no salirse en curvas.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
1. *"¿Por qué el sensor IR distingue entre blanco y negro?"*
2. *"¿Qué pasa si ponemos la velocidad al 100% en una curva cerrada?"*

---

## 🎨 PROMPT PARA NOTEBOOKLM
```text
Crea una presentación estilo cómic educativo de Super Mario en español para estudiantes de 9no EGB (13-14 años) del Volumen 3: "Navegación y Robótica Móvil", como un capítulo autoconclusivo independiente ("Refuerzo Integrador y Cierre", etiqueta 🛠️ REFUERZO) basado en el punto 7 de FUENTE_9NO_EGB_PARCIAL3_COMPLETO.md.

ELENCO Y ALTERNANCIA VISUAL (CÓMIC + LÁMINA DE ESTUDIO):
Usa únicamente personajes de Super Mario en TODAS las diapositivas: Mario, Luigi, Toad y Bowser en la copa final (prohibido dibujar niños genéricos, profesores o personajes externos).
- TRAMA EN 3 ACTOS: Inicio (el personaje tiene un problema concreto que solo se resuelve con este tema) -> Meollo (para ayudarlo, explican la teoría esencial con diagramas y consejos preventivos repetidos antes de construir/probar paso a paso) -> Final (logran resolver el problema inicial).
- En Portada, Reto y Cierre: viñetas dinámicas de cómic con diálogos en la copa final integrando pista y obstáculos.
- En el Mapa Resumen: lámina visual limpia resumiendo placa mCore, motores, ultrasonido y sigue-líneas sin globos largos que tapen los esquemas.

Usa las diapositivas que necesites, siguiendo exactamente este orden de bloques:
1. Portada y gancho inicial con etiqueta 🛠️ REFUERZO.
2. Propósito LEV y explicación cercana a su edad (13-14 años) de para qué les sirve combinar varios sensores y actuadores en un mismo sistema autónomo.
3. Lámina visual resumen de placa mCore, motores, ultrasonido y sigue-líneas.
4. Preguntas de repaso integrador (SIN respuestas visibles) y enunciado del reto combinado en pista (seguir línea negra + detenerse con alerta ante obstáculo).
5. Tabla de Autoevaluación Escala de Likert (1 al 5) con los 4 aspectos exactos de la fuente y cierre autoconclusivo.

ALCANCE ESTRICTO: Usa únicamente los conceptos y código verificado de la fuente (PROHIBIDO inventar código por tu cuenta o introducir bucles/librerías/temas avanzados no vistos en esta clase).
Prohibido poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados, "Continuará..." o adelantos del próximo capítulo (este capítulo cierra al terminar).
```

### 🎬 VIDEO DE REPASO DEL PARCIAL
```text
Crea un video explicativo de repaso en español para estudiantes de 9no EGB (13-14 años) sobre todo el Volumen 3: "Navegación y Robótica Móvil" usando el archivo FUENTE_9NO_EGB_PARCIAL3_COMPLETO.md.

Cubre de forma ordenada y solo teórica todos los temas y subtemas del parcial (arquitectura de la placa mCore y puertos RJ25, modo En Vivo vs. Subir código, luces RGB y buzzer, tracción diferencial M1/M2 y giros con diagramas de flujo, calibración física por fricción/batería, sensor ultrasonido en cm y lógica binaria 0/1 del sensor sigue-líneas IR). Usa gráficos claros, diagramas de flujo y ejemplos cotidianos cercanos a su edad (sin personajes de cómics).

Prohibido mencionar nombres de profesor/mediador, fechas, "Semana X" o entregables.
```
