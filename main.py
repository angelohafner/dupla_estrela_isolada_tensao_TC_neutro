import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def polar_form(value):
    magnitude = abs(value)
    angle = np.angle(value, deg=True)
    return f"{magnitude:.2f} ∠ {angle:.2f}°"

# Entrada de dados
st.title("Cálculo da Tensão Máxima do Neutro em Circuitos de Dupla Estrela Isolada")

col1, col2, col3, col4 = st.columns(4)
with col1:
    V3f = st.number_input("Tensão trifásica (kV)", value=34.5) * 1e3
with col2:
    freq = st.number_input("Frequência (Hz)", value=60.0)
with col3:
    z_real = st.number_input("Parte real (Ω)", value=0.0)
with col4:
    z_imag = st.number_input("Parte imaginária (Ω)", value=-100.0)



# Cálculo do omega
omega = 2 * np.pi * freq

# Definição das tensões de fase
Van = V3f / np.sqrt(3) * np.exp(-1j * np.radians(30))
Vbn = V3f / np.sqrt(3) * np.exp(-1j * np.radians(150))
Vcn = V3f / np.sqrt(3) * np.exp(1j * np.radians(90))

# Impedância dos ramos
z = complex(z_real, z_imag)
Za1, Za2 = 10**10 * z, z
Za = 1 / (1/Za1 + 1/Za2)

Zb1, Zb2 = z, z
Zb = 1 / (1/Zb1 + 1/Zb2)

Zc1, Zc2 = z, z
Zc = 1 / (1/Zc1 + 1/Zc2)

# Montagem da matriz de impedâncias
Z_matrix = np.array([[Za + Zc, -Zc],
                     [-Zc, Zb + Zc]])

V_vector = np.array([V3f * np.exp(1j * np.radians(120)),
                     V3f * np.exp(-1j * np.radians(120))])

# Cálculo das correntes Iαβ
I_alpha_beta = np.linalg.inv(Z_matrix) @ V_vector

# Cálculo das correntes e tensões em cada ramo
Ia = -I_alpha_beta[0]
Ib = I_alpha_beta[1]
Ic = I_alpha_beta[0] - I_alpha_beta[1]

Vao = Ia * Za
Vbo = Ib * Zb
Vco = Ic * Zc

Von = Van - Vao

# Cálculo das correntes nos sub-ramos
Ia1 = Vao / Za1
Ia2 = Vao / Za2

Ib1 = Vbo / Zb1
Ib2 = Vbo / Zb2

Ic1 = Vco / Zc1
Ic2 = Vco / Zc2

In12 = Ia1 + Ib1 + Ic1
In21 = Ia2 + Ib2 + Ic2


# Diagrama fasorial das tensões
st.write(f"Von = {np.round(abs(Von)/1e3,2)} kV")
st.write(f"In12 = {np.round(abs(In12),2)} A")
fig_V, ax_V = plt.subplots()
colors = ['blue', 'red', 'green', 'purple']
for V, label, color in zip([Van, Vbn, Vcn, Von], ["Van", "Vbn", "Vcn", "Von"], colors):
    ax_V.arrow(0, 0, V.real / 1e3, V.imag / 1e3, head_width=1, head_length=1, fc=color, ec=color, label=label)

ax_V.set_xlabel("Real (kV)")
ax_V.set_ylabel("Imaginário (kV)")
ax_V.legend()
ax_V.grid(":")
ax_V.set_aspect('equal')
st.pyplot(fig_V)

# Diagrama fasorial das correntes
fig_I, ax_I = plt.subplots()
colors = ['blue', 'red', 'green', 'purple']
for I, label, color in zip([Ia, Ib, Ic, In12], ["Ia", "Ib", "Ic", "In12"], colors):
    ax_I.arrow(0, 0, I.real, I.imag, head_width=10, head_length=10, fc=color, ec=color, label=label)

ax_I.set_xlabel("Real (A)")
ax_I.set_ylabel("Imaginário (A)")
ax_I.legend()
ax_I.grid(":")
ax_I.set_aspect('equal')
st.pyplot(fig_I)

# Exibição dos resultados
st.write("### Resultados")
col1, col2, col3 = st.columns(3)
with col1:
    st.write(f"Van = {polar_form(Van)} V")
    st.write(f"Vbn = {polar_form(Vbn)} V")
    st.write(f"Vcn = {polar_form(Vcn)} V")
with col2:
    st.write(f"Vao = {polar_form(Vao)} V")
    st.write(f"Vbo = {polar_form(Vbo)} V")
    st.write(f"Vco = {polar_form(Vco)} V")
with col3:
    st.write(f"Ia = {polar_form(Ia)} A")
    st.write(f"Ib = {polar_form(Ib)} A")
    st.write(f"Ic = {polar_form(Ic)} A")

col1, col2, col3 = st.columns(3)
with col1:
    st.write(f"Ia1 = {polar_form(Ia1)} A")
    st.write(f"Ib1 = {polar_form(Ia2)} A")
    st.write(f"Ic1 = {polar_form(Ib1)} A")
with col2:
    st.write(f"Ia2 = {polar_form(Ib2)} A")
    st.write(f"Ib2 = {polar_form(Ic1)} A")
    st.write(f"Ic2 = {polar_form(Ic2)} A")
with col3:
    st.write(f"Von = {polar_form(Von)} V")
    st.write(f"In12 = {polar_form(In12)} A")
    st.write(f"In21 = {polar_form(In21)} A")