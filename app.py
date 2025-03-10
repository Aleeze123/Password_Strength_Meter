import streamlit as st
import random
import string
def password_strength(password):
    score = 0
    feedback = []
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔴 Password should be at least 8 characters long. 🚫")
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("🟠 Include at least one uppercase letter.🔑")
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("🟡 Include at least one lowercase letter.🔓")
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("🟢 Include at least one number. 🔢")
    if any(char in "!@#$%^&*()_+[]{}|;:,.<>?" for char in password):
        score += 1
    else:
        feedback.append(" Include at least one special character.🛡️")
    return score, feedback
def get_strength_label(score):
    if score == 0:
        return 'Weak 🔴', 'red'
    elif score == 1:
        return 'Weak 🟠', 'orange'
    elif score == 2:
        return 'Medium 🟡', 'yellow'
    elif score == 3:
        return 'Strong 🟢', 'blue'
    elif score == 4:
        return 'Very Strong 🔵', 'blue'
    elif score == 5:
        return 'Very Strong 🔥', 'blue'
def generate_password(length, include_uppercase, include_special, include_numbers):
    characters = string.ascii_lowercase  
    if include_uppercase:
        characters += string.ascii_uppercase  
    if include_special:
        characters += string.punctuation
    if include_numbers:
        characters += string.digits  
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")
st.markdown("""
    <style>
    h1 {
        color: #4CAF50;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    footer {
        text-align: center;
        font-size: 12px;
        color: #999;
        margin-top: 50px;
    }
    .stButton > button {
        background-color: black; 
        border: 2px solid blue; 
        border-radius: 8px; 
        color: white;
        padding: 10px 20px; 
        font-size: 16px;
        font-weight: bold;
        cursor: pointer; 
        transition: 0.3s ease; 
    }
    .stButton > button:hover {
        background-color: black;
        border-color: lightblue; 
        color: lightblue; 
    }
    * {
        font-family: 'Verdana', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)
st.title("Password Strength Checker🔐")
password = st.text_input("Enter your password", type="password", key="password")
if st.button("Check Password Strength"):
    if password:
        score, feedback = password_strength(password)
        strength_label, color = get_strength_label(score)
        st.markdown("### Suggestions for Improvement: ✍️")
        if feedback:
            for suggestion in feedback:
                st.markdown(f"""
                    <div style="background-color:#f9f9f9; border-radius:5px; padding:10px; margin-bottom:10px;">
                        <p style="font-size:16px; color:#000;">{suggestion}</p>
                    </div>
                """, unsafe_allow_html=True)
        st.markdown(f"<h3 style='color:{color};'>{strength_label}</h3>", unsafe_allow_html=True)
        st.progress(score / 5)  
        st.write(f"Password Strength Score: {score} / 5")
    else:
        st.warning("Please enter a password to check its strength. 🧐")
st.subheader("Password Generator 🔑")
length = st.slider("Select Password Length", min_value=8, max_value=20, value=12)
include_uppercase = st.checkbox("Include Uppercase Letters?", value=False, key="uppercase_checkbox")
include_special = st.checkbox("Include Special Characters?", value=False, key="special_checkbox")
include_numbers = st.checkbox("Include Numbers?", value=False, key="numbers_checkbox")  
if st.button("Generate Password"):
    generated_password = generate_password(length, include_uppercase, include_special, include_numbers)
    st.text(f"Generated Password: {generated_password}")
st.markdown("""
    <footer>
        <p>💡 Created with ❤️ by Aleeza using Streamlit.</p>
    </footer>
""", unsafe_allow_html=True)
