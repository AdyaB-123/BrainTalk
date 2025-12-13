import streamlit as st
import mne
import pandas as pd
import numpy as np
from tsfresh import extract_features
from tsfresh.utilities.dataframe_functions import impute
import joblib
from gtts import gTTS
from io import BytesIO
import os
import requests

def load_model():
    try:
        model_path = Path(__file__).parent / "best_XGBoost_reg"
        if not model_path.exists():
            st.error(f"Model file does not exist at: {model_path}")
            return None
        if not os.access(str(model_path), os.R_OK):
            st.error(f"No read permission for the file: {model_path}")
            return None
        return joblib.load(str(model_path))
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

def extract_eeg_features(edf_path):
    raw = mne.io.read_raw_edf(edf_path, preload=True)
    data, times = raw.get_data(return_times=True)
    df_list = []

    for i, channel_name in enumerate(raw.ch_names):
        df = pd.DataFrame({
            'id': i,
            'time': times,
            'value': data[i]
        })
        df_list.append(df)

    full_df = pd.concat(df_list, ignore_index=True)
    extracted_features = extract_features(full_df, column_id='id', column_sort='time', column_value='value')
    return impute(extracted_features)

def text_to_speech(text):
    try:
        tts = gTTS(text=text, lang='en')
        audio_buffer = BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        st.audio(audio_buffer, format="audio/mp3")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def download_edf_file(url, filename):
    try:
        session = requests.Session()
        response = session.get(url, stream=True, timeout=10)
        response.raise_for_status()

        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        if os.path.getsize(filename) > 0:
            try:
                raw = mne.io.read_raw_edf(filename, preload=False, verbose=False)
                return True
            except Exception as e:
                st.error(f"Invalid EDF file: {e}")
                os.remove(filename)
                return False
        else:
            st.error("Downloaded file is empty")
            return False
    except Exception as e:
        st.error(f"Error downloading {filename}: {str(e)}")
        if os.path.exists(filename):
            os.remove(filename)
        return False

def show_home_page():
    st.title("BrainTalk")

    os.makedirs("downloaded_edf", exist_ok=True)

    st.subheader("Download sample EDF files")
    st.write("Click on the buttons below to download sample EDF files for testing:")

    edf_links = {
        'A': 'https://drive.google.com/uc?export=download&id=1ckD6gt7Z_Lkttg6kUv90ZbLQlanLP6NA',
        # Add other links here...
    }

    cols = st.columns(5)
    for i, (letter, url) in enumerate(edf_links.items()):
        with cols[i % 5]:
            if st.button(f"Download '{letter}'", 
                        key=f"btn_{letter}",
                        use_container_width=True):
                filename = os.path.join("downloaded_edf", f"sample_{letter}.edf")
                with st.spinner(f"Downloading {letter}.edf..."):
                    if download_edf_file(url, filename):
                        st.success(f"Downloaded {os.path.basename(filename)}")
                        with open(filename, "rb") as f:
                            st.download_button(
                                label=f"Save {letter}.edf",
                                data=f,
                                file_name=f"sample_{letter}.edf",
                                mime="application/octet-stream",
                                key=f"dl_{letter}"
                            )
                    else:
                        st.error("Download failed. Please try again.")

    st.subheader("Upload your EEG data")
    uploaded_files = st.file_uploader("Select EDF files (in desired order)", 
                                    type="edf", 
                                    accept_multiple_files=True,
                                    key="file_uploader")
    st.markdown("---")

    model = load_model()

    if uploaded_files:
        if st.button("Process EEG Data", type="primary"):
            with st.spinner("Processing EEG data..."):
                label_mapping = {0: 'A', 1: 'C', 2: 'F', 3: 'H', 4: 'J', 
                                5: 'M', 6: 'P', 7: 'S', 8: 'T', 9: 'Y'}
                all_labels = []

                for i, uploaded_file in enumerate(uploaded_files):
                    with open(f"temp_{i}.edf", "wb") as f:
                        f.write(uploaded_file.getbuffer())

                    try:
                        features_df = extract_eeg_features(f"temp_{i}.edf")
                        class_indices = model.predict(features_df)
                        unique, counts = np.unique(class_indices, return_counts=True)
                        most_common_index = np.argmax(counts)
                        most_common_element = unique[most_common_index]
                        all_labels.append(label_mapping[most_common_element])
                        os.remove(f"temp_{i}.edf")
                    except Exception as e:
                        st.error(f"Error processing file {uploaded_file.name}: {str(e)}")
                        continue

                if all_labels:
                    concatenated_labels = ''.join(all_labels)
                    st.subheader("Voice of the Mind")
                    st.write(concatenated_labels)
                    text_to_speech(concatenated_labels)
