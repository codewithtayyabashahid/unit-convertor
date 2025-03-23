#unit convertor
#buit a unit convertor using python and streamlit


import streamlit as st

# Apply custom CSS styles
st.markdown(
    """
    <style>
    body { background-color: #1e1e2f; color: white; }
    .stApp {
        background: linear-gradient(135deg, #1e1e2f);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1 { text-align: center; font-size: 36px; color: white; }
    .stButton>button {
        background: linear-gradient(45deg, #0b5394, #351c75);
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        transition: 0.3s;
        box-shadow: 0 5px 15px rgba(0, 201, 255, 0.4);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        color: black;
    }
    .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0 5px 15px rgba(0, 201, 255, 0.4);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: grey;
    }
    </style>       
    """,
    unsafe_allow_html=True
)

# Title & Description
st.markdown("<h1>Unit Converter using Python and Streamlit</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight, and temperature.")

# Sidebar menu
conversion_type = st.sidebar.selectbox("Select conversion type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter the value to convert", value=0.0, min_value=0.0, step=0.1)

# Layout for unit selection
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["meters", "kilometers", "centimeters", "millimeters", "miles", "feet", "yards", "inches"])
    with col2:
        to_unit = st.selectbox("To", ["meters", "kilometers", "centimeters", "millimeters", "miles", "feet", "yards", "inches"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["kilograms", "grams", "milligrams", "pounds", "ounces"])
    with col2:
        to_unit = st.selectbox("To", ["kilograms", "grams", "milligrams", "pounds", "ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["celsius", "fahrenheit", "kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["celsius", "fahrenheit", "kelvin"])

# Conversion functions
def length_conversion(value, from_unit, to_unit):
    length_units = {
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 100,
        'millimeters': 1000,
        'miles': 0.000621371,
        'feet': 3.28084,
        'yards': 1.09361,
        'inches': 39.37,
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_conversion(value, from_unit, to_unit):
    weight_units = {
        'kilograms': 1,
        'grams': 1000,
        'milligrams': 1000000,
        'pounds': 2.20462,
        'ounces': 35.274,
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == "celsius":
        return (value * 9/5 + 32) if to_unit == "fahrenheit" else value + 273.15 if to_unit == "kelvin" else value
    elif from_unit == "fahrenheit":
        return (value - 32) * 5/9 if to_unit == "celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "kelvin" else value
    elif from_unit == "kelvin":
        return value - 273.15 if to_unit == "celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "fahrenheit" else value
    return value

# Initialize result
result = None

# Button for conversion
if st.button("🚀 Convert"):
    if conversion_type == "Length":
        result = length_conversion(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_conversion(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_conversion(value, from_unit, to_unit)

# Display result only if it exists
if result is not None:
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.2f} {to_unit}</div>", unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <div class="footer">
        <p>Developed by <a href="https://github.com/codewithtayyabashahid" target="_blank">Tayyaba Shahid</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
