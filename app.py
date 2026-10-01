import streamlit as st
import requests

st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️"
)

st.title("⚖️ LegalEase")
st.subheader("AI-Powered Legal Document Generator")

document_type = st.selectbox(
    "Document Type",
    [
        "Employment Contract",
        "Non-Disclosure Agreement",
        "Lease Agreement",
        "Freelance Work Contract"
    ]
)

parties = st.text_area("Parties Involved")
terms = st.text_area("Terms and Conditions")
effective_date = st.text_input("Effective Date")

if st.button("Generate Document"):
    if parties and terms and effective_date:
        data = {
            "document_type": document_type,
            "parties": parties,
            "terms": terms,
            "effective_date": effective_date
        }

        try:
            response = requests.post(
                "http://127.0.0.1:8000/generate",
                json=data,
                timeout=180
            )
            response.raise_for_status()
            result = response.json()["document"]

            st.success("Document Generated!")
            edited = st.text_area(
                "Edit Your Document",
                value=result,
                height=400
            )

            st.download_button(
                "Download TXT",
                edited,
                file_name="legal_document.txt"
            )

        except requests.RequestException as error:
            st.error(f"Error: {error}")
    else:
        st.warning("Please fill in all required fields.")