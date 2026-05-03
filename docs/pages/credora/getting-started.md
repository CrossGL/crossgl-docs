# Getting Started with Credora

This guide walks you through submitting your first document for AI-powered analysis using the Credora API.

---

## Prerequisites

- A Credora API key (contact [support@crossgl.net](mailto:support@crossgl.net) to request access)
- A PDF document to analyze (tax slip, bank statement, invoice, etc.)

---

## Quick Start

### 1. Analyze a Document

Submit a PDF to the analysis endpoint:

```bash
curl -X POST https://api.credora.crossgl.net/analyze-tax-slip \
  -F "file=@/path/to/document.pdf" \
  -F "reference_count=1" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Request Parameters:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `file` | file | Yes | The PDF document to analyze |
| `reference_count` | integer | No | Number of reference documents for cross-validation (default: 1) |

### 2. Response

A successful response returns the analysis results:

```json
{
  "status": "success",
  "document_id": "doc_abc123",
  "document_type": "T4_TAX_SLIP",
  "processing_time_ms": 4820,
  "extraction": {
    "fields": {
      "employer_name": {
        "value": "Acme Corporation",
        "confidence": 0.997
      },
      "employment_income": {
        "value": 85000.00,
        "confidence": 0.994
      },
      "tax_year": {
        "value": "2024",
        "confidence": 0.999
      },
      "income_tax_deducted": {
        "value": 18750.00,
        "confidence": 0.991
      }
    },
    "tables": [],
    "metadata": {
      "page_count": 1,
      "extraction_engine": "multi-engine-v2"
    }
  },
  "risk_assessment": {
    "risk_score": 12,
    "risk_level": "LOW",
    "flags": [],
    "confidence": 0.96
  },
  "annotated_pdf_url": "https://api.credora.crossgl.net/documents/doc_abc123/annotated.pdf"
}
```

**Response Fields:**

| Field | Description |
|---|---|
| `document_type` | Detected document classification |
| `extraction.fields` | Key-value pairs with extracted data and confidence scores |
| `risk_assessment.risk_score` | Composite risk score (0–100, lower is better) |
| `risk_assessment.risk_level` | Categorical risk level: `LOW`, `MEDIUM`, `HIGH`, `CRITICAL` |
| `risk_assessment.flags` | Array of specific issues detected (empty if clean) |
| `annotated_pdf_url` | URL to download the annotated PDF report |

---

### 3. Retrieve Past Analyses

List your previous analyses:

```bash
curl https://api.credora.crossgl.net/documents \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Fetch a specific analysis by ID:

```bash
curl https://api.credora.crossgl.net/documents/doc_abc123 \
  -H "Authorization: Bearer YOUR_API_KEY"
```

---

## Error Handling

| Status Code | Meaning |
|---|---|
| `200` | Success |
| `400` | Bad request — invalid file format or missing parameters |
| `401` | Unauthorized — invalid or missing API key |
| `413` | Payload too large — file exceeds size limit |
| `422` | Unprocessable — document could not be parsed |
| `500` | Server error — retry or contact support |

---

## Next Steps

- [API Reference](api-reference.md) — Full endpoint documentation with all parameters
- [Overview](overview.md) — Learn more about Credora's architecture and capabilities
