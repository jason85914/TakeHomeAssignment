# 使用 Python 3.8 作為基礎映像
FROM python:3.8

# 設置工作目錄
WORKDIR /app

# 將要求文件複製到容器中
COPY requirements.txt .

# 安裝所需的依賴項
RUN pip install --no-cache-dir -r requirements.txt

# 將應用程序代碼複製到容器中
COPY . .

# 暴露端口
EXPOSE 5000

# 定義啟動命令
CMD ["python", "get_raw_data.py"]

# 使用--env-file選項將.env文件中的環境變量包含在映像中
RUN set -o allexport; source $ENV_FILE; set +o allexport