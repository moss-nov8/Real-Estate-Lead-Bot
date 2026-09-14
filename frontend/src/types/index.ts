export type LeadStatus =
  | "NEW"
  | "QUALIFYING"
  | "QUALIFIED"
  | "ASSIGNED"
  | "CONTACTED"
  | "ENGAGED"
  | "VIEWING_SCHEDULED"
  | "NEGOTIATING"
  | "NURTURE"
  | "CONVERTED"
  | "LOST";

export type LeadClassification = "HOT" | "WARM" | "COLD" | "UNQUALIFIED";

export interface Lead {
  id: string;
  name?: string | null;
  email?: string | null;
  phone?: string | null;
  transaction_type: string;
  property_type?: string | null;
  bedrooms?: number | null;
  location?: string | null;
  budget_min?: number | null;
  budget_max?: number | null;
  currency: string;
  timeline: string;
  status: LeadStatus;
  score: number;
  classification: LeadClassification;
  score_reasons?: string | null;
  notes?: string | null;
  assigned_to?: string | null;
  created_at: string;
  updated_at: string;
}

export interface Message {
  id: string;
  conversation_id: string;
  role: "CUSTOMER" | "BOT" | "AGENT" | "SYSTEM";
  content: string;
  processing_status: string;
  created_at: string;
}

export interface MessageResponse {
  customer_message: Message;
  bot_message?: Message | null;
  conversation_id: string;
  lead_id: string;
  lead?: Lead | null;
  status: string;
  detail?: string | null;
}

export interface LeadList {
  items: Lead[];
  total: number;
}

export interface ChatMessage {
  id: string;
  role: "customer" | "bot";
  content: string;
  createdAt: string;
  failed?: boolean;
}
