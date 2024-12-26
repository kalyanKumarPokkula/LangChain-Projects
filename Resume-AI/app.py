import streamlit as st

# Import the individual pages
import page1
import page2


# Dictionary to map page names to functions
PAGES = {
    "Generate Bullet Points": page1,
    "Chat with your Resume": page2,
}

def main():
    # Set the page configuration
    st.set_page_config(layout="wide", page_title="Experience Bullet Points")
    
    st.sidebar.title('Navigation')
    # Use session state to remember the selected page
    if 'selected_page' not in st.session_state:
        st.session_state.selected_page = "Generate Bullet Points"
    
    # Create the navigation buttons
    for page in PAGES.keys():
        if st.sidebar.button(page):
            st.session_state.selected_page = page
    
    # Display the selected page
    page = PAGES[st.session_state.selected_page]
    page.app()

if __name__ == "__main__":
    main()