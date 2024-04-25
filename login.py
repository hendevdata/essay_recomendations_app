import streamlit as st

# Placeholder for user data storage (replace with database or secure storage)
users = {'admin': 'password123'}  # Username: Password

def register_user(new_username, new_password):
    # Replace with logic to securely store username and hashed password in a database
    users[new_username] = new_password  # Placeholder storage (update for security)
    st.success('Registration successful!')

def register():
    new_username = st.text_input("Username:")
    new_password = st.text_input("Password:", type="password")
    confirm_password = st.text_input("Confirm Password:", type="password")
    
    if new_password == confirm_password and st.button("Submit"):
        register_user(new_username, new_password)
    elif new_password != confirm_password:
        st.error('Passwords do not match!')

def main():
    st.title('Essay Scorer')
    st.write('Welcome to the essay scoring app!')

    choice = st.selectbox('Login or Register', ['Login', 'Register'])

    if choice == 'Register':
        register()

if __name__ == '__main__':
    main()
