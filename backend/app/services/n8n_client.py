"""Client to trigger n8n webhooks."""

import logging
from typing import Any, Optional
from uuid import UUID

import httpx

from app.core.config import settings

logger = logging.getLogger(__name__)


async def trigger_process_message(
    *,
    message_id: UUID,
    conversation_id: UUID,
    lead_id: UUID,
    content: str,
    lead_snapshot: Optional[dict[str, Any]] = None,
) -> dict[str, Any]:
    url = settings.N8N_WEBHOOK_URL.rstrip("/")
    if not url.endswith("lead-process-message"):
        url = f"{url}/lead-process-message"

    payload = {
        "message_id": str(message_id),
        "conversation_id": str(conversation_id),
        "lead_id": str(lead_id),
        "content": content,
        "lead": lead_snapshot or {},
        "secret": settings.N8N_WEBHOOK_SECRET or None,
    }

    try:
        async with httpx.AsyncClient(timeout=settings.AI_TIMEOUT_SECONDS) as client:
            resp = await client.post(url, json=payload)
            resp.raise_for_status()
            data = resp.json() if resp.content else {}
            logger.info("n8n process-message OK: %s", data)
            return {"ok": True, "data": data}
    except httpx.HTTPError as exc:
        logger.warning("n8n process-message failed: %s", exc)
        return {"ok": False, "error": str(exc)}
    except Exception as exc:
        logger.exception("n8n unexpected error")
        return {"ok": False, "error": str(exc)}
