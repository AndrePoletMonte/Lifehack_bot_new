# database.py
import os
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, func
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# Читаем URL базы из переменных окружения (настрой на Railway)
DATABASE_URL = os.getenv("DATABASE_URL")

# Создаём асинхронный движок
engine = create_async_engine(DATABASE_URL, echo=False)

# Базовый класс для моделей
Base = declarative_base()

# Создаём фабрику сессий
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

# Таблица пользователей
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, index=True)
    language = Column(String(10), default="en")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    stats = relationship("Stats", back_populates="user")

# Таблица лайфхаков
class Lifehack(Base):
    __tablename__ = "lifehacks"

    id = Column(Integer, primary_key=True, index=True)
    text_en = Column(Text, nullable=False)
    text_sr = Column(Text, nullable=True)

# Таблица статистики
class Stats(Base):
    __tablename__ = "stats"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    action = Column(String(50))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="stats")


# Функция для создания таблиц
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
