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
