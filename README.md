# Chatbot_RAG

## Kimi K2.6 Setup

This project is configured to use Kimi K2.6 through NVIDIA's OpenAI-compatible chat endpoint.

1. Copy [.env.example](.env.example) to [.env](.env).
2. Set `NVIDIA_API_KEY` to your NVIDIA API key.
3. Keep `NVIDIA_BASE_URL` as `https://integrate.api.nvidia.com/v1`.
4. Keep `KIMI_MODEL` as `moonshotai/kimi-k2.6` unless your provider tells you otherwise.

To verify the configuration, run:

```powershell
.\venv\Scripts\python app.py
```

Then open `http://127.0.0.1:5000/health`.