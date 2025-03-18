import torch
from transformers import AutoTokenizer
from datasets import load_dataset
from model import model

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Tải dữ liệu huấn luyện từ Hugging Face (OpenWebText)
dataset = load_dataset("openwebtext", split="train")

# Tiền xử lý dữ liệu
def tokenize_data(example):
    return tokenizer(example["text"], truncation=True, padding="max_length", max_length=128)

dataset = dataset.map(tokenize_data, batched=True)

# Huấn luyện mô hình
optimizer = torch.optim.Adam(model.parameters(), lr=5e-5)
loss_fn = torch.nn.CrossEntropyLoss()

for epoch in range(5):
    for batch in dataset:
        inputs = torch.tensor(batch["input_ids"])
        targets = torch.tensor(batch["input_ids"])

        optimizer.zero_grad()
        outputs = model(inputs)
        loss = loss_fn(outputs.view(-1, 50000), targets.view(-1))
        loss.backward()
        optimizer.step()

    print(f"Epoch {epoch+1}: Loss = {loss.item()}")

# Lưu mô hình
torch.save(model.state_dict(), "models/chatbot_model.pth")
print("🎉 Mô hình đã train xong và lưu vào models/chatbot_model.pth")
