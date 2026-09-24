import os
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, Image
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.graphics.shapes import Drawing, Line, Polygon, Rect

pdf_path = r"C:\Users\David\Desktop\clases bach\ESQUEMA_SECUENCIALIDAD_ROBOTICA.pdf"
logo_path = r"C:\Users\David\Desktop\clases bach\logo.png"

# A4 Landscape dimensions: 841.89 pt x 595.27 pt
# Usamos marges ultramínimos de 4pt para maximizar el área útil (833.89 pt x 587.27 pt)
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=landscape(A4),
    rightMargin=4,
    leftMargin=4,
    topMargin=4,
    bottomMargin=4
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'GTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=14,
    leading=16,
    textColor=colors.HexColor('#0F172A'),
    alignment=TA_LEFT
)

sub_style = ParagraphStyle(
    'GSub',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=12,
    textColor=colors.HexColor('#2563EB'),
    alignment=TA_LEFT
)

axis_header_style = ParagraphStyle(
    'GAxisHeader',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=12,
    textColor=colors.white,
    alignment=TA_CENTER
)

course_header_egb = ParagraphStyle(
    'GCourseEGB',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=12,
    textColor=colors.white,
    alignment=TA_CENTER
)

course_header_bgu = ParagraphStyle(
    'GCourseBGU',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=12,
    textColor=colors.white,
    alignment=TA_CENTER
)

# Aumentamos la fuente de los textos de 7.8pt a 8.2pt (leading 10.5pt) para mayor presencia visual
topic_card_title_style = ParagraphStyle(
    'GCardTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=8.2,
    leading=10.2,
    textColor=colors.HexColor('#0F172A'),
    alignment=TA_CENTER
)

topic_card_desc_style = ParagraphStyle(
    'GCardDesc',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=7.4,
    leading=9.4,
    textColor=colors.HexColor('#475569'),
    alignment=TA_CENTER
)

def create_google_arrow(color_hex='#4285F4'):
    # Flechas vectoriales de 16pt de alto para extender la conexión vertical
    d = Drawing(187, 16)
    d.add(Line(93.5, 16, 93.5, 3, strokeColor=colors.HexColor(color_hex), strokeWidth=2.2))
    d.add(Polygon([89.5, 5.0, 97.5, 5.0, 93.5, 0], fillColor=colors.HexColor(color_hex), strokeColor=colors.HexColor(color_hex)))
    return d

def make_card(badge_letter, badge_color_hex, title, desc):
    return [
        Paragraph(f"<font color='{badge_color_hex}'><b>[{badge_letter}]</b></font> <b>{title}</b>", topic_card_title_style),
        Spacer(1, 2),
        Paragraph(desc, topic_card_desc_style)
    ]

story = []

# Encabezado
logo_img = Image(logo_path, width=74.66, height=34.0)

text_block = [
    Paragraph("UNIDAD EDUCATIVA LEV VYGOTSKY", title_style),
    Spacer(1, 1),
    Paragraph("Plan Curricular de Robótica", sub_style)
]

badge_p = Paragraph("<font color='#2563EB'>●</font> <b>2026 - 2027</b>", ParagraphStyle('BYear', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=10.5, textColor=colors.HexColor('#0F172A'), alignment=TA_RIGHT))

header_table_data = [
    [logo_img, text_block, badge_p]
]

header_table = Table(header_table_data, colWidths=[85, 545, 203])
header_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('ALIGN', (0,0), (0,0), 'LEFT'),
    ('ALIGN', (1,0), (1,0), 'LEFT'),
    ('ALIGN', (2,0), (2,0), 'RIGHT'),
    ('PADDING', (0,0), (-1,-1), 0),
]))

story.append(header_table)
story.append(Spacer(1, 3))

# Barra de Acento Multicolor Google
bar_drawing = Drawing(833, 3)
bar_drawing.add(Rect(0, 0, 208.25, 3, fillColor=colors.HexColor('#4285F4'), strokeColor=None))
bar_drawing.add(Rect(208.25, 0, 208.25, 3, fillColor=colors.HexColor('#EA4335'), strokeColor=None))
bar_drawing.add(Rect(416.5, 0, 208.25, 3, fillColor=colors.HexColor('#FBBC05'), strokeColor=None))
bar_drawing.add(Rect(624.75, 0, 208.25, 3, fillColor=colors.HexColor('#34A853'), strokeColor=None))

story.append(bar_drawing)
story.append(Spacer(1, 4))

# Encabezados de Ejes
row_headers = [
    Paragraph("<b>Nivel / Año</b>", ParagraphStyle('H0', parent=axis_header_style, textColor=colors.HexColor('#0F172A'))),
    Paragraph("<b>EJE 1: CAD 3D & Fabricación</b>", ParagraphStyle('H1', parent=axis_header_style, textColor=colors.white)),
    Paragraph("<b>EJE 2: Electrónica & Displays</b>", ParagraphStyle('H2', parent=axis_header_style, textColor=colors.white)),
    Paragraph("<b>EJE 3: Lógica & Control ADC</b>", ParagraphStyle('H3', parent=axis_header_style, textColor=colors.HexColor('#0F172A'))),
    Paragraph("<b>EJE 4: Telemetría & Mecatrónica</b>", ParagraphStyle('H4', parent=axis_header_style, textColor=colors.white)),
]

# 8VO EGB
row_8vo = [
    Paragraph("<b>8VO EGB</b>", course_header_egb),
    make_card("A", "#2563EB", "Diseño 3D Inicial y Geometría", "Construcción tridimensional de Taza de Chocolate en Tinkercad."),
    make_card("B", "#DC2626", "Diseño 3D Técnico y Estructuras", "Modelado paramétrico de Vehículo / Carro 3D."),
    make_card("C", "#D97706", "Modelado Simétrico y Modificadores", "Diseño de personaje Among Us con efecto espejo."),
    make_card("D", "#16A34A", "Vectores 2D y Logotipos 3D", "Diseño de llaveros en Inkscape y extrusión tridimensional.")
]

row_arrow_1 = ["", create_google_arrow('#2563EB'), create_google_arrow('#DC2626'), create_google_arrow('#D97706'), create_google_arrow('#16A34A')]

# 9NO EGB
row_9no = [
    Paragraph("<b>9NO EGB</b>", course_header_egb),
    make_card("B", "#2563EB", "Modelado 3D Complejo", "Diseño de Casa Caricatura y generación de Litofanías 3D."),
    make_card("C", "#DC2626", "Fundamentos de Electrónica", "Energía eléctrica y montaje de circuitos Serie y Paralelo."),
    make_card("D", "#D97706", "Programación de Robots", "mBlock por bloques y control de movimientos del mBot."),
    make_card("A", "#16A34A", "Navegación Autónoma", "Programación de rutina de trayectoria cuadrada en mBot.")
]

row_arrow_2 = ["", create_google_arrow('#2563EB'), create_google_arrow('#DC2626'), create_google_arrow('#D97706'), create_google_arrow('#16A34A')]

# 10MO EGB
row_10mo = [
    Paragraph("<b>10MO EGB</b>", course_header_egb),
    make_card("C", "#2563EB", "Salidas Digitales y LEDs", "Introducción a Arduino, función Blink y secuencias luminosas."),
    make_card("A", "#DC2626", "Entradas Digitales y Pulsadores", "Lectura de estado binario con resistencias Pull-up."),
    make_card("B", "#D97706", "Lógica de Control Algorítmica", "Toma de decisiones condicionales con estructuras if / else."),
    make_card("D", "#16A34A", "Salidas Analógicas y Variación", "Modulación por ancho de pulso PWM y fading de luces.")
]

row_arrow_3 = ["", create_google_arrow('#2563EB'), create_google_arrow('#DC2626'), create_google_arrow('#D97706'), create_google_arrow('#16A34A')]

# 1RO BGU
row_1ro_bgu = [
    Paragraph("<b>1RO BGU</b>", course_header_bgu),
    make_card("A", "#2563EB", "CAD 3D Técnico y Tolerancias", "Dimensionamiento milimétrico exacto, acotado y regla."),
    make_card("B", "#DC2626", "Programación Estructurada C++", "Secuenciadores C++, Semáforos y efectos PWM."),
    make_card("C", "#D97706", "Entradas Digitales de Seguridad", "Control de pulsadores e integración lógica industrial."),
    make_card("D", "#16A34A", "Telemetría y Puerto Serial", "Protocolo UART (9600 bps), buffer serial y comandos PC.")
]

row_arrow_4 = ["", create_google_arrow('#2563EB'), create_google_arrow('#DC2626'), create_google_arrow('#D97706'), create_google_arrow('#16A34A')]

# 2DO BGU
row_2do_bgu = [
    Paragraph("<b>2DO BGU</b>", course_header_bgu),
    make_card("A", "#2563EB", "Enclosures y Carcasas 3D", "Diseño de carcasas ahuecadas para alojar placas PCB y protoboards."),
    make_card("B", "#DC2626", "Interfaces Visuales de Salida", "Displays de 7 segmentos y pantallas LCD 16x2 (LiquidCrystal)."),
    make_card("C", "#D97706", "Entradas Análogas y ADC", "Conversión ADC (10-bits, 0-1023), función map() y LDR."),
    make_card("D", "#16A34A", "Termometría y Alarmas Sonoras", "Sensor de temperatura TMP36 y alertas con Buzzer.")
]

row_arrow_5 = ["", create_google_arrow('#2563EB'), create_google_arrow('#DC2626'), create_google_arrow('#D97706'), create_google_arrow('#16A34A')]

# 3RO BGU
row_3ro_bgu = [
    Paragraph("<b>3RO BGU</b>", course_header_bgu),
    make_card("A", "#2563EB", "Etapa de Potencia con BJT", "Transistor NPN como conmutador para aislamiento de corriente."),
    make_card("B", "#DC2626", "Control de Motores DC", "Regulación de velocidad por PWM e indicadores de marcha."),
    make_card("C", "#D97706", "Actuadores Mecánicos y Drivers", "Puente H L298N para inversión de giro y Servomotores."),
    make_card("D", "#16A34A", "Sensores Ultrasónicos", "Medición de tiempo de vuelo con HC-SR04 y cálculo de distancia.")
]

table_data = [
    row_headers,
    row_8vo,
    row_arrow_1,
    row_9no,
    row_arrow_2,
    row_10mo,
    row_arrow_3,
    row_1ro_bgu,
    row_arrow_4,
    row_2do_bgu,
    row_arrow_5,
    row_3ro_bgu
]

# Ancho Total = 833 pt -> ColWidths: Course (85), Eje 1 (187), Eje 2 (187), Eje 3 (187), Eje 4 (187)
t_vertical = Table(table_data, colWidths=[85, 187, 187, 187, 187])

t_vertical.setStyle(TableStyle([
    # Eje Headers: Google 4 Colors Vibrantes
    ('BACKGROUND', (0,0), (0,0), colors.HexColor('#E2E8F0')),
    ('BACKGROUND', (1,0), (1,0), colors.HexColor('#2563EB')),
    ('BACKGROUND', (2,0), (2,0), colors.HexColor('#DC2626')),
    ('BACKGROUND', (3,0), (3,0), colors.HexColor('#F59E0B')),
    ('BACKGROUND', (4,0), (4,0), colors.HexColor('#16A34A')),
    ('VALIGN', (0,0), (-1,0), 'MIDDLE'),
    ('BOTTOMPADDING', (0,0), (-1,0), 6),
    ('TOPPADDING', (0,0), (-1,0), 6),

    # Colors Años / Cursos
    ('BACKGROUND', (0,1), (0,1), colors.HexColor('#5B21B6')),
    ('BOX', (0,1), (0,1), 1, colors.HexColor('#4C1D95')),
    ('BACKGROUND', (0,3), (0,3), colors.HexColor('#5B21B6')),
    ('BOX', (0,3), (0,3), 1, colors.HexColor('#4C1D95')),
    ('BACKGROUND', (0,5), (0,5), colors.HexColor('#5B21B6')),
    ('BOX', (0,5), (0,5), 1, colors.HexColor('#4C1D95')),

    ('BACKGROUND', (0,7), (0,7), colors.HexColor('#1E293B')),
    ('BOX', (0,7), (0,7), 1, colors.HexColor('#0F172A')),
    ('BACKGROUND', (0,9), (0,9), colors.HexColor('#1E293B')),
    ('BOX', (0,9), (0,9), 1, colors.HexColor('#0F172A')),
    ('BACKGROUND', (0,11), (0,11), colors.HexColor('#1E293B')),
    ('BOX', (0,11), (0,11), 1, colors.HexColor('#0F172A')),

    # Tarjetas Eje 1 (Borde Azul Real)
    ('BACKGROUND', (1,1), (1,11), colors.HexColor('#FFFFFF')),
    ('BOX', (1,1), (1,1), 0.5, colors.HexColor('#93C5FD')),
    ('BOX', (1,3), (1,3), 0.5, colors.HexColor('#93C5FD')),
    ('BOX', (1,5), (1,5), 0.5, colors.HexColor('#93C5FD')),
    ('BOX', (1,7), (1,7), 0.5, colors.HexColor('#93C5FD')),
    ('BOX', (1,9), (1,9), 0.5, colors.HexColor('#93C5FD')),
    ('BOX', (1,11), (1,11), 0.5, colors.HexColor('#93C5FD')),

    # Tarjetas Eje 2 (Borde Rojo)
    ('BACKGROUND', (2,1), (2,11), colors.HexColor('#FFFFFF')),
    ('BOX', (2,1), (2,1), 0.5, colors.HexColor('#FCA5A5')),
    ('BOX', (2,3), (2,3), 0.5, colors.HexColor('#FCA5A5')),
    ('BOX', (2,5), (2,5), 0.5, colors.HexColor('#FCA5A5')),
    ('BOX', (2,7), (2,7), 0.5, colors.HexColor('#FCA5A5')),
    ('BOX', (2,9), (2,9), 0.5, colors.HexColor('#FCA5A5')),
    ('BOX', (2,11), (2,11), 0.5, colors.HexColor('#FCA5A5')),

    # Tarjetas Eje 3 (Borde Ámbar)
    ('BACKGROUND', (3,1), (3,11), colors.HexColor('#FFFFFF')),
    ('BOX', (3,1), (3,1), 0.5, colors.HexColor('#FDE68A')),
    ('BOX', (3,3), (3,3), 0.5, colors.HexColor('#FDE68A')),
    ('BOX', (3,5), (3,5), 0.5, colors.HexColor('#FDE68A')),
    ('BOX', (3,7), (3,7), 0.5, colors.HexColor('#FDE68A')),
    ('BOX', (3,9), (3,9), 0.5, colors.HexColor('#FDE68A')),
    ('BOX', (3,11), (3,11), 0.5, colors.HexColor('#FDE68A')),

    # Tarjetas Eje 4 (Borde Verde)
    ('BACKGROUND', (4,1), (4,11), colors.HexColor('#FFFFFF')),
    ('BOX', (4,1), (4,1), 0.5, colors.HexColor('#86EFAC')),
    ('BOX', (4,3), (4,3), 0.5, colors.HexColor('#86EFAC')),
    ('BOX', (4,5), (4,5), 0.5, colors.HexColor('#86EFAC')),
    ('BOX', (4,7), (4,7), 0.5, colors.HexColor('#86EFAC')),
    ('BOX', (4,9), (4,9), 0.5, colors.HexColor('#86EFAC')),
    ('BOX', (4,11), (4,11), 0.5, colors.HexColor('#86EFAC')),

    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('BOTTOMPADDING', (0,2), (-1,2), 0),
    ('TOPPADDING', (0,2), (-1,2), 0),
    ('BOTTOMPADDING', (0,4), (-1,4), 0),
    ('TOPPADDING', (0,4), (-1,4), 0),
    ('BOTTOMPADDING', (0,6), (-1,6), 0),
    ('TOPPADDING', (0,6), (-1,6), 0),
    ('BOTTOMPADDING', (0,8), (-1,8), 0),
    ('TOPPADDING', (0,8), (-1,8), 0),
    ('BOTTOMPADDING', (0,10), (-1,10), 0),
    ('TOPPADDING', (0,10), (-1,10), 0),

    # AUMENTAMOS EL PADDING INTERNO A 7.5 pt (ARRIBA Y ABAJO) PARA QUE LAS CAJAS LLENEN EL ESPACIO VERTICAL
    ('BOTTOMPADDING', (0,1), (-1,1), 7.5),
    ('TOPPADDING', (0,1), (-1,1), 7.5),
    ('BOTTOMPADDING', (0,3), (-1,3), 7.5),
    ('TOPPADDING', (0,3), (-1,3), 7.5),
    ('BOTTOMPADDING', (0,5), (-1,5), 7.5),
    ('TOPPADDING', (0,5), (-1,5), 7.5),
    ('BOTTOMPADDING', (0,7), (-1,7), 7.5),
    ('TOPPADDING', (0,7), (-1,7), 7.5),
    ('BOTTOMPADDING', (0,9), (-1,9), 7.5),
    ('TOPPADDING', (0,9), (-1,9), 7.5),
    ('BOTTOMPADDING', (0,11), (-1,11), 7.5),
    ('TOPPADDING', (0,11), (-1,11), 7.5),
]))

story.append(t_vertical)

doc.build(story)
print("PDF maximizado para cubrir el 100% de la pagina A4 sin dejar vacios!")
