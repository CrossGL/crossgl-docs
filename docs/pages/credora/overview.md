# Credora Overview

**Credora** is an AI-powered document authentication, verification, and analysis platform built for financial institutions. It combines advanced PDF extraction with Google Vertex AI and Gemini models to deliver fast, accurate document intelligence at scale.

---

## What Credora Does

Credora ingests financial documents — tax slips, bank statements, pay stubs, invoices, and more — and returns structured data, confidence scores, risk assessments, and annotated PDF reports. The entire pipeline runs in seconds, not minutes.

### Core Capabilities

| Capability | Description |
|---|---|
| **PDF Extraction** | High-fidelity text, table, and field extraction from scanned and digital PDFs using multi-engine parsing |
| **AI Analysis** | Vertex AI and Gemini models classify documents, validate fields, and detect anomalies |
| **Risk Scoring** | Automated risk scores based on data consistency, document authenticity, and cross-field validation |
| **Annotated Output** | Generates annotated PDF reports highlighting extracted fields, flagged issues, and confidence levels |

### Key Stats

- **99.4%** extraction accuracy across supported document types
- **< 7 seconds** average end-to-end processing time
- **60+** supported document types (tax forms, bank statements, pay stubs, invoices, identity documents, and more)

---

## Architecture

Credora's pipeline follows a three-stage architecture:

1. **Ingestion & Extraction**
    - Documents are uploaded via the API or web interface
    - Multi-engine PDF extraction handles both scanned and digital documents
    - Tables, fields, and metadata are extracted with positional data

2. **AI Analysis & Verification**
    - Extracted data is passed to Vertex AI / Gemini models
    - Classification identifies document type and expected fields
    - Cross-field validation checks for internal consistency
    - Anomaly detection flags potential fraud or errors

3. **Scoring & Report Generation**
    - A composite risk score is generated based on extraction confidence, field validation, and anomaly signals
    - An annotated PDF is produced, overlaying extraction results and flags on the original document
    - Structured JSON results are returned via the API

---

## Use Cases

- **Mortgage Underwriting** — Automate income and asset verification from tax returns and bank statements
- **KYC / Compliance** — Verify identity documents and cross-reference fields
- **Audit & Review** — Batch-process financial documents with full traceability
- **Fraud Detection** — Flag inconsistencies, alterations, and anomalies in submitted documents

---

## Next Steps

- [Getting Started](getting-started.md) — Submit your first document for analysis
- [API Reference](api-reference.md) — Full endpoint documentation
