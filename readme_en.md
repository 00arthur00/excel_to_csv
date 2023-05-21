[中文文档](./README.md)
# Excel to CSV Converter

This is a web application written in Python using the Streamlit library. It allows you to convert Excel files to CSV
format and provides file preview and download functionality.

You can experience the app directly on Streamlit Sharing: [Excel to CSV Converter](https://excel-to-csv.streamlit.app/)

## Features

- Upload Excel file and convert it to CSV
- Preview the converted CSV file
- Download the converted CSV file

## How to Use

1. Make sure you have the required dependencies installed (such as Streamlit and Pandas).

```bash
pip install -r requirements.txt
```

2. Save the file as app.py.
3. Run the application locally using the following command:

```bash
streamlit run app.py
```

4. The application will start a local server and display a URL.
5. Visit that URL in your browser to use the web application.

## Multi-Language Support
This application supports two languages: English and Chinese. You can select the desired language in the sidebar of the application.

## Notes
* The application assumes that the uploaded Excel file contains only one worksheet. If the file contains multiple worksheets, modification is required as per your needs.
* The application does not store the CSV files on the server. The converted CSV data will be generated as a temporary file for download.

Hope this application is helpful for you! If you have any questions or feedback, feel free to reach out.