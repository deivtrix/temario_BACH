# 🐢 9NO EGB — PARCIAL 2 (FUENTE ÚNICA PARA NOTEBOOKLM)
**Materia:** Robótica y Tecnología  
**Unidad:** Modelado Digital 3D y Prototipado

---

# 1. Introducción a Tinkercad 3D y Llavero (`👤 ACTIVIDAD INDIVIDUAL 1`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Diseñar** un llavero personalizado en Tinkercad 3D dominando los ejes `X, Y, Z`, formas sólidas/huecas, alineación (`L`) y agrupación (`Ctrl + G`).
* **¿Para qué me sirve en la vida?** Para crear objetos reales imprimibles en 3D entendiendo cómo se ubican y combinan piezas en el espacio tridimensional.

## 📚 CONTENIDO Y RETO INDIVIDUAL
* **Fundamento técnico (10 min):**
  * **Espacio 3D (`X, Y, Z`):** `X` (ancho izquierda/derecha), `Y` (profundidad adelante/atrás) y `Z` (altura arriba/abajo sobre el plano de trabajo).
  * **Sólido vs. Hueco:** Un objeto hueco restado y agrupado (`Ctrl + G`) con un sólido recorta perforaciones exactas (como el ojal de un llavero).
  * **Comandos clave:** `L` (Alinear centros y bordes), `Ctrl + D` (Duplicar), `Ctrl + G` (Agrupar) y `Ctrl + Shift + G` (Desagrupar).
* **Actividad individual (`👤 ACTIVIDAD INDIVIDUAL` — sin diseño resuelto):**
  * Diseñar un llavero propio con base de bordes suaves, nombre o iniciales en relieve y perforación circular pasante para argolla.
  * **1 Consejo:** Usa la herramienta Alinear (`L`) antes de agrupar para que el texto y el agujero queden centrados con precisión.
* **Preguntas de verificación:** ¿Qué hace la combinación `Ctrl + G` cuando unes un cilindro hueco con una placa sólida? ¿Para qué sirve la tecla `L`?

---

# 2. Case de iPhone en Tinkercad 3D — Parte 1 (`📘 PRÁCTICA GUIADA`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Modelar** la estructura base de un protector (case) con medidas reales en milímetros y vaciado interno preciso.
* **¿Para qué me sirve en la vida?** Para diseñar piezas que deben encajar exactamente alrededor de objetos reales usando medidas en milímetros.

## 📚 CONTENIDO EXPLICATIVO Y PRÁCTICA GUIADA
* **Fundamento técnico (10 min):**
  * **Medición en milímetros (`mm`):** En diseño 3D e impresión 3D la unidad estándar es el milímetro (`1 cm = 10 mm`).
  * **Vaciado por diferencia:** Para crear una carcasa con paredes de `2 mm` de grosor, al bloque exterior se le resta un bloque hueco interior `4 mm` más estrecho en `X` y `Y`, elevado `2 mm` sobre `Z` (fondo sólido).
* **Práctica guiada:** Crear el bloque exterior del teléfono, duplicar (`Ctrl + D`), convertir en hueco, restar `4 mm` en ancho y largo, elevar `2 mm` en `Z`, alinear (`L`) al centro y agrupar (`Ctrl + G`) para obtener la bandeja base.
* **Preguntas de verificación:** Si la pared debe medir `2 mm` en cada lado, ¿cuántos milímetros en total debemos restar al ancho del bloque hueco interior?

---

# 3. Case de iPhone — Parte 2: Tolerancias y Cortes (`👤 ACTIVIDAD INDIVIDUAL 2`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Completar** el case 3D aplicando holguras/tolerancias reales y aberturas exactas para cámara, botones laterales y puerto de carga.
* **¿Para qué me sirve en la vida?** Para aprender por qué las piezas fabricadas necesitan décimas de milímetro de holgura para no quedar apretadas ni sueltas.

## 📚 CONTENIDO Y RETO INDIVIDUAL
* **Fundamento técnico (5 min):**
  * **Tolerancia / Holgura (`0.3` a `0.5 mm`):** Si un teléfono mide exactamente `71.5 mm` de ancho y haces el hueco de `71.5 mm`, en plástico impreso no entrará; se suma holgura para un ajuste funcional.
  * **Cortes funcionales:** Ventana trasera para módulo de cámara, ranura inferior para cargador y rebajes laterales para botones.
* **Actividad individual (`👤 ACTIVIDAD INDIVIDUAL` — sin diseño resuelto):**
  * Completar el case agregando con precisión el recorte de cámara, el puerto de carga y los botones laterales, verificando medidas y tolerancias reales.
  * **1 Consejo:** Usa el plano de trabajo auxiliar (`W`) sobre la cara lateral o trasera para colocar los huecos de botones y cámara sin que floten fuera de lugar.
* **Preguntas de verificación:** ¿Qué ocurriría al imprimir en 3D si diseñamos el hueco interno exactamente igual al ancho físico del teléfono sin holgura?

---

# 4. Escena Temática 3D con Vectores `.SVG` en Tinkercad (`👤 ACTIVIDAD INDIVIDUAL 2`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Componer** una escena temática 3D en Tinkercad importando al menos 5 elementos vectoriales `.SVG` sobre una base personalizada con tu nombre.
* **¿Para qué me sirve en la vida?** Para crear maquetas, dioramas, placas personalizadas, sellos o llaveros en 3D combinando íconos vectoriales listos sin dibujar cada silueta desde cero.

## 📚 CONTENIDO EXPLICATIVO (TEORÍA PUNTUAL — 10 MIN)
* **Mapa de bits (`.PNG`/`.JPG`) vs. Vector (`.SVG`):**
  * Una imagen **`.PNG`** está formada por cuadritos (píxeles); si la amplías mucho se ve borrosa y un software CAD 3D no puede convertir píxeles directos en volumen limpio.
  * Un archivo **`.SVG` (Gráficos Vectoriales Escalables)** guarda curvas y líneas matemáticas; conserva nitidez infinita y Tinkercad puede darle altura (`extrusión`) al instante.
* **Flujo paso a paso `svgrepo.com` -> Tinkercad 3D:**
  1. Buscar y descargar íconos simples en formato **`.SVG`** desde `svgrepo.com`.
  2. En Tinkercad 3D, usar **Importar**, ajustar la escala en `mm` si el vector llega demasiado grande y definir su altura de relieve (`Z`).
  3. Combinar mínimo 5 elementos `.SVG` distintos formando una escena coherente (ej. plato de comida, árbol de Navidad decorado o paisaje) sobre una base personalizada con nombre o iniciales en 3D.
* **Práctica individual (`👤 ACTIVIDAD INDIVIDUAL` — sin diseño resuelto):** Componer una escena temática 3D con mínimo 5 vectores `.SVG` distintos sobre una base con nombre 3D, cuidando alineación (`L`) y proporciones.
* **Preguntas de verificación:** ¿Por qué Tinkercad 3D necesita archivos `.SVG` y no `.PNG` directos? ¿Qué parámetro ajustamos en Tinkercad tras importar un `.SVG` para darle volumen?

---

# 5. Proyecto Grupal 3D: Vehículo / Carro — Parte 1 (`📘 PRÁCTICA EN EQUIPOS`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Modelar** en equipos la estructura principal (chasis y carrocería) de un vehículo 3D cuidando proporciones y pasos de rueda.
* **¿Para qué me sirve en la vida?** Para planificar diseños mecánicos compuestos por varias piezas que luego deberán ensamblarse con ejes móviles.

## 📚 CONTENIDO EXPLICATIVO Y AVANCE EN EQUIPOS
* **Fundamento técnico (5 min):**
  * **Diseño modular:** Antes de poner ruedas, un vehículo necesita un **chasis firme**, **carrocería** (cabina con parabrisas recortado o aerodinámica) y **espacios libres (guardafangos)** para que las ruedas no choquen con el cuerpo.
  * **Simetría:** Usar `L` (Alinear) sobre el eje central para que ambos lados del carro queden equilibrados.
* **Práctica en equipos:** Diseñar en equipo la base del chasis y la carrocería del vehículo (dejando los arcos o espacios libres para las 4 ruedas).
* **Preguntas de verificación:** ¿Por qué debemos dejar espacio libre alrededor de donde irán las ruedas?

---

# 6. Proyecto Grupal 3D: Vehículo / Carro — Parte 2 (`👥 ACTIVIDAD GRUPAL`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Ensamblar** ejes, ruedas con holgura (`0.3–0.5 mm`) y detalles finales en el vehículo 3D, exportándolo en formato `.STL` listo para impresión.
* **¿Para qué me sirve en la vida?** Para preparar un prototipo 3D real exportable a impresora 3D verificando que todas sus piezas apoyen bien y puedan girar.

## 📚 CONTENIDO Y RETO GRUPAL
* **Fundamento técnico (5 min):**
  * **Apoyo al suelo (`Z = 0`):** Las 4 ruedas deben tocar exactamente el plano de trabajo (`Z = 0`), mientras el chasis queda elevado por los ejes sin rozar el piso.
  * **Holgura de eje (`0.3–0.5 mm`):** Si el eje atraviesa un agujero del chasis, el agujero debe ser ligeramente más ancho que el eje para que pueda girar al imprimir.
  * **Formato `.STL`:** Formato universal de malla de triángulos que leen las impresoras 3D (laminadores).
* **Actividad grupal (`👥 ACTIVIDAD GRUPAL` — sin diseño resuelto):**
  * Completar el vehículo en equipo agregando los 2 ejes, las 4 ruedas alineadas al suelo (`Z = 0`) con holgura real, detalles (faros, alerón o matrícula) y exportarlo en `.STL`.
  * **1 Consejo:** Seleccionen las 4 ruedas y usen la vista frontal/lateral para comprobar que todas tocan el plano `Z = 0` por igual.
* **Preguntas de verificación:** ¿Para qué sirve exportar el diseño en formato `.STL`? ¿Qué pasa si el chasis toca el suelo más abajo que las ruedas?

---

# 7. Refuerzo 3D: Casa en Tinkercad y Autoevaluación (`🛠️ REFUERZO`)
## 🎯 PROPÓSITO Y ¿PARA QUÉ SIRVE?
* **Propósito:** **Consolidar** todas las herramientas 3D (vaciado, alineación, huecos, rotación y techo) modelando una vivienda completa y evaluando el dominio propio.
* **¿Para qué me sirve en la vida?** Para integrar múltiples técnicas de diseño CAD en un proyecto arquitectónico o de maqueta funcional.

## 📚 CONTENIDO, RETO Y AUTOEVALUACIÓN LIKERT (1 AL 5)
* **Repaso integrador (sin respuestas visibles):**
  * ¿Qué comando alinea objetos respecto a un borde o centro?
  * ¿Cuál es la diferencia práctica entre un archivo `.PNG`, un `.SVG` y un `.STL`?
  * ¿Por qué se añade `0.3–0.5 mm` de holgura entre un eje y su agujero?
* **Reto integrador (`🛠️ REFUERZO`):** Modelar una **Casa 3D** con muros huecos uniformes, 1 puerta, 2 ventanas pasantes, techo inclinado alineado y al menos 1 detalle exterior (jardín, cerca o placa `.SVG`).
* **Autoevaluación Escala de Likert (1 = Todavía me cuesta | 3 = Lo entiendo con ayuda | 5 = Lo domino y lo puedo explicar):**
  1. Utilizar ejes `X, Y, Z`, formas huecas y comandos clave (`L`, `Ctrl + G`, `Ctrl + D`).
  2. Aplicar medidas en milímetros y tolerancias/holguras reales (`0.3–0.5 mm`) en diseños funcionales.
  3. Descargar vectores `.SVG` e importarlos/extruirlos en Tinkercad 3D con proporciones coherentes.
  4. Ensamblar proyectos completos de varias piezas (Vehículo y Casa 3D) y exportarlos en `.STL`.
