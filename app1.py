import streamlit as st
import random

# Algoritmos
gun_tcll_plus = ["F2 R U R' F R U2 R'", "F R U2 R' F R U' R2 F R", "R U' R' F U' R' F R", "F R' F' R U R U' R2 F R2 U' R' F", "F U R' F' R2 U R2 F R", "R U2 R F' U' F R'"]
hammer_tcll_plus = ["R2 U R2 U' R2 U2 R U2 R'", "R' U2 R' U R' U F R F'", "R U R' U' R U' F R' F' U2 R'", "R' F R F' U' R' F R F' R U' R'", "F2 R' F2 R2 U R' U2 R' F R", "R U' R U' R' F R' F' R U' R'"]
pinwheel_poser_tcll_plus = ["F R' F' U R F R2 F' R2", "F U R U' R2 F' R F R' F' R", "R' U2 F R' F' U R2 U2 R", "F' U F2 R' F' R", "F2 R' F' R U2 F'", "R U' F R2 F' R'"]
pinwheel_tcll_plus = ["R2 U R' U R' U2 R U2 R' U2 R", "R' U2 R' U2 R2 F R' F' R'", "R2 F' R U2 R U R' F2 R"]
spaceship_tcll_plus = ["R U' R U2 R U' R U' R2" , "R U' R2 U R U F R2 F' U R U' R' U R", "R U2 R F R' F' R U2 R'", "F R' F' R U R U R' U2 R U R'", "L F L' U2 L' U' L F2", "F R F' R F R' F' R U R' U R"]
stollery_tcll_plus = ["R2 U R2 U' R U2 R' U2 R", "R U R' U' R U F R F' U' R'", "R2 U' R' F R' F' U' R U' R'", "R' U' R' U F R F' R U' R'", "R' F2 R F2 R' F2 R2 U R'", "F R' F' U R2 U R2 U' R"]
turtle_tcll_plus = ["R U R' U R U' R' U' R U R'", "R U' R' F2 R U R2 F' R F", "F R U R' F R U' R2 F' R", "R U2 R' U2 R' U F' U' F R U' R", "R U' F R' F' U' R'", "R' U2 R2 F R' F' U' R"]
two_face_tcll_plus = ["R U R' U' R U' R2 U R2", "F2 R U' R' U R' F2 R", "F' R' F R F U' R U R'", "R2 U R' F R F' R' U' R"]

st.title("Generar casos de TCLL 2x2")

opcion_gun = st.toggle("Gun")
opcion_hammer = st.toggle("Hammer")
opcion_pinwheel_poser = st.toggle("Pinwheel Poser")
opcion_pinwheel = st.toggle("Pinwheel")
opcion_spaceship = st.toggle("Spaceship")
opcion_stollery = st.toggle("Stollery")
opcion_turtle = st.toggle("Turtle")
opcion_two_face = st.toggle("Two Face")

casos = []

if opcion_gun == True:
    for alg in gun_tcll_plus:
        casos.append(alg)

if opcion_hammer == True:
    for alg in hammer_tcll_plus:
        casos.append(alg)

if opcion_pinwheel_poser == True:
    for alg in pinwheel_poser_tcll_plus:
        casos.append(alg)

if opcion_pinwheel == True:
    for alg in pinwheel_tcll_plus:
        casos.append(alg)

if opcion_spaceship == True:
    for alg in spaceship_tcll_plus:
        casos.append(alg)

if opcion_stollery == True:
    for alg in stollery_tcll_plus:
        casos.append(alg)

if opcion_turtle == True:
    for alg in turtle_tcll_plus:
        casos.append(alg)

if opcion_two_face == True:
    for alg in two_face_tcll_plus:
        casos.append(alg)

if not len(casos) == 0:
    try:
        # Botón para cambiar de algoritmo
        if st.button("Siguiente algoritmo"):
            st.session_state.alg_random = random.randint(0, len(casos) - 1)

        # Inicializar la variable en la sesión si no existe
        if "alg_random" not in st.session_state:
            st.session_state.alg_random = random.randint(0, len(casos) - 1)

        st.write(casos[st.session_state.alg_random])
    except IndexError:
        pass