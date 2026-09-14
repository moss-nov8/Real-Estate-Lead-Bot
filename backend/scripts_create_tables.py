"""Quick bootstrap: create all tables without Alembic (dev only)."""

import asyncio

from app.db.base import Base
from app.db.session import engine
from app.models import *  # noqa: F401,F403


async def main() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tables created successfully.")


if __name__ == "__main__":
    asyncio.run(main())
