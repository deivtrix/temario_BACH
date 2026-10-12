# 📘 10MO EGB — PLANIFICACIÓN DE CLASE (SEMANA 3)
## 🔌 CÓMO FUNCIONA EL PROTOBOARD: LÍNEAS, ENERGIZACIÓN Y CONEXIONES

**Propósito de la Clase (Taxonomía Lev):**  
> **Comprender** la arquitectura interna y el flujo de corriente en una protoboard siguiendo las diapositivas oficiales del curso (`CA.1.RB.5.PR.26-27`, pág. 38-44), **identificar** la diferencia entre los buses horizontales de alimentación ($+$ y $-$) y las pistas verticales de 5 orificios comunes, y **simular** en Tinkercad Circuits la energización correcta y conexión de componentes sin cortocircuitos.

* **Curso:** 10mo EGB  
* **Duración:** 45 Minutos  
* **Modalidad:** 💻 100% Virtual en Computadoras (Tinkercad Circuits + Cuaderno de apuntes).  
* **Docente:** Ing. David Castro T.  
* **Diapositivas Oficiales:** `CA.1.RB.5.PR.26-27 (Ard mod1)` — Diapositivas 38 a 44.  
* **Política de Entrega:** 🟢 **SIN INFORME ESCRITO.** Evaluación 100% formativa en pantalla y verificación directa del docente en el laboratorio. Cero tareas pesadas para la casa.

---

### ⏱️ DESGLOSE PASO A PASO (45 MINUTOS)

#### 1. 🎯 Activación y Diapositivas: ¿Qué es una Protoboard? (00 - 10 min)
* Proyección de las diapositivas 38 y 39:
  * *"Chicos, una protoboard no es una caja mágica; por dentro tiene láminas de metal con patitas que hacen contacto. Si no entendemos cómo viajan las líneas metálicas por dentro, causaremos cortocircuitos al conectar componentes."*
* **Pregunta detonante:** *"¿Por qué la protoboard tiene orificios numerados y otros con signos $+$ y $-$?"*

---

#### 2. 💡 Las 3 Zonas Clave del Protoboard (10 - 22 min)
Explicación directa con la pizarra y las diapositivas 40 a 43:

1. **⚡ Buses de Alimentación (Líneas de Energización Horizontales):**
   * Son las dos filas largas de los extremos (superior e inferior) marcadas con rojo ($+$) y azul/negro ($-$).
   * **Cómo van las conexiones:** Van conectadas **horizontalmente a lo largo de toda la placa** para llevar energía a cualquier rincón.
   * Regla de oro del docente: *"Rojo con 5V, Negro/Azul con GND"*.

2. **🔢 Pistas de Trabajo (Líneas Comunes Verticales - Pág. 41):**
   * Los orificios del centro organizados en columnas numeradas (ej. columna 1, 2, 3... con letras a, b, c, d, e).
   * **Cómo van las conexiones:** Esos 5 agujeros de una misma columna están **interconectados verticalmente entre sí**.
   * Si conectas dos cables en la misma columna, se tocan eléctricamente. Si los conectas en columnas distintas, están aislados.

3. **🚧 El Canal Central de Separación (Pág. 43):**
   * ¿Por qué la protoboard está dividida por una zanja plástica a la mitad?
   * Para separar los orificios de arriba de los de abajo. Permite conectar chips (circuitos integrados) con patitas a ambos lados sin que sus pines hagan cortocircuito entre sí.

---

#### 3. 💻 Práctica Guiada en Tinkercad Circuits: Energización y Conexión (22 - 38 min)
Los estudiantes abren [tinkercad.com](https://www.tinkercad.com/) y crean un circuito nuevo:

* **Paso 1 (Alimentar la Protoboard):**
  * Sacar una batería de $9\text{V}$ (o fuente de alimentación) y una protoboard.
  * Conectar el terminal positivo ($+$) a la línea roja del bus superior.
  * Conectar el terminal negativo ($-$) a la línea negra/azul del bus superior.
  * **Puenteo:** Usar 2 cables para pasar el $+$ y el $-$ al bus inferior para que toda la placa tenga corriente.

* **Paso 2 (Conexión de Circuito Básico en Pistas Comunes - Pág. 42):**
  * Conectar una resistencia de $330\ \Omega$ desde el bus positivo ($+$) hacia la columna 10.
  * Conectar el ánodo (pata larga) de un foco LED en la columna 10 (misma columna donde llega la resistencia).
  * Conectar el cátodo (pata corta) del LED en la columna 11.
  * Desde la columna 11, sacar un cable de retorno hacia el bus negativo ($-$).

* **Paso 3 (Demostración de Error de Pistas):**
  * ¿Qué pasa si clavas las dos patas del LED en la misma columna (ej. ambas en la columna 10)?
  * *Observación en vivo:* Las dos patas se unen por la misma lámina metálica, la corriente se salta el LED y no enciende (puente cerrado).

---

#### 4. 📝 Cierre Formativo y Verificación en Pantalla (38 - 45 min)
* El docente recorre los puestos verificando:
  1. La protoboard correctamente energizada con cables ordenados (rojo para $+$ y negro para $-$).
  2. El foco LED encendido utilizando las columnas de 5 agujeros.
* Sin informe de entrega para la casa: evaluación formativa registrada en la planilla docente en el aula.

---

### 📢 AVISO INFORMATIVO PARA GOOGLE CLASSROOM (REGISTRO FORMATIVO)

```text
TÍTULO: Clase Práctica: Arquitectura y Energización del Protoboard en Tinkercad

INSTRUCCIONES:
Estimados estudiantes, en esta sesión aprendimos a utilizar correctamente la protoboard analizando su estructura interna según nuestras diapositivas oficiales:

1. Identificamos los buses de alimentación horizontales (+ y -) y las pistas comunes verticales de 5 orificios.
2. Comprendimos por qué la protoboard tiene un canal aislante central para evitar cortocircuitos.
3. Simulamos en Tinkercad Circuits la energización correcta y el encendido de un foco LED a través de las pistas.

📌 NOTA: Esta sesión es 100% práctica y formativa en laboratorio; la calificación fue registrada directamente en sus pantallas durante la clase. ¡Buen trabajo!
```
