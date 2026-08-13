"""
Đọc toàn bộ biến môi trường từ file .env vào 1 object Settings duy nhất.
Dùng pydantic-settings để: (1) tự validate kiểu dữ liệu (VD PORT phải là int),
(2) báo lỗi ngay lúc khởi động nếu thiếu biến bắt buộc, thay vì lỗi ngầm lúc chạy.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    # --- Server ---
    PROJECT_NAME: str = "Web Len Ke Hoach Nhom AI"
    PORT: int = 8000
    ENVIRONMENT: str = "development"
    API_V1_STR: str = "/api/v1"
    FRONTEND_URL: str = "http://localhost:5173"

    # --- Database ---
    DATABASE_URL: str

    # --- Redis ---
    REDIS_URL: str = "redis://localhost:6379/0"

    # --- Auth (JWT & OAuth2) ---
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    GOOGLE_CLIENT_ID: str = ""
    GOOGLE_CLIENT_SECRET: str = ""
    GOOGLE_CALLBACK_URL: str = ""
    FACEBOOK_APP_ID: str = ""
    FACEBOOK_APP_SECRET: str = ""

    # --- AI DeepSeek API (Nhóm AI dùng, khai báo sẵn ở đây để dùng chung 1 nguồn config) ---
    DEEPSEEK_API_KEY: str = ""
    AI_MODEL_DEFAULT: str = "deepseek-chat"
    AI_MODEL_REASONING: str = "deepseek-reasoner"
    AI_MAX_TOKENS_PER_REQUEST: int = 4096
    AI_MAX_STEPS_PER_SESSION: int = 15

    # --- External APIs ---
    GOOGLE_PLACES_API_KEY: str = ""
    MAPBOX_ACCESS_TOKEN: str = ""
    OPENWEATHER_API_KEY: str = ""
    EXCHANGE_RATE_API_KEY: str = ""

    # --- Email & SMTP ---
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    EMAILS_FROM_EMAIL: str = ""
    EMAILS_FROM_NAME: str = ""

    # --- Rate Limit ---
    RATE_LIMIT_AI_PER_MINUTE: int = 20
    RATE_LIMIT_AUTH_PER_MINUTE: int = 10

    # Đọc từ file .env ở thư mục backend/, bỏ qua các biến VITE_* của frontend
    model_config = SettingsConfigDict(env_file="../.env", env_file_encoding="utf-8", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    """
    Cache lại 1 instance duy nhất — tránh đọc lại file .env mỗi lần gọi.
    Dùng: from app.core.config import get_settings; settings = get_settings()
    """
    return Settings()


settings = get_settings()