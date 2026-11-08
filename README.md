# Local AI Data Pipeline with Ollama & Pydantic Validation

A production-ready Python architecture for structured data extraction and triage from unstructured input text, executed 100% locally using Ollama (llama3.2) and validated via Pydantic.

This repository demonstrates how to build privacy-first, zero-cost data extraction pipelines for enterprises with strict compliance needs (GDPR, HIPAA) or high-volume API constraints.

---

## Technical Features

* Air-Gapped Local Inference: Executes LLM inference offline using Ollama (llama3.2). No third-party API keys or external data transmissions.
* Deterministic Structured Outputs: Utilizes Pydantic's JSON schema enforcement to guarantee type-safe outputs (bool, str).
* Zero Variable Cost: Eliminates per-token cloud API charges, making it scalable for massive batch processing.
* Seamless Python Native Integration: Parses raw model outputs directly into validated Python data objects.

---

## Architecture Overview

[ Unstructured Customer Request ]
               │
               ▼
   [ Python App Execution ]
               │
               ▼ (Local HTTP Request via localhost:11434)
   [ Ollama Engine (llama3.2) ] ── (Strict JSON Schema Enforcement)
               │
               ▼
  [ Raw JSON Model Response ]
               │
               ▼
 [ Pydantic Model Validation ] ──► Validated Native Python Object

---

## Requirements & Setup

1. Ollama: Install Ollama on your host machine from ollama.com.
2. Pull the Local Model:
   ollama run llama3.2
3. Install Dependencies:
   pip install ollama pydantic

---

## Execution & Output Sample

Run the local processor script:
python procesador_local.py

### Validated Output Benchmark

--- RESULTADO PROCESADO EN LOCAL (COSTO: $0.00) ---
Resumen: Problema de pago
Categoría: Soporte Técnico
Urgencia: Alta
Escalado Humano: True

Tipo de objeto validado: <class '__main__.SolicitudSoporte'>

---

## Business & Commercial Use Cases

1. Healthcare & Legal Data Processing: Automated ingestion of sensitive documents where privacy policies forbid cloud LLM API usage.
2. Cost-Optimization for Scale: Replacing repetitive cloud classification APIs with local inference servers, saving thousands in operational expenditure.
3. Offline Desktop & Enterprise Applications: Embedding intelligent features directly into software deployed on local corporate infrastructure.