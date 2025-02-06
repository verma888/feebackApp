import streamlit as st

# Title of the application
st.title('Customer Feedback')

# Form to collect feedback
with st.form(key='feedback_form'):
    name = st.text_input('Customer Name')
    feedback = st.text_area('Feedback Message')
    rating = st.selectbox('Rating', options=[1, 2, 3, 4, 5])
    submit_button = st.form_submit_button(label='Submit')

# List to store feedback entries
feedback_entries = []

# Display feedback upon form submission
if submit_button:
    feedback_entries.append({'name': name, 'feedback': feedback, 'rating': rating})
    st.success('Feedback submitted!')

# Display all feedback entries
if feedback_entries:
    st.write('### Submitted Feedback')
    for entry in feedback_entries:
        st.write(f"**Name:** {entry['name']}")
        st.write(f"**Feedback:** {entry['feedback']}")
        st.write(f"**Rating:** {entry['rating']}")
        st.write('---')
