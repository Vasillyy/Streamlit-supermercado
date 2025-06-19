import streamlit as st
import pandas as pd

def calcular_subtotal(producto_nombre, precio_producto, cantidad_producto):
    subtotal = float(precio_producto) * float(cantidad_producto)
    nueva_fila = {
        "producto": producto_nombre,
        "precio": precio_producto,
        "cantidad": cantidad_producto,
        "subtotal": subtotal
    }
    st.session_state.table_data = pd.concat(
        [st.session_state.table_data, pd.DataFrame([nueva_fila])],
        ignore_index=True
    )

if "table_data" not in st.session_state:
    st.session_state.table_data = pd.DataFrame(
        columns=["producto", "precio", "cantidad", "subtotal"]
    )

st.title("Supermercado Dia")

with st.form("producto_form"):
    producto_nombre = st.text_input("Ingrese el nombre del producto")
    precio_producto = st.number_input("Ingrese el precio del producto")
    cantidad_producto = st.number_input("Ingrese la cantidad")
    subtotal_button = st.form_submit_button("Calcular subtotal")

if subtotal_button:
    if producto_nombre and precio_producto > 0 and cantidad_producto > 0:
        calcular_subtotal(producto_nombre, precio_producto, cantidad_producto)
    else:
        st.warning("Por favor, ingrese un producto válido." \
        " El precio y la cantidad deben ser mayores a 0.")

st.dataframe(st.session_state.table_data)

if st.button("Calcular Total"):
    total=st.session_state.total = st.session_state.table_data["subtotal"].sum()

    st.subheader("Total")
    st.write("El precio total es "+ str(total))