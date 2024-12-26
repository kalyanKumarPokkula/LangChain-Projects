import streamlit as st
from llm import get_bllt_pnts_frm_desc

def app():

    # Title
    st.title("Get Experience Bullet Points")
    st.text("Get tailored bullet points for your resume based on your experience and job description of the job you're applying for.")

    # Apply CSS to increase the width of the input and output text areas
    st.markdown(
        """
        <style>
        .input-text-area .stTextArea textarea {
            width: 80% !important;
        }
        .output-text-area .stTextArea textarea {
            width: 80% !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Initialize session state
    if 'output_text' not in st.session_state:
        st.session_state.output_text = ''

    # Create the layout with columns
    col1, col2, col3 = st.columns([2, 1, 2])

    # Input field
    with col1:
        st.markdown('<div class="input-text-area">', unsafe_allow_html=True)
        input_text = st.text_area("Job Description", height=300, placeholder="Paste your job description here..!")
        st.markdown('</div>', unsafe_allow_html=True)

    # Button to perform action
    with col2:
        if st.button("Generate"):
            with st.spinner("Processing..."):
                # Perform some action
                response = get_bllt_pnts_frm_desc(str(input_text))
                st.session_state.output_text = str(response)

    # Output field
    with col3:
        st.markdown('<div class="output-text-area">', unsafe_allow_html=True)
        output_text = st.text_area("Generated Bullet Points", height=300, value=st.session_state.output_text, key="output_field", placeholder="Once you provide a job description, you will get bullet points.")
        st.markdown('</div>', unsafe_allow_html=True)