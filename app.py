import streamlit as st
import random
import string

# Initialize session state
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
if 'password_strength' not in st.session_state:
    st.session_state.password_strength = ""

# Dark mode toggle function
def toggle_dark_mode():
    st.session_state.dark_mode = not st.session_state.dark_mode

if st.checkbox("🌙 Dark Mode", value=st.session_state.dark_mode, on_change=toggle_dark_mode):
    st.session_state.dark_mode = not st.session_state.dark_mode

# Define CSS based on dark mode state
background_color = "#121212" if st.session_state.dark_mode else "#FFFFFF"
text_color = "#FFFFFF" if st.session_state.dark_mode else "#000000"
button_color = "white" if st.session_state.dark_mode else "green"

st.markdown(
    f"""
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: {background_color} !important;
            color: {text_color} !important;
        }}
        .stApp {{
            background-color: {background_color} !important;
            color: {text_color} !important;
        }}
        .title {{text-align: center; font-size: 24px; font-weight: bold;}}
        .slider {{color: red;}}
        .password-box {{border: 1px solid #ccc; padding: 10px; border-radius: 5px;}}
        .btn {{display: block; width: 100%; margin-top: 10px; padding: 10px; border-radius: 5px;}}
        .btn-color {{background-color: {button_color}; color: black; border: 1px solid black;}}
    </style>
    """,
    unsafe_allow_html=True,
)

# Password strength checker
def check_password_strength(password):
    length = len(password)
    if length < 6:
        return "Weak 🔴"
    elif length < 10:
        return "Moderate 🟡"
    else:
        return "Strong 🟢"

st.title("Password Strength Meter")
st.subheader("Check password strength and generate secure passwords.")
password = st.text_input("Enter Password:", type="password")
if st.button("Check Strength", key="check", help="Analyze password strength", use_container_width=True):
    st.session_state.password_strength = check_password_strength(password)
st.write(f"Password Strength: {st.session_state.password_strength}")

# Password generator
st.subheader("🔑 Generate Secure Password")
length = st.slider("Password Length:", min_value=8, max_value=24, value=12)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

if st.button("Generate Password", key="generate", use_container_width=True, help="Generate a secure password"):
    new_password = generate_password(length)
    st.text_input("Generated Password:", new_password, key="output", disabled=True)

# Clear history button
st.button("🗑️ Clear History", key="clear", use_container_width=True, help="Clear stored passwords")

# Recent Passwords section
st.subheader("📜 Recent Passwords")

# Footer
st.markdown("Made by Rizwana Ali")





