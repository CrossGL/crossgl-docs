# Credora API Reference

Base URL: `https://api.credora.crossgl.net`

All authenticated endpoints require a `Bearer` token in the `Authorization` header.

---

## POST /analyze-tax-slip

Analyze a financial document. Supports PDF uploads up to 50 MB.

**Content-Type:** `multipart/form-data`

### Request

| Parameter | Type | Required | Description |
|---|---|---|---|
| `file` | file | Yes | PDF document to analyze |
| `reference_count` | integer | No | Number of reference documents for cross-validation (default: `1`) |

### Response `200 OK`

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

### Error Responses

| Status | Body | Cause |
|---|---|---|
| `400` | `{"error": "invalid_file_format"}` | Uploaded file is not a valid PDF |
| `401` | `{"error": "unauthorized"}` | Missing or invalid API key |
| `413` | `{"error": "payload_too_large"}` | File exceeds 50 MB limit |
| `422` | `{"error": "unprocessable_document"}` | Document could not be parsed |

---

## GET /documents

List all previously analyzed documents for the authenticated user.

**Authentication:** Required

### Query Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `page` | integer | No | Page number for pagination (default: `1`) |
| `limit` | integer | No | Results per page (default: `20`, max: `100`) |
| `document_type` | string | No | Filter by document type (e.g., `T4_TAX_SLIP`) |

### Response `200 OK`

```json
{
  "documents": [
    {
      "document_id": "doc_abc123",
      "document_type": "T4_TAX_SLIP",
      "created_at": "2025-01-15T10:30:00Z",
      "risk_level": "LOW",
      "risk_score": 12
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 1
  }
}
```

---

## GET /documents/{id}

Retrieve a specific analysis by document ID.

**Authentication:** Required

### Path Parameters

| Parameter | Type | Description |
|---|---|---|
| `id` | string | The document ID returned from analysis |

### Response `200 OK`

Returns the full analysis object (same schema as the `POST /analyze-tax-slip` response).

### Error Responses

| Status | Body | Cause |
|---|---|---|
| `401` | `{"error": "unauthorized"}` | Missing or invalid API key |
| `404` | `{"error": "not_found"}` | Document ID does not exist or does not belong to the authenticated user |

---

## GET /health

Health check endpoint. No authentication required.

### Response `200 OK`

```json
{
  "status": "healthy",
  "version": "1.0.0",
  "uptime_seconds": 86400
}
```
