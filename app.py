import streamlit as st

# Title and header
st.title("📊 Unit Converter App")


st.markdown("### 📈 Convert Weight, Time, and Temperature with ease")

# Category selection
category = st.selectbox("📈 Select Category", ["Weight ⚖️", "Time ⏱️", "Temperature ❄️"])

# Conversion function
def convert_units(category, value, unit):
    if category == "Weight ⚖️":
        if unit == "Kg to Pound":
            return value * 2.20462
        elif unit == "Pound to Kg":
            return value * 0.453592
    elif category == "Time ⏱️":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
    elif category == "Temperature ❄️":
        if unit == "Celsius to Fahrenheit":
            return (value * 9/5) + 32
        elif unit == "Fahrenheit to Celsius":
            return (value - 32) * 5/9

# Unit selection based on category
if category == "Weight ⚖️":
    unit = st.selectbox("⚖️ Select Conversion", ["Kg to Pound", "Pound to Kg"])
elif category == "Time ⏱️":
    unit = st.selectbox("⏱️ Select Conversion", ["Seconds to Minutes", "Minutes to Seconds", "Hours to Minutes", "Minutes to Hours"])
elif category == "Temperature ❄️":
    unit = st.selectbox("❄️ Select Conversion", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])

# Value input
value = st.number_input("Enter the value to convert")

# Convert button
if st.button("🔄 Convert"):
    result = convert_units(category, value, unit)
    st.success(f"🎉 The result is {result:.2f}")
