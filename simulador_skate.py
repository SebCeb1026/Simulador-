import customtkinter as ctk
import math
import tkinter as tk

# =========================
# CONFIGURACIÓN VENTANA
# =========================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("1400x800")
app.title("Simulador de Skate - Energía Mecánica")

# =========================
# DATOS FÍSICOS
# =========================

m = 60
g = 9.8
h = 6
longitud = 10.5
friccion = 120

energia_inicial = m * g * h
trabajo_friccion = friccion * longitud
energia_final = energia_inicial - trabajo_friccion

velocidad_final = math.sqrt((2 * energia_final) / m)

# =========================
# VARIABLES
# =========================

t = 0
running = False

# =========================
# FRAME IZQUIERDO
# =========================

left_frame = ctk.CTkFrame(
    app,
    width=350,
    corner_radius=20
)

left_frame.pack(side="left", fill="y", padx=20, pady=20)

title = ctk.CTkLabel(
    left_frame,
    text="SIMULADOR SKATE",
    font=("Arial", 30, "bold")
)

title.pack(pady=25)

# =========================
# INFORMACIÓN
# =========================

info_text = f"""
Masa: 60 kg

Altura: 6 m

Longitud: 10.5 m

Ángulo: 35°

Fricción: 120 N
"""

info_label = ctk.CTkLabel(
    left_frame,
    text=info_text,
    font=("Arial", 20),
    justify="left"
)

info_label.pack(pady=20)

velocidad_label = ctk.CTkLabel(
    left_frame,
    text="Velocidad: 0.00 m/s",
    font=("Arial", 24, "bold"),
    text_color="#4ade80"
)

velocidad_label.pack(pady=20)

energia_label = ctk.CTkLabel(
    left_frame,
    text=f"Energía inicial: {energia_inicial:.0f} J",
    font=("Arial", 18)
)

energia_label.pack(pady=10)

friccion_label = ctk.CTkLabel(
    left_frame,
    text=f"Trabajo fricción: -{trabajo_friccion:.0f} J",
    font=("Arial", 18),
    text_color="#f87171"
)

friccion_label.pack(pady=10)

# =========================
# CANVAS
# =========================

canvas = tk.Canvas(
    app,
    bg="#0f172a",
    highlightthickness=0
)

canvas.pack(fill="both", expand=True, padx=20, pady=20)

# =========================
# POSICIONES RAMPA
# =========================

start_x = 150
start_y = 150

end_x = 900
end_y = 600

# =========================
# BOTONES
# =========================

def iniciar():
    global running
    running = True

def reiniciar():
    global t, running
    t = 0
    running = False

btn_start = ctk.CTkButton(
    left_frame,
    text="Iniciar simulación",
    font=("Arial", 18),
    height=45,
    command=iniciar
)

btn_start.pack(pady=20)

btn_reset = ctk.CTkButton(
    left_frame,
    text="Reiniciar",
    font=("Arial", 18),
    height=45,
    fg_color="#ef4444",
    hover_color="#dc2626",
    command=reiniciar
)

btn_reset.pack(pady=10)

# =========================
# DIBUJAR ESCENA
# =========================

def draw_scene():

    canvas.delete("all")

    # Fondo degradado visual
    canvas.create_rectangle(
        0,0,2000,900,
        fill="#0f172a",
        outline=""
    )

    # Piso
    canvas.create_rectangle(
        0,650,2000,900,
        fill="#14532d",
        outline=""
    )

    # Rampa
    canvas.create_line(
        start_x,start_y,
        end_x,end_y,
        fill="#9ca3af",
        width=16
    )

    # Etiquetas
    canvas.create_text(
        start_x-30,
        start_y-20,
        text="A",
        fill="white",
        font=("Arial",24,"bold")
    )

    canvas.create_text(
        end_x+25,
        end_y,
        text="B",
        fill="white",
        font=("Arial",24,"bold")
    )

    canvas.create_text(
        start_x-80,
        380,
        text="h = 6 m",
        fill="white",
        font=("Arial",20)
    )

    canvas.create_text(
        start_x+80,
        start_y+50,
        text="35°",
        fill="white",
        font=("Arial",20)
    )

    # Posición patinador
    x = start_x + (end_x - start_x) * t
    y = start_y + (end_y - start_y) * t

    # Sombra
    canvas.create_oval(
        x-25,y-25,
        x+25,y+25,
        fill="#1d4ed8",
        outline=""
    )

    # Skate
    canvas.create_rectangle(
        x-35,y+25,
        x+35,y+35,
        fill="black",
        outline=""
    )

    # Ruedas
    canvas.create_oval(
        x-28,y+32,
        x-18,y+42,
        fill="#ef4444",
        outline=""
    )

    canvas.create_oval(
        x+18,y+32,
        x+28,y+42,
        fill="#ef4444",
        outline=""
    )

    # Flecha fricción
    canvas.create_line(
        x,y-45,
        x-90,y-45,
        fill="red",
        width=5,
        arrow=tk.LAST
    )

    canvas.create_text(
        x-130,
        y-65,
        text="Fricción",
        fill="red",
        font=("Arial",16,"bold")
    )

# =========================
# ACTUALIZAR
# =========================

def update():

    global t

    if running:

        t += 0.0025

        if t >= 1:
            t = 1

    velocidad_actual = velocidad_final * t

    velocidad_label.configure(
        text=f"Velocidad: {velocidad_actual:.2f} m/s"
    )

    draw_scene()

    app.after(16, update)

# =========================
# INICIAR
# =========================

update()

app.mainloop()
