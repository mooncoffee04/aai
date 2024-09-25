#we are making a sign up page using streamlit!
import streamlit as st
import pandas as pd
 
# Initialize session state for login status and current page
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'page' not in st.session_state:
    st.session_state['page'] = 'login'  # Default to login page
 
# Function to load user data from CSV
def load_user_data():
    try:
        df = pd.read_csv('user_data.csv')
        # Ensure columns are present
        if 'Username' not in df.columns or 'Password' not in df.columns:
            st.error("CSV does not have the required columns!")
            return pd.DataFrame(columns=['Username', 'Password', 'Mobile Number', 'City'])
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=['Username', 'Password', 'Mobile Number', 'City'])
 
# Function to handle login page
def login_page():
    st.title("Login")
 
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type='password', key="login_password")
    if st.button("Submit", key="login_submit"):
        user_data = load_user_data()
 
        if user_data.empty:
            st.error("No users found. Please sign up first.")
        else:
            # Check if username and password match any record in the CSV file
            if ((user_data['Username'] == username) & (user_data['Password'] == password)).any():
                st.session_state['logged_in'] = True
                st.success("Login successful!")
            else:
                st.error("Invalid username or password.")
 
# Function to handle signup page
def signup_page():
    st.title("Signup")
 
    username = st.text_input("New Username", key="signup_username")
    password = st.text_input("New Password", type='password', key="signup_password")
    mobile = st.text_input("Mobile Number", key="signup_mobile")
    city = st.text_input("City", key="signup_city")
 
    if st.button("Sign Up", key="signup_submit"):
        user_data = load_user_data()
        # Check if username already exists
        if (user_data['Username'] == username).any():
            st.error("Username already exists. Please choose a different username.")
        elif (user_data['Mobile Number'] == mobile).any():
            st.error("Mobile number already registered. Please use a different number.")
        else:
            new_data = pd.DataFrame({
                'Username': [username], 
                'Password': [password], 
                'Mobile Number': [mobile], 
                'City': [city]
            })
            if user_data.empty:  # If the file is empty, include header
                new_data.to_csv('user_data.csv', index=False)
            else:
                new_data.to_csv('user_data.csv', mode='a', header=False, index=False)
            st.success(f"Signed up as: {username}")
            st.session_state['page'] = 'login'  # Redirect to login after successful signup
 
# Control navigation between login and signup
st.sidebar.title("User Options")
 
if st.sidebar.button("Login", key="login_button"):
    st.session_state['page'] = 'login'
 
if st.sidebar.button("Signup", key="signup_button"):
    st.session_state['page'] = 'signup'
 
# Display either login or signup page based on the current session state
if st.session_state['page'] == 'login':
    login_page()
elif st.session_state['page'] == 'signup':
    signup_page()
 
# If user is logged in, display additional content
if st.session_state['logged_in']:
    st.sidebar.write("You are logged in!")
