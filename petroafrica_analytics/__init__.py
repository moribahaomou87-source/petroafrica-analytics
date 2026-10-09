# PETROAFRICA ANALYTICS

PETROAFRICA ANALYTICS is a professional prototype focused on the first module of the petroleum quality-control platform: compliance verification for petroleum and petrochemical products.

This repository implements a minimal but functional and auditable control module. It is intentionally limited to the compliance-checking workflow requested by the project, without reconstructing the entire enterprise application.

## Scope of the prototype

The current module supports:

- product and sample identification
- parameter measurement input
- applicable specification selection
- comparison against normative limits
- reference validation for units, conditions, and test method
- classification as compliant, non-compliant, or indeterminate
- traceable audit logging of results
- French, English and Russian labels for the UI and API messages

## Technical choices

We intentionally start with a simple, modular backend architecture:

- Python + FastAPI for the API layer and business logic
- SQLite for the prototype database to keep installation simple and portable
- Jinja2 templates for a functional interface without a heavy frontend dependency
- Pydantic schemas to validate inputs and keep the API self-documenting
- explicit business rules in a dedicated compliance engine instead of mixing logic into the API layer

This keeps the prototype easy to run and test while preserving a structure that can later evolve to PostgreSQL, authentication, role management, and more advanced reporting.

## Project structure

- `petroafrica_analytics/` : application package
- `petroafrica_analytics/main.py` : API entry point and UI routes
- `petroafrica_analytics/compliance_engine.py` : decision engine
- `petroafrica_analytics/storage.py` : SQLite traceability layer
- `petroafrica_analytics/demo_data.py` : demonstration data clearly marked as sample data
- `tests/` : automated checks for compliance decisions

## Demo data note

The data in `petroafrica_analytics/demo_data.py` is clearly identified as demonstration-only and must not be interpreted as an official regulatory limit. It is used only to validate the decision logic and illustrate how the module behaves with compliant, non-compliant and indeterminate situations.

## Installation

1. Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the application:

```bash
python -m uvicorn petroafrica_analytics.main:app --reload
```

4. Open the browser at:

```text
http://127.0.0.1:8000
```

## API endpoints

### Web interface

- `GET /` : interactive prototype form

### Compliance evaluation

- `POST /api/compliance/check` : evaluate a product sample against a specification

Example request:

```json
{
  "product_name": "Diesel fuel",
  "sample_code": "D-001",
  "parameter": "Density at 15°C",
  "measured_value": 832.4,
  "unit": "kg/m3",
  "reference_conditions": "15°C",
  "test_method": "ASTM D4052",
  "specification": {
    "standard": "EN 590",
    "edition": "2022",
    "clause": "Table 1",
    "source_document": "European Committee for Standardization",
    "lower_limit": 820.0,
    "upper_limit": 845.0,
    "unit": "kg/m3",
    "reference_conditions": "15°C",
    "test_method": "ASTM D4052 / ISO 12185",
    "type": "product specification"
  }
}
```

Example response:

```json
{
  "status": "conforme",
  "decision": "conforme",
  "parameter": "Density at 15°C",
  "measured_value": 832.4,
  "unit": "kg/m3",
  "specification_summary": "EN 590 / 2022 / Table 1",
  "source_document": "European Committee for Standardization",
  "reason": "Measured value is within the specification interval.",
  "warnings": []
}
```

## Demo scenarios

The application includes matching examples for:

- conforming result
- non-conforming result
- insufficient data / indeterminate result
- unit mismatch
- specification absent

## Verification

Run the automated tests:

```bash
pytest -q
```

## Important regulatory note

This project does not invent official normative limits. The prototype relies on clearly identified sample specifications stored in memory and in the database as demonstration metadata. Any production deployment must be tied to an authoritative document source with traceable reference data and validation by a qualified quality team.

## Next evolution paths

The following phases are intentionally deferred to preserve the first-module focus:

- role-based access and authentication
- extended dictionary of standards and methods
- richer dashboard and PDF reporting
- integration with laboratory information systems
- PostgreSQL migration and audit-grade retention
- versioned specification management and review workflow

