from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, Field

DecisionStatus = Literal["conforme", "non_conforme", "indetermine"]


class SpecificationInput(BaseModel):
    standard: str = Field(..., min_length=2)
    edition: str = Field(..., min_length=1)
    clause: str = Field(..., min_length=1)
    source_document: str = Field(..., min_length=2)
    lower_limit: Optional[float] = None
    upper_limit: Optional[float] = None
    unit: Optional[str] = None
    reference_conditions: Optional[str] = None
    test_method: Optional[str] = None
    type: str = "product specification"


class ComplianceCheckRequest(BaseModel):
    product_name: str = Field(..., min_length=2)
    sample_code: str = Field(..., min_length=2)
    parameter: str = Field(..., min_length=2)
    measured_value: Optional[float] = None
    unit: Optional[str] = None
    reference_conditions: Optional[str] = None
    test_method: Optional[str] = None
    specification: Optional[SpecificationInput] = None


class ComplianceDecisionResponse(BaseModel):
    status: DecisionStatus
    decision: DecisionStatus
    parameter: str
    measured_value: Optional[float]
    unit: Optional[str]
    specification_summary: str
    source_document: str
    reason: str
    warnings: list[str] = []
    sample_code: str
    product_name: str
    standard: Optional[str] = None
    edition: Optional[str] = None
    clause: Optional[str] = None
