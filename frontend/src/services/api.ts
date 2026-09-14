import type { Lead, LeadList, Message, MessageResponse } from "../types";

const API_BASE =
  import.meta.env.VITE_API_BASE_URL?.replace(/\/$/, "") || "/api/v1";

async function request<T>(path: string, options?: RequestInit): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: {
      "Content-Type": "application/json",
      ...(options?.headers || {}),
    },
    ...options,
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(text || `HTTP ${res.status}`);
  }
  return res.json() as Promise<T>;
}

export function sendMessage(payload: {
  content: string;
  conversation_id?: string | null;
  external_id?: string;
}): Promise<MessageResponse> {
  return request("/messages", {
    method: "POST",
    body: JSON.stringify({
      content: payload.content,
      conversation_id: payload.conversation_id || undefined,
      external_id: payload.external_id,
      role: "CUSTOMER",
    }),
  });
}

export function getMessages(conversationId: string): Promise<Message[]> {
  return request(`/conversations/${conversationId}/messages`);
}

export function listLeads(params?: {
  q?: string;
  status?: string;
  classification?: string;
}): Promise<LeadList> {
  const sp = new URLSearchParams();
  if (params?.q) sp.set("q", params.q);
  if (params?.status) sp.set("status", params.status);
  if (params?.classification) sp.set("classification", params.classification);
  const qs = sp.toString();
  return request(`/leads${qs ? `?${qs}` : ""}`);
}

export function getLead(id: string): Promise<Lead> {
  return request(`/leads/${id}`);
}

export function health(): Promise<{ status: string; database: string }> {
  return request("/health");
}
