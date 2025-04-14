import streamlit as st

# Length convert karne wali function
def convert_length(input_value, conversion_type):
    if conversion_type == "Kilometers to Miles":
        return f"{input_value} km equals {input_value * 0.621371} miles"
    elif conversion_type == "Miles to Kilometers":
        return f"{input_value} miles equals {input_value * 1.60934} km"

# Weight convert karne wali function
def convert_weight(input_value, conversion_type):
    if conversion_type == "Kilograms to Pounds":
        return f"{input_value} kg equals {input_value * 2.20462} pounds"
    elif conversion_type == "Pounds to Kilograms":
        return f"{input_value} pounds equals {input_value * 0.453592} kg"

# Temperature convert karne wali function
def convert_temperature(input_value, conversion_type):
    if conversion_type == "Celsius to Fahrenheit":
        return f"{input_value}°C is {(input_value * 9/5) + 32}°F"
    elif conversion_type == "Fahrenheit to Celsius":
        return f"{input_value}°F equals {(input_value - 32) * 5/9}°C"

# Main function for app interface
def app():
    st.title("Universal Unit Converter")  # App ka title
    st.subheader("Convert Length, Weight, or Temperature with Ease")  # Subheader

    # User se yeh poochhna ke wo kis category ko convert karna chahte hain
    category = st.selectbox("Pick a Conversion Category", ["Length", "Weight", "Temperature"])

    if category == "Length":
        conversion_option = st.radio("Choose Conversion Direction", ["Kilometers to Miles", "Miles to Kilometers"])
        number_input = st.number_input("Enter Value", min_value=0.0, format="%.2f")  # Value ka input
        if st.button("Convert Now"):  # Jab button press kiya jaye
            st.success(convert_length(number_input, conversion_option))  # Result dikhayein

    elif category == "Weight":
        conversion_option = st.radio("Choose Conversion Direction", ["Kilograms to Pounds", "Pounds to Kilograms"])
        number_input = st.number_input("Enter Value", min_value=0.0, format="%.2f")  # Value ka input
        if st.button("Convert Now"):  # Jab button press kiya jaye
            st.success(convert_weight(number_input, conversion_option))  # Result dikhayein

    elif category == "Temperature":
        conversion_option = st.radio("Choose Conversion Direction", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
        number_input = st.number_input("Enter Value", format="%.2f")  # Value ka input
        if st.button("Convert Now"):  # Jab button press kiya jaye
            st.success(convert_temperature(number_input, conversion_option))  # Result dikhayein

# App ko run karna
if __name__ == "__main__":
    app()
