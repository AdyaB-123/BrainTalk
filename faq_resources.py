import streamlit as st

def show_faq_resources_page():
    st.title("Frequently Asked Questions & Resources")

    faq_expander = st.expander("General Questions", expanded=True)
    with faq_expander:
        st.markdown("""
        **Q: What is BrainTalk?**  
        A: BrainTalk converts EEG brainwave data into spoken words, helping individuals with speech impairments communicate.

        **Q: How accurate is the EEG to text conversion?**  
        A: Accuracy depends on EEG data quality and individual users. Our model is trained on diverse datasets, but results may vary.

        **Q: Is my data secure?**  
        A: Yes, all processing happens locally on your device. We don't store your EEG data.
        """)

    als_expander = st.expander("For ALS Patients and Caregivers")
    with als_expander:
        st.markdown("""
        **Q: How can ALS patients benefit from BrainTalk?**  
        A: BrainTalk provides a non-invasive communication method for ALS patients as their condition progresses.

        **Q: What equipment do I need?**  
        A: You'll need an EEG headset that exports data in EDF format. Consult your healthcare provider for recommendations.
        """)

    resources_expander = st.expander("Helpful Resources")
    with resources_expander:
        st.markdown("""
        ### Community Forums and Support Groups
        - [ALS Association Discussion Forums](https://www.als.org/community/discussion-forums)
        - [ALS Forums](https://www.alsforums.com/)
        - [Brain-Computer Interface Community](https://www.bci-info.org/)
        - [Reddit r/ALS](https://www.reddit.com/r/ALS/)
        - [Reddit r/BCI](https://www.reddit.com/r/BCI/)

        ### Research and Information
        - [ALS Association](https://www.als.org/)
        - [International Brain-Computer Interface Society](http://bcisociety.org/)
        - [National Institute of Neurological Disorders and Stroke](https://www.ninds.nih.gov/)
        """)

    st.markdown("---")
    st.markdown("Have more questions? Contact us at support@braintalk.example.com")
