import streamlit as st

def show_about_page():
    st.title("About BrainTalk")
    st.markdown("""
    ## Welcome to BrainTalk

    BrainTalk is an innovative application that converts EEG brainwave data into spoken words, 
    providing a voice to individuals with speech impairments such as ALS, locked-in syndrome, 
    or other conditions affecting speech.

    ### Key Features
    - **EEG to Text Conversion**: Upload EEG data in EDF format to convert brain signals into text
    - **Text to Speech**: Hear the converted text with our built-in speech synthesis
    - **User-Friendly Interface**: Simple and intuitive design for ease of use
    - **Privacy-Focused**: Your data stays on your device and is not stored on our servers

    ### Who Can Benefit
    - Individuals with ALS (Amyotrophic Lateral Sclerosis)
    - Patients with locked-in syndrome
    - People with speech disorders
    - Stroke survivors with speech impairments
    - Researchers in the field of Brain-Computer Interfaces (BCI)
    - Healthcare professionals working with non-verbal patients

    ### How It Works
    1. Upload your EEG data in EDF format
    2. Our AI model processes the brainwave patterns
    3. The system predicts the intended characters
    4. Characters are combined to form words
    5. The text is converted to natural-sounding speech

    ### Getting Started
    Click on the 'Home' tab in the sidebar to begin converting your EEG data to speech.
    """)
    st.markdown("---")
    st.markdown("© 2025 BrainTalk - Empowering Communication Through Technology")
