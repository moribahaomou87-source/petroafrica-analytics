from __future__ import annotations

from petroafrica_analytics.config import DB_PATH

# Demo dataset explicitly marked as non-official demonstration data.
# These values are for testing the business logic only.

DEMO_PRODUCTS = [
    {
        "product_id": "diesel-en590",
        "name": "Diesel fuel",
        "family": "Refined petroleum",
        "category": "distillate",
    },
    {
        "product_id": "gasoline-95",
        "name": "Gasoline 95",
        "family": "Refined petroleum",
        "category": "motor fuel",
    },
]

DEMO_SPECIFICATIONS = [
    {
        "product_id": "diesel-en590",
        "parameter": "Density at 15°C",
        "unit": "kg/m3",
        "lower_limit": 820.0,
        "upper_limit": 845.0,
        "reference_conditions": "15°C",
        "test_method": "ASTM D4052 / ISO 12185",
        "standard": "EN 590",
        "edition": "2022",
        "clause": "Table 1",
        "source_document": "European Committee for Standardization",
        "type": "product specification",
    },
    {
        "product_id": "diesel-en590",
        "parameter": "Sulfur content",
        "unit": "mg/kg",
        "lower_limit": 0.0,
        "upper_limit": 10.0,
        "reference_conditions": "normalized to product",
        "test_method": "ISO 20846 / ASTM D5453",
        "standard": "EN 590",
        "edition": "2022",
        "clause": "Table 1",
        "source_document": "European Committee for Standardization",
        "type": "product specification",
    },
    {
        "product_id": "gasoline-95",
        "parameter": "Research octane number",
        "unit": "RON",
        "lower_limit": 95.0,
        "upper_limit": 100.0,
        "reference_conditions": "reference conditions",
        "test_method": "ASTM D2699",
        "standard": "EN 228",
        "edition": "2022",
        "clause": "Table 2",
        "source_document": "European Committee for Standardization",
        "type": "product specification",
    },
]

DEMO_RESULTS = [
    {
        "sample_code": "D-001",
        "parameter": "Density at 15°C",
        "measured_value": 832.4,
        "unit": "kg/m3",
        "status": "conforme",
        "reason": "Measured value is within the specification interval.",
        "standard": "EN 590",
        "edition": "2022",
        "clause": "Table 1",
        "source_document": "European Committee for Standardization",
    },
    {
        "sample_code": "D-001",
        "parameter": "Sulfur content",
        "measured_value": 18.3,
        "unit": "mg/kg",
        "status": "non_conforme",
        "reason": "Measured value exceeds the upper specification limit.",
        "standard": "EN 590",
        "edition": "2022",
        "clause": "Table 1",
        "source_document": "European Committee for Standardization",
    },
]

DATABASE_PATH = DB_PATH
