
"""
Nền tảng SQLAlchemy async cho toàn bộ project:
- Base: mọi model (User, Event, Plan...) đều kế thừa từ đây, để Alembic quét được hết bảng.
- engine: kết nối thật tới Postgres, chỉ tạo 1 lần duy nhất, dùng chung toàn app.
- AsyncSessionLocal: factory tạo session (1 phiên làm việc với DB) cho mỗi request.

"""

from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.core.config import settings

from app.models.base import Base

# echo=True: in ra toàn bộ câu SQL thật khi chạy — hữu ích lúc dev để debug,
# nên tắt (echo=False) khi deploy production vì log sẽ rất nhiều.
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.ENVIRONMENT == "development",
    future=True,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,  # tránh lỗi truy cập object sau khi đã commit
    autoflush=False,
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Dùng trong route: `db: AsyncSession = Depends(get_db)`.
    yield thay vì return để FastAPI tự đóng session lại sau khi trả response,
    kể cả khi route đó bị lỗi giữa chừng (nhờ try/finally).
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()