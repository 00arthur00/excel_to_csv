import streamlit as st
import pandas as pd
import base64
from io import BytesIO


def convert_excel_to_csv(file):
    df = pd.read_excel(file)
    csv_data = df.to_csv(index=False).encode()
    return csv_data


def download_csv(csv_data, csv_file):
    b64 = base64.b64encode(csv_data).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{csv_file}">点击这里下载</a>'
    return href


def main():
    st.title("Excel转CSV转换器")
    st.write("上传一个Excel文件并转换为CSV")

    uploaded_file = st.file_uploader("选择一个Excel文件", type=["xlsx"])

    if uploaded_file is not None:
        try:
            csv_data = convert_excel_to_csv(uploaded_file)
            csv_file = uploaded_file.name.replace(".xlsx", ".csv")
            st.success(f"文件成功转换。点击下方按钮下载CSV文件：")
            download_link = download_csv(csv_data, csv_file)
            st.markdown(download_link, unsafe_allow_html=True)

            # 预览转换后的CSV文件
            st.subheader("转换后的CSV文件预览")
            df = pd.read_csv(BytesIO(csv_data))
            st.dataframe(df)

        except Exception as e:
            st.error(f"转换文件时出错：{str(e)}")


if __name__ == "__main__":
    main()
