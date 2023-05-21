import streamlit as st
import pandas as pd
import base64
from io import BytesIO


# 多语言翻译字典
translations = {
    'en': {
        'app_title': "Excel to CSV Converter",
        'upload_text': "Upload an Excel file and convert it to CSV",
        'choose_file': "Choose an Excel file",
        'success_message': "File successfully converted. Click the button below to download the CSV file:",
        'download_link': "Download CSV",
        'preview_header': "Preview of the Converted CSV file",
        'error_message': "Error occurred while converting the file:",
        'privacy_message': "Privacy Notice: We do not store any of your data.",
    },
    'zh_CN': {
        'app_title': "Excel转CSV转换器",
        'upload_text': "上传一个Excel文件并转换为CSV",
        'choose_file': "选择一个Excel文件",
        'success_message': "文件成功转换。点击下方按钮下载CSV文件：",
        'download_link': "点击这里下载",
        'preview_header': "转换后的CSV文件预览",
        'error_message': "转换文件时出错：",
        'privacy_message': "隐私声明：我们不会存储您的任何数据。",
    }
}


def translate(text, language):
    return translations[language].get(text, text)


def convert_excel_to_csv(file):
    df = pd.read_excel(file)
    csv_data = df.to_csv(index=False).encode()
    return csv_data


def download_csv(csv_data, csv_file, language):
    b64 = base64.b64encode(csv_data).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{csv_file}">{translate("download_link", language)}</a>'
    return href



def main():
    language = st.selectbox("Select Language", ("English", "简体中文"))
    language_code = "en" if language == "English" else "zh_CN"

    st.title(translate("app_title", language_code))
    st.write(translate("upload_text", language_code))
    st.write(translate("privacy_message", language_code))

    uploaded_file = st.file_uploader(translate("choose_file", language_code), type=["xlsx"])

    if uploaded_file is not None:
        try:
            csv_data = convert_excel_to_csv(uploaded_file)
            csv_file = uploaded_file.name.replace(".xlsx", ".csv")
            st.success(translate("success_message", language_code))
            download_link = download_csv(csv_data, csv_file, language_code)
            st.markdown(download_link, unsafe_allow_html=True)

            # 预览转换后的CSV文件
            st.subheader(translate("preview_header", language_code))
            df = pd.read_csv(BytesIO(csv_data))
            st.dataframe(df)

        except Exception as e:
            st.error(translate("error_message", language_code) + f" {str(e)}")


if __name__ == "__main__":
    main()
