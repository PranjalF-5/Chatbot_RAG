from flask import Flask, jsonify

from src.config import get_kimi_settings


app = Flask(__name__)


@app.get("/health")
def health() -> tuple[dict[str, str], int]:
	settings = get_kimi_settings()
	return (
		{
			"status": "ok",
			"model": settings.model,
			"base_url": settings.base_url,
		},
		200,
	)


@app.get("/")
def index() -> tuple[dict[str, str], int]:
	return jsonify(
		{
			"message": "Chatbot_RAG is configured for Kimi K2.6 via NVIDIA's OpenAI-compatible endpoint.",
		}
	), 200


if __name__ == "__main__":
	app.run(debug=True)

