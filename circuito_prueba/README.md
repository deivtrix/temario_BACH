# 🧪 Circuito de Prueba (Velxio / Wokwi Simulator)

Este es un proyecto interactivo completo de prueba que contiene:
* **Arduino UNO**
* **LED Verde** conectado al **Pin 12** con resistencia de protección de $220\ \Omega$.
* **Pulsador Rojo** conectado al **Pin 2** y a `GND` con lógica de resistencia interna `INPUT_PULLUP`.
* **Monitor Serial** activo a 9600 baudios.

---

## 📁 Archivos del Proyecto:
1. 🔌 [diagram.json](file:///C:/Users/Master_Lab2_DavidC/Documents/LEV/temario_BACH/circuito_prueba/diagram.json): Mapa físico de componentes y cables.
2. 💻 [sketch.ino](file:///C:/Users/Master_Lab2_DavidC/Documents/LEV/temario_BACH/circuito_prueba/sketch.ino): Código C++ de Arduino listo para compilar y ejecutar.

---

## 🕹️ Cómo Probarlo:

### Opción 1: En VS Code (Con la extensión Velxio instalada)
1. Abre esta carpeta en VS Code (`Archivo > Abrir carpeta > circuito_prueba`).
2. Presiona `Ctrl + Shift + P`.
3. Escribe y selecciona: **`Velxio: Open Simulator`**.
4. Haz clic en el botón de **Play** para iniciar la simulación.
5. Haz clic con el mouse sobre el **Pulsador Rojo** y verás el LED verde encenderse y los mensajes aparecer en la consola serial.

### Opción 2: En la Web (velxio.dev o wokwi.com)
* Puedes arrastrar estos dos archivos o copiar su contenido directamente en [velxio.dev](https://velxio.dev) o [wokwi.com](https://wokwi.com) para simulación en el navegador.
