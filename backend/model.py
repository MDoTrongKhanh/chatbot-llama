import torch
import torch.nn as nn
import torch.optim as optim

class SimpleTransformer(nn.Module):
    def __init__(self, vocab_size, hidden_dim, num_layers):
        super(SimpleTransformer, self).__init__()
        self.embedding = nn.Embedding(vocab_size, hidden_dim)
        self.encoder = nn.TransformerEncoder(
            nn.TransformerEncoderLayer(d_model=hidden_dim, nhead=8), 
            num_layers=num_layers
        )
        self.decoder = nn.Linear(hidden_dim, vocab_size)

    def forward(self, x):
        x = self.embedding(x)
        x = self.encoder(x)
        return self.decoder(x)

# Khởi tạo mô hình
model = SimpleTransformer(vocab_size=50000, hidden_dim=256, num_layers=4)
