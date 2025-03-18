Chatbot AI - Tự Train với Transformer

🚀 Giới thiệu

Đây là một chatbot AI được xây dựng từ đầu bằng mô hình Transformer, không phụ thuộc vào API bên ngoài như OpenAI. Mô hình sẽ được huấn luyện trên dữ liệu hội thoại và có thể trả lời tin nhắn của người dùng.

🛠 Cài đặt

1. Cài đặt thư viện cần thiết

pip install -r requirements.txt



pip install torch torchvision torchaudio




pip install fastapi uvicorn

2. Train mô hình

python backend/train.py

Sau khi train xong, mô hình sẽ được lưu vào thư mục models/

3. Chạy API chatbot

python -m uvicorn backend.main:app --reload

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


