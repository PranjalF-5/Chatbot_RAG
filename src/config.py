from dataclasses import dataclass
import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


@dataclass(frozen=True)
class KimiSettings:
    api_key: str
    base_url: str
    model: str
    max_tokens: int
    temperature: float
    top_p: float


def get_kimi_settings() -> KimiSettings:
    api_key = os.getenv("NVIDIA_API_KEY", "").strip()
    base_url = os.getenv("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1").strip()
    model = os.getenv("KIMI_MODEL", "moonshotai/kimi-k2.6").strip()
    max_tokens = int(os.getenv("KIMI_MAX_TOKENS", "16384"))
    temperature = float(os.getenv("KIMI_TEMPERATURE", "1.0"))
    top_p = float(os.getenv("KIMI_TOP_P", "1.0"))

    if not api_key:
        raise ValueError("NVIDIA_API_KEY is missing from the environment")

    return KimiSettings(
        api_key=api_key,
        base_url=base_url,
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
    )


def get_kimi_client() -> OpenAI:
    settings = get_kimi_settings()
    return OpenAI(api_key=settings.api_key, base_url=settings.base_url)
