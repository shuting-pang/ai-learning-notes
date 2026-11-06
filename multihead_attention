import torch
import torch.nn as nn
import math
class MultiheadAttention(nn.Module):
    def __init__(self, d_model, n_heads):
        super().__init__()
        assert d_model % n_heads == 0
        self.d_model = d_model
        self.n_heads = n_heads
        self.d_k = d_model // n_heads

        self.Wq = nn.Linear(d_model,d_model)
        self.Wk = nn.Linear(d_model,d_model) 
        self.Wv = nn.Linear(d_model,d_model) 
        self.Wo = nn.Linear(d_model,d_model) 

    def forward(self, x, mask=None):
        B, L, D = x.shape
        Q = self.Wq(x)
        K = self.Wk(x)
        V = self.Wv(x)
        Q = Q.view(B, L, self.n_heads, self.d_k).transpose(1,2)
        K = K.view(B, L, self.n_heads, self.d_k).transpose(1,2)
        V = V.view(B, L, self.n_heads, self.d_k).transpose(1,2)
        scores = torch.matmul(Q, K.transpose(-1,-2)) / math.sqrt(self.d_k)
        if mask is not None:
            scores = scores.masked_fill(mask ==0, float('-inf'))

        attn = torch.softmax(scores, dim=-1)
        out = torch.matmul(attn, V)
        out = out.transpose(1,2).contiguous().view(B, L, D)
        out = self.Wo(out)
        return out

if __name__ == "__main__":
    model = MultiheadAttention(d_model=64, n_heads=8)
    x = torch.randn(2, 10, 64)
    # d_model, n_heads = map(int, input().split())
    out = model(x)
    print(out.shape) 
