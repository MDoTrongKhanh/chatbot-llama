Chatbot AI - Tự Train với Transformer

🚀 Giới thiệu

Đây là một chatbot AI được xây dựng từ đầu bằng mô hình Transformer, không phụ thuộc vào API bên ngoài như OpenAI. Mô hình sẽ được huấn luyện trên dữ liệu hội thoại và có thể trả lời tin nhắn của người dùng.

📂 Cấu trúc thư mục

chatbot-llama/         # Thư mục chính của dự án
│── backend/           # Chứa mã backend (API & model)
│   │── main.py        # API chatbot
│   │── model.py       # Mô hình AI (Transformer)
│   │── train.py       # Huấn luyện mô hình
│── models/            # Chứa mô hình AI đã train
│   │── chatbot_model.pth  # Mô hình AI đã lưu
│── requirements.txt   # Danh sách thư viện cần cài
│── README.md          # Hướng dẫn sử dụng dự án
│── .gitignore         # Bỏ qua file không cần đẩy lên GitHub

🛠 Cài đặt

1. Cài đặt thư viện cần thiết

pip install -r requirements.txt

2. Train mô hình

python backend/train.py

Sau khi train xong, mô hình sẽ được lưu vào thư mục models/

3. Chạy API chatbot

uvicorn backend.main:app --reload

Sau khi chạy, truy cập API tại:
👉 http://127.0.0.1:8000/chat?prompt=Hello

🚀 Đẩy lên GitHub

git init
git add .
git commit -m "Upload chatbot AI tự train"
git branch -M main
git remote add origin https://github.com/USERNAME/chatbot-llama.git
git push -u origin main

👉 Thay USERNAME bằng GitHub của bạn.


