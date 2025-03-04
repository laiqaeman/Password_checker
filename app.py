import streamlit as st
import re
import secrets
import string
import pyperclip

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    # Check length
    if len(password) < 8:
        return "Weak: Too short", "red", 0.2, ["Increase password length to at least 8 characters."]
    
    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 0.2
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 0.2
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check for digits
    if re.search(r"[0-9]", password):
        score += 0.2
    else:
        feedback.append("Add at least one digit.")

    # Check for special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 0.2
    else:
        feedback.append("Add at least one special character.")

    # Check for common passwords
    common_passwords = ["password123", "12345678", "qwerty"]
    if password in common_passwords:
        return "Weak: Common password, choose another", "red", 0.2, ["Avoid common passwords."]

    # Determine strength based on score
    if score == 1.0:
        return "Strong: Your password is strong!", "green", score, []
    elif score < 0.6:
        return "Weak", "red", score, feedback
    elif score < 1.0:
        return "Moderate", "blue", score, feedback
    else:
        return "Strong", "green", score, ["Your password is strong!"]

# Function to generate a secure password
def generate_secure_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

# Set page title and layout
st.set_page_config(page_title="Password Strength Meter", layout="centered")


# Apply custom CSS for new stylish font & UI improvements
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Raleway:wght@400;700&display=swap');

    .stApp {
        background: linear-gradient(to right, #2C3E50, #4CA1AF); /* Midnight Blue to Teal */
        color: white;
    }
    h1, h2, h3, h4, h5, h6, p {
        font-family: 'Raleway', sans-serif !important;
    }
     h1, h2 {
        font-size: 42px;
        text-align: center;
        font-weight: bold;
             background: linear-gradient(to right, #FFB6C1, #ADD8E6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7); /* Adding text shadow */
    }
    h3 {
        font-size: 24px;
        text-align: center;
        font-weight: bold;
        color: white;
    }
    p {
        font-size: 18px;
        text-align: center;
        color: #EAEAEA;
    }
    .separator {
        height: 5px;
        margin-top: 10px;
        margin-bottom: 10px;
        border-radius: 5px;
    }
    .input-box {
        padding: 10px;
        border-radius: 10px;
        border: 2px solid #FF512F;
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
    }
     .footer {
        text-align: center;
        padding: 20px;
        margin-top: 40px;
        border-top: 1px solid #EAEAEA;
        color: #EAEAEA;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown("<h1 class='gradient-text'>Password Strength Tester</h1>", unsafe_allow_html=True)


password_input = st.text_input("Enter Password", type="password")

if password_input:
    strength_message, color, score, feedback = check_password_strength(password_input)
    
    st.markdown(f"<h3 style='color:{color}; text-align: center; font-family: Raleway;'>{strength_message}</h3>", unsafe_allow_html=True)
    st.progress(score)

    if feedback:
        st.markdown("<h2 class='gradient-text'>Password Suggestions</h2>", unsafe_allow_html=True)
        for suggestion in feedback:
            st.write(f"- {suggestion}")

    # Generate Secure Password
    if st.button("Generate Strong Password"):
        strong_password = generate_secure_password()
        st.text_input("Generated Password", value=strong_password, disabled=True)

        # Copy to clipboard option
        if st.button("Copy to Clipboard"):
            pyperclip.copy(strong_password)
            st.success("Password copied to clipboard!")

# FAQs Section

    st.markdown("<h2 class='gradient-text'>Frequently Asked Questions</h2>", unsafe_allow_html=True)
faq_questions = {
    "Is it safe to enter my real password here?": 
        "Yes. Your password is never stored or transmitted. It is processed locally on your browser.",
    
    "How do you calculate password strength?": 
        "We evaluate length, character variety, and check against common weak passwords.",
    
    "How do I create a strong password?": 
        "Use at least 12 characters, mix uppercase, lowercase, numbers, and special characters.",
    
    "What's the best way to manage my passwords?": 
        "Use a password manager to store and generate secure passwords."
}

for question, answer in faq_questions.items():
    with st.expander(question):
        st.write(answer)
st.markdown("""
    <div class='footer'>
        Made with ❤️ by Laiqa | Secure Your Digital Life
    </div>
    """, unsafe_allow_html=True)
