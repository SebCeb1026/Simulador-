import streamlit as st
import math
import time

st.set_page_config(
    page_title="Simulador Skate",
    layout="wide"
)

# ==========================
# ESTILO
# ==========================

st.markdown("""
<style>

.big-title{
    font-size:45px;
    font-weight:bold;
    color:#2563eb;
}

.card{
    background-color:#111827;
    padding:20px;
    border-radius:20px;
    color:white;
    margin-bottom:20px;
}

.metric{
    font-size:30px;
    color:#4ade80;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# DATOS
# ==========================

m = 60
g = 9.8
h = 6
d = 10.5
friccion = 120

energia_inicial = m * g * h
trabajo_friccion = friccion * d
energia_final = energia_inicial - trabajo_friccion

v_final = math.sqrt((2 * energia_final) / m)

# ==========================
# TÍTULO
# ==========================

st.markdown(
    '<p class="big-title">🛹 Simulador de Skate</p>',
    unsafe_allow_html=True
)

# ==========================
# COLUMNAS
# ==========================

col1, col2 = st.columns([1,2])

# ==========================
# PANEL IZQUIERDO
# ==========================

with col1:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Datos físicos")

    st.write(f"**Masa:** {m} kg")
    st.write(f"**Altura:** {h} m")
    st.write(f"**Longitud:** {d} m")
    st.write(f"**Ángulo:** 35°")
    st.write(f"**Fricción:** {friccion} N")

    st.markdown("---")

    st.write(f"**Energía inicial:** {energia_inicial:.0f} J")
    st.write(f"**Trabajo de fricción:** -{trabajo_friccion:.0f} J")

    st.markdown('</div>', unsafe_allow_html=True)

# ==========================
# ANIMACIÓN
# ==========================

with col2:

    st.subheader("Movimiento del patinador")

    progress_bar = st.progress(0)

    velocity_text = st.empty()

    animation = st.empty()

    if st.button("▶ Iniciar simulación"):

        for i in range(101):

            t = i / 100

            velocidad = v_final * t

            progress_bar.progress(i)

            velocity_text.markdown(
                f'<p class="metric">Velocidad: {velocidad:.2f} m/s</p>',
                unsafe_allow_html=True
            )

            skate_position = int(t * 40)

            pista = "🛹" + "-" * skate_position + "⬇"

            animation.markdown(f"## {pista}")

            time.sleep(0.03)

        st.success(
            f"Velocidad final: {v_final:.2f} m/s"
        )
