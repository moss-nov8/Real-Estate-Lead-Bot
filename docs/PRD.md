# PRD — Real Estate Lead Bot (PrimeHomes Realty)

**Version:** 1.0  
**Status:** Draft  
**Stack:** React + FastAPI + n8n + PostgreSQL + Google Sheets

## Executive Summary

The Real Estate Lead Bot acts as an AI-powered digital receptionist for PrimeHomes Realty. It receives natural-language customer enquiries, extracts structured requirements, qualifies leads, stores them, responds, and notifies the sales team when needed.

## Goals

- Automate lead capture and qualification
- Understand natural language
- Improve response time
- Reduce sales team repetitive work
- Maintain a reliable structured record of leads and conversations

## Non-Goals (MVP)

- Full property marketplace / listing management
- Automated negotiation or contract generation
- Payment processing
- Fully autonomous AI sales agent that makes binding commitments

## Core User Journey

Customer message → AI understanding → extraction → missing-info questions if needed → lead scoring & classification → store → respond → notify sales (if HOT) → human follow-up.

## Lead Information

Customer: name, email, phone  
Property: type, bedrooms, location, budget  
Intent: BUY / RENT / SELL / INQUIRE  
Timeline: IMMEDIATE / WITHIN_1_MONTH / WITHIN_3_MONTHS / WITHIN_6_MONTHS / RESEARCHING

## Lead Classification

HOT (80–100) · WARM (60–79) · COLD (30–59) · UNQUALIFIED (0–29)

Full original PRD content is available in git history.
