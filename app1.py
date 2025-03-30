import streamlit as st
import random

# Tabs
tabs = ["TCLL+", "TCLL-"]
seleccion = st.sidebar.selectbox("Selecciona un método: ", tabs)

titulo = seleccion + " 2x2"

st.title(titulo)

# Algoritmos
if seleccion == "TCLL+":
    gun_tcll = ["F2 R U R' F R U2 R'", "F R U2 R' F R U' R2 F R", "R U' R' F U' R' F R", "F R' F' R U R U' R2 F R2 U' R' F", "F U R' F' R2 U R2 F R", "R U2 R F' U' F R'"]
    hammer_tcll = ["R2 U R2 U' R2 U2 R U2 R'", "R' U2 R' U R' U F R F'", "R U R' U' R U' F R' F' U2 R'", "R' F R F' U' R' F R F' R U' R'", "F2 R' F2 R2 U R' U2 R' F R", "R U' R U' R' F R' F' R U' R'"]
    pinwheel_poser_tcll = ["F R' F' U R F R2 F' R2", "F U R U' R2 F' R F R' F' R", "R' U2 F R' F' U R2 U2 R", "F' U F2 R' F' R", "F2 R' F' R U2 F'", "R U' F R2 F' R'"]
    pinwheel_tcll = ["R2 U R' U R' U2 R U2 R' U2 R", "R' U2 R' U2 R2 F R' F' R'", "R2 F' R U2 R U R' F2 R"]
    spaceship_tcll = ["R U' R U2 R U' R U' R2" , "R U' R2 U R U F R2 F' U R U' R' U R", "R U2 R F R' F' R U2 R'", "F R' F' R U R U R' U2 R U R'", "L F L' U2 L' U' L F2", "F R F' R F R' F' R U R' U R"]
    stollery_tcll = ["R2 U R2 U' R U2 R' U2 R", "R U R' U' R U F R F' U' R'", "R2 U' R' F R' F' U' R U' R'", "R' U' R' U F R F' R U' R'", "R' F2 R F2 R' F2 R2 U R'", "F R' F' U R2 U R2 U' R"]
    turtle_tcll = ["R U R' U R U' R' U' R U R'", "R U' R' F2 R U R2 F' R F", "F R U R' F R U' R2 F' R", "R U2 R' U2 R' U F' U' F R U' R", "R U' F R' F' U' R'", "R' U2 R2 F R' F' U' R"]
    two_face_tcll = ["R U R' U' R U' R2 U R2", "F2 R U' R' U R' F2 R", "F' R' F R F U' R U R'", "R2 U R' F R F' R' U' R"]
elif seleccion == "TCLL-":
    gun_tcll = ["R2 U R2 U' R' U R' U'", "R U R' F2 R F2 R' F2 R'", "R U' R U F R' F' R2 U'", "U' F2 U F R' U2 F2 R' F' U", "R' F2 R U' R U R' F2", "R2 U' R' F R' F' U2 R U R'"]
    hammer_tcll = ["F' L F L' F' L F L'", "L' U' L U' F U2 F' ", "F R F' U2 R U2 R U R2", "R2 F' U F U2 F R' F'", "R U' R2 F R U R U' R' F'", "R U' R' U2 F R' F' R2 U2 R'"]
    pinwheel_poser_tcll = ["Sin algs en Pinwheel Poser por ahora..."]
    pinwheel_tcll = ["Sin algs en Pinwheel por ahora..."]
    spaceship_tcll = ["R U' R' U R U' R'", "R U' R' U R U R' F R' F' R2 U2 R'", "R' F R F' R' U2 R' U2 R", "F' R' F' R U R U R2 F' R", "R U R' F R' F' R U F R' F' R ", "R' F2 R U R' F2 R F' U R U' R'"]
    stollery_tcll = ["R U R' U F' R U' R' F2", "R' F R U' F' R U2 R' F2", "R' U' F R F' U R2 U' R'", "R U R' F R U R' U' R' F' R", "R2 F R F' U R U' R U' R2", "R U R' U F R F' R U R2"]
    turtle_tcll = ["R' U' R U R' U' R", "R' U2 R U R' F R' F' R2 U R' U' R", "R' F R' F' R U' R U' R' U R", "F R' F' R U R U2 R' U R U' R'", "R' F2 R U2 F' L F L'", "R' U' R U' R2 F R F' R"]
    two_face_tcll = ["R U2 R U2 R' U' R U' R2", "R' U F' U F U' R2 U' R2", "R U' R' U F' R' F' R F", "R2 U' R2 U R2 U R2 F' U F"]

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
    for alg in gun_tcll:
        casos.append(alg)

if opcion_hammer == True:
    for alg in hammer_tcll:
        casos.append(alg)

if opcion_pinwheel_poser == True:
    for alg in pinwheel_poser_tcll:
        casos.append(alg)

if opcion_pinwheel == True:
    for alg in pinwheel_tcll:
        casos.append(alg)

if opcion_spaceship == True:
    for alg in spaceship_tcll:
        casos.append(alg)

if opcion_stollery == True:
    for alg in stollery_tcll:
        casos.append(alg)

if opcion_turtle == True:
    for alg in turtle_tcll:
        casos.append(alg)

if opcion_two_face == True:
    for alg in two_face_tcll:
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