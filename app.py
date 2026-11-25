import streamlit as st
import requests

"""
# Zoologist front
"""

st.markdown(
    """
Remember that there are several ways to output content into your web page...

Either like the title above by just creating a string (or an f-string) starting. Or like this paragraph using the `st.` function.
"""
)


## User inputs
island = st.selectbox("Island", ["Biscoe", "Dream", "Torgersen"])
bill_length_mm = st.slider("Bill length (mm)", min_value=30.0, max_value=60.0, value=40.0, step=0.1)
bill_depth_mm = st.slider("Bill depth (mm)", min_value=10.0, max_value=25.0, value=15.0, step=0.1)
flipper_length_mm = st.slider("Flipper length (mm)", min_value=100.0, max_value=300.0, value=200.0, step=0.1)
body_mass_g = st.slider("Body mass (g)", min_value=2500.0, max_value=7000.0, value=2800.0, step=0.1)
sex = st.radio("Sex", ["Male", "Female"])

## Call the API
url = "http://localhost:8000/predict"

if st.button("Predict species"):
    params = {
        "island": island,
        "bill_length_mm": bill_length_mm,
        "bill_depth_mm": bill_depth_mm,
        "flipper_length_mm": flipper_length_mm,
        "body_mass_g": body_mass_g,
        "sex": sex,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        prediction = response.json()
        st.success(f"This penguin is a {prediction['species']}")
    else:
        st.error(f"API error {response.status_code}: {response.text}")
