# Excel转CSV转换器

这是一个使用 Python 和 Streamlit 库编写的网页应用程序，旨在实现从 Excel 文件转换为 CSV 格式，并提供文件预览和下载功能。

可以在stream app上直接体验: https://excel-to-csv.streamlit.app/

## 功能

- 上传 Excel 文件并将其转换为 CSV
- 提供转换后的 CSV 文件预览
- 下载转换后的 CSV 文件

## 如何使用

1. 确保已安装所需的依赖项（如 Streamlit 和 Pandas）。

```bash
pip install -r requirements.txt
```

2. 将文件保存为 `app.py`。
3. 使用以下命令在本地运行应用程序：

```shell
streamlit run app.py
```

4. 应用程序将在本地启动一个服务器，并显示一个 URL。
5. 在浏览器中访问该 URL，即可使用网页应用程序。

## 注意事项

- 应用程序假定上传的 Excel 文件只包含一个工作表。如果文件包含多个工作表，需要根据需要进行修改。
- 应用程序不会在服务器上保留 CSV 文件。转换后的 CSV 数据将在下载时生成临时的 CSV 文件供用户下载。

希望这个应用程序能对你有所帮助！如有任何问题或反馈，请随时提出。
