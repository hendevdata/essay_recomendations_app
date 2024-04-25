
import streamlit as st
import plotly.express as px
import pandas as pd

# Set page title and icon
st.set_page_config(page_title='Modern Landing Page', page_icon='🚀')

# Create a title and subtitle
st.title('Welcome to our Modern Landing Page!')
st.write('This is a simple example of a modern landing page created with Streamlit.')

# Add a section to invite users to register and login
st.header('Join us today!')
st.write('Register and login to access the full features of our platform.')

# Register form
register_username = st.text_input('New Username')
register_password = st.text_input('New Password', type='password')
confirm_password = st.text_input('Confirm Password', type='password')
if st.button('Register'):
    if register_password == confirm_password:
        # Add your registration logic here
        st.write(f'Registration attempt with username: {register_username} and password: {register_password}')
    else:
        st.error('Passwords do not match.')

# Login form
login_username = st.text_input('Username')
login_password = st.text_input('Password', type='password')
if st.button('Login'):
    # Add your login logic here
    st.write(f'Login attempt with username: {login_username} and password: {login_password}')

# Create a section for a plot
st.header('Data Visualization')
st.write('Here is a simple plot created with Plotly Express.')

# Sample data for plot
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 20, 30, 40, 50]
})

# Create a plot
fig = px.line(df, x='x', y='y', title='Simple Line Plot')
st.plotly_chart(fig)

# Create a section for text
st.header('About Us')
st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, justo et pharetra commodo, quam mi tristique libero, ac aliquet metus nunc et nisl. Quisque nec fermentum ex, sit amet vulputate velit. Duis ullamcorper justo vitae justo commodo, nec dictum quam euismod. Integer sit amet tincidunt turpis, eget fermentum risus. Vivamus lobortis risus vitae justo pharetra, ut facilisis ligula commodo.')

# Create a call-to-action button
st.markdown('##')
if st.button('Get Started'):
    st.success('You clicked the button! You can add your action here.')

# Add a footer
st.markdown('---')
st.write('© 2024 Your Company. All rights reserved.')


# Create a plot
fig = px.line(df, x='x', y='y', title='Simple Line Plot')
st.plotly_chart(fig)

# Create a section for text
st.header('About Us')
st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, justo et pharetra commodo, quam mi tristique libero, ac aliquet metus nunc et nisl. Quisque nec fermentum ex, sit amet vulputate velit. Duis ullamcorper justo vitae justo commodo, nec dictum quam euismod. Integer sit amet tincidunt turpis, eget fermentum risus. Vivamus lobortis risus vitae justo pharetra, ut facilisis ligula commodo.')

# Create a call-to-action button
st.markdown('##')
if st.button('Get Started'):
    st.success('You clicked the button! You can add your action here.')

# Add a footer
st.markdown('---')
st.write('© 2024 Your Company. All rights reserved.')

