# 🔴 1RO BGU — PARCIAL 2 / SEMANA 7 (14 – 18 dic)

> [!IMPORTANT]
> # 👥 ACTIVIDAD GRUPAL EVALUADA
**Tema:** Theremin Musical Controlado por Luz (LDR + Buzzer `tone()`) *(Grupal Físico — Kits Arduino)*  
**Mediador:** David Castro  
**Modo de Clase:** Modo B — Montaje Grupal Físico en Kit Arduino (45 min) *(usando código validado en S6)*  
**Entregable:** Visto bueno en vivo del kit físico sonando + Informe corto grupal anti-IA en Classroom.

## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Verificar** los valores reales de luz en el Monitor Serial para ajustar bien nuestros sensores.
* **¿Para qué me sirve en la vida?** Todo sensor físico cambia según el lugar (más o menos luz); saber leer el Monitor Serial permite ajustar cualquier proyecto en segundos.

## ⏱️ GUION MINUTO A MINUTO (45 MINUTOS)
### 1. Inicio y Propósito (00 – 05 min)
* **¿Qué decirles?** *"Muchos copiaron un número como `400` para su LDR sin mirar qué número marcaba su propio sensor en esta aula. Hoy aprendemos a diagnosticar y calibrar como ingenieros."*
* **Propósito en pantalla:** *"Verificar los valores reales de luz en el Monitor Serial para ajustar bien nuestros sensores."*

### 2. Demostración Rápida de Diagnóstico (05 – 12 min)
* Proyectar cómo imprimir `Serial.print("Valor: "); Serial.println(analogRead(A0));` y calcular el **punto medio** `(min + max) / 2` como umbral perfecto.

### 3. Nivelación y Reto de Calibración (12 – 40 min)
* Quienes deban alguna práctica del Parcial 2 (Potenciómetro, Atenuador PWM, LDR o Theremin) la completan hoy.
* Quienes estén al día calibran un circuito en Tinkercad/kit usando la fórmula de punto medio e imprimen en Serial `"DIA"` o `"NOCHE"`.

### 4. Cierre y Preguntas de Verificación (40 – 45 min)
* **2 preguntas rápidas:**
  1. *"¿Cómo encuentras el umbral ideal para un sensor LDR en cualquier habitación?"*
  2. *"¿Qué comando inicia la comunicación entre Arduino y la pantalla de la PC?"*

## 📢 TEXTO PARA GOOGLE CLASSROOM
```text
TÍTULO: Refuerzo Práctico: Calibración de Sensores con Monitor Serial

PROPÓSITO: Verificar los valores reales de luz en el Monitor Serial para ajustar bien nuestros sensores.

ACTIVIDAD:
- Práctica de diagnóstico en clase calculando el punto medio real de un sensor analógico (LDR / Potenciómetro).
- Nivelación de entregas pendientes antes de vacaciones.
```

---

## 🎨 PROMPT PARA NOTEBOOKLM
```text
Crea una presentación estilo cómic educativo de las Tortugas Ninja en español para estudiantes de 1ro BGU (15-16 años) del Volumen 2: "Señales Analógicas y Regulación PWM", como un capítulo autoconclusivo independiente ("Calibración con Monitor Serial", etiqueta 🛠️ REFUERZO) basado en el CAPÍTULO #5 de FUENTE_1RO_BGU_PARCIAL2_COMPLETO.md.

ELENCO Y ALTERNANCIA VISUAL (CÓMIC + LÁMINA DE ESTUDIO):
Usa únicamente personajes de las Tortugas Ninja en TODAS las diapositivas: Leonardo, Donatello, Rafael, Miguel Ángel y Destructor (prohibido dibujar niños genéricos, profesores o personajes externos).
- TRAMA EN 3 ACTOS: Inicio (el personaje tiene un problema concreto que solo se resuelve con este tema) -> Meollo (para ayudarlo, explican la teoría esencial con diagramas y consejos preventivos repetidos antes de construir/probar paso a paso) -> Final (logran resolver el problema inicial).
- En Portada, Problema de luz real y Cierre: viñetas dinámicas de cómic con diálogos resolviendo por qué un código falla cuando cambia la luz del aula.
- En Teoría: lámina explicativa profunda paso a paso ("Medir Mínimo (oscuro) + Medir Máximo (luz) -> Calcular Punto Medio (min + max) / 2"), presentada por Donatello sin globos que tapen la fórmula.

Usa las diapositivas que necesites, siguiendo exactamente este orden de bloques:
1. Portada y gancho inicial con etiqueta 🛠️ REFUERZO.
2. Propósito LEV y explicación cercana a su edad (15-16 años) de para qué sirve calibrar umbrales reales en vez de copiar números fijos de internet.
3. Lámina explicativa profunda del método de calibración con Monitor Serial.
4. Reto práctico de calibración en clase (SIN regalar los valores medidos) y cierre autoconclusivo.

ALCANCE ESTRICTO: Usa únicamente los conceptos y código verificado de la fuente (PROHIBIDO inventar código por tu cuenta o introducir bucles/librerías/temas avanzados no vistos en esta clase).
Prohibido poner nombres de profesor/mediador, fechas, "Semana X", entregables amarrados, "Continuará..." o adelantos del próximo capítulo (este capítulo cierra al terminar).
```
