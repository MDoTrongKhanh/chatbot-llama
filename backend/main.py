from fastapi import FastAPI
import torch
from model import SimpleTransformer
from transformers import AutoTokenizer

app = FastAPI()

# Load mô hình đã train
model = SimpleTransformer(vocab_size=50000, hidden_dim=256, num_layers=4)
model.load_state_dict(torch.load("models/chatbot_model.pth"))
model.eval()

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

@app.get("/chat")
def chat(prompt: str):
    inputs = torch.tensor([tokenizer.encode(prompt, truncation=True, padding="max_length", max_length=128)])
    outputs = model(inputs)
    response = tokenizer.decode(outputs.argmax(dim=-1).tolist()[0])
    return {"response": response}
