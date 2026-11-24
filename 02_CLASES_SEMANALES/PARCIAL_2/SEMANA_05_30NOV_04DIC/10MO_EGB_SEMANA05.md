# 📘 10MO EGB — PARCIAL 2 / SEMANA 5 (30 nov – 4 dic)

> [!NOTE]
> # 📘 CLASE SIN ENTREGA
**Tema:** Múltiples Salidas Digitales: Semáforo en Tinkercad  
**Mediador:** David Castro  
**Modo de Clase:** Modo A — Tema Nuevo (45 min)  
**Entregable:** Captura exprés en Classroom del semáforo funcionando con variables `int`.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Simular** un semáforo de 3 luces en Tinkercad usando nombres (`int`) para ordenar los pines.
* **¿Para qué me sirve en la vida?** Para organizar cualquier programa grande usando nombres claros (`ledRojo`, `ledVerde`) en lugar de memorizar números de pines.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"La semana pasada controlamos 1 o 2 LEDs usando `13` y `12`. Pero si tuviéramos 20 luces, ¿se acordarían qué hace cada número? Hoy vamos a ponerles nombre con variables."*
* **Propósito en pantalla:** *"Simular un semáforo de 3 luces en Tinkercad usando nombres (`int`) para ordenar los pines."*

### 2. Teoría Corta y Modelación (05 – 15 min)
* **Variables `int`:** `int rojo = 13;`, `int amarillo = 12;`, `int verde = 11;`. Si mañana cambias un cable de pin, solo cambias el número arriba una vez.
* **Modelación en Tinkercad:** Conectar 3 LEDs (Rojo, Amarillo, Verde) con resistencias de $220\,\Omega$ a GND y cargar el ciclo básico.

### 3. Práctica Guiada y Reto Individual (15 – 40 min)
* **15 – 25 min (Guiada):** Todos arman el semáforo de 3 LEDs en protoboard dentro de Tinkercad y prueban el encendido secuencial.
* **25 – 40 min (Reto Solos):** *"Haz que la luz **Verde** parpadee 3 veces antes de pasar a Amarillo (como semáforo real de ciudad), y coloca tiempos reales: Verde 3s, Amarillo 1s, Rojo 3s."*

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **2 preguntas rápidas:**
  1. *"¿Para qué sirve declarar `int rojo = 13;` al inicio del código?"*
  2. *"¿Qué pasa si olvidas apagar el LED anterior con `LOW` antes de encender el siguiente?"*
* **Cierre:** Subir captura de Tinkercad con el código y el semáforo encendido a Classroom.

## 📢 TEXTO PARA GOOGLE CLASSROOM
```text
TÍTULO: Práctica Arduino: Semáforo Inteligente en Tinkercad

PROPÓSITO: Simular un semáforo de 3 luces en Tinkercad usando nombres (`int`) para ordenar los pines.

INSTRUCCIONES:
1. Conecta 3 LEDs (Rojo en Pin 13, Amarillo en Pin 12, Verde en Pin 11) con sus resistencias de 220 ohmios a GND.
2. Declara variables int para cada color al inicio del código.
3. Programa el ciclo completo haciendo que el Verde parpadee 3 veces antes de cambiar a Amarillo.
4. Escribe // Tu Nombre Apellido en la línea 1 y sube 1 captura de la simulación corriendo.

Calificación: 10 puntos (Práctica de clase).
```

---

## 🎨 PROMPT PARA NOTEBOOKLM
```text
Crea una presentación estilo cómic educativo de las Tortugas Ninja en español para estudiantes de 10mo EGB (14-15 años) del Volumen 2: "Conexiones Seguras y Primer Código", como un capítulo autoconclusivo independiente ("Semáforo Funcional en Tinkercad") basado en el CAPÍTULO #3 de FUENTE_10MO_EGB_PARCIAL2_COMPLETO.md.

ELENCO Y ALTERNANCIA VISUAL (CÓMIC + LÁMINA DE ESTUDIO):
Usa únicamente personajes de las Tortugas Ninja en TODAS las diapositivas: Leonardo, Donatello, Rafael y Miguel Ángel (prohibido dibujar niños genéricos, profesores o personajes externos).
- TRAMA EN 3 ACTOS: Inicio (el personaje tiene un problema concreto que solo se resuelve con este tema) -> Meollo (para ayudarlo, explican la teoría esencial con diagramas y consejos preventivos repetidos antes de construir/probar paso a paso) -> Final (logran resolver el problema inicial).
- En los bloques de HISTORIA (Portada, Problema de tráfico, Práctica y Cierre): usa viñetas dinámicas de cómic con diálogos sincronizando el cruce de túneles de la ciudad.
- En los bloques de TEORÍA: usa láminas explicativas profundas estilo cuadrícula comparativa ("Números sueltos difíciles de leer vs. Variables int con nombre claro" y "Secuencia temporal Rojo -> Verde -> Amarillo"), con diagramas claros presentados por Donatello sin globos que tapen el esquema.

Usa las diapositivas que necesites para no comprimir conceptos, siguiendo exactamente este orden de bloques:
1. Portada y gancho inicial.
2. Propósito LEV y explicación cercana a su edad (14-15 años) de para qué les sirve organizar pines con variables int y controlar múltiples salidas sincronizadas.
3. Láminas explicativas profundas sobre variables int y secuencia de 3 LEDs con resistencias de 220 Ω.
4. Práctica guiada paso a paso en Tinkercad Circuits dentro de la historia.
5. Preguntas de verificación (con pista breve de comprobación) y cierre autoconclusivo.

ALCANCE ESTRICTO: Usa únicamente los conceptos y código verificado de la fuente (PROHIBIDO inventar código por tu cuenta o introducir bucles/librerías/temas avanzados no vistos en esta clase).
Prohibido poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados, "Continuará..." o adelantos del próximo capítulo (este capítulo cierra al terminar).
```
