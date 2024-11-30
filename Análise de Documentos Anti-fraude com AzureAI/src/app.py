import streamlit as st
from services.blob_service import upload_blob

def configure_interface():
    st.title("Upload do lab da dio Azure Docs")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        fileName = uploaded_file.name
        blob_url = upload_blob(uploaded_file, fileName)
        if blob_url:
            st.write(f"Arquivo {fileName} enviado ao blob do Azure Storage")
            credit_card_info = ""
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f"Erro ao enviar o arquivo {fileName} ao blob do Azure Storage")            

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="imagem enviada", use_column_width=True)
    st.write("resultado da validação"
            if credit_card_info and credit_card_info["card_name"]:
                st.markdown(f"<h1 style='color: green;'>Cartão Válido</h1>", unsafe_allow_html=True)
                st.write(f"Nome do titular do cartão: {credit_card_info['card_name']}")
                st.write(f"Nome do banco emissor: {credit_card_info['bank_name']}")
                st.write(f"Data de validade: {credit_card_info['expiry_date']}")
            else:
                st.write("Erro 423")
    
if __name__ == "__main__":
    configure_interface()