from __future__ import annotations

import re
from typing import Optional

from petroafrica_analytics.schemas import ComplianceCheckRequest, ComplianceDecisionResponse, SpecificationInput


def _normalize_text(value: Optional[str]) -> str:
    if value is None:
        return ""
    return re.sub(r"\s+", " ", value.strip().lower())


def _compatible_method(request_method: Optional[str], spec_method: Optional[str]) -> bool:
    if not request_method or not spec_method:
        return True
    request_norm = _normalize_text(request_method)
    spec_norm = _normalize_text(spec_method)
    if request_norm == spec_norm:
        return True
    if request_norm in spec_norm or spec_norm in request_norm:
        return True
    return False


def _compatible_reference(reference: Optional[str], spec_reference: Optional[str]) -> bool:
    if not reference or not spec_reference:
        return True
    return _normalize_text(reference) == _normalize_text(spec_reference)


def _validate_specification(specification: Optional[SpecificationInput]) -> tuple[bool, str]:
    if specification is None:
        return False, "No applicable specification was provided."

    if specification.lower_limit is None and specification.upper_limit is None:
        return False, "Specification limits are missing or invalid."

    if specification.lower_limit is not None and specification.upper_limit is not None:
        if specification.lower_limit > specification.upper_limit:
            return False, "Specification lower limit exceeds the upper limit."

    if specification.standard.strip() == "" or specification.edition.strip() == "" or specification.clause.strip() == "":
        return False, "The specification metadata is incomplete: standard, edition, or clause is missing."

    return True, "Specification validated."


def evaluate_compliance(check: ComplianceCheckRequest) -> ComplianceDecisionResponse:
    spec = check.specification
    if check.measured_value is None:
        return ComplianceDecisionResponse(
            status="indetermine",
            decision="indetermine",
            parameter=check.parameter,
            measured_value=None,
            unit=check.unit,
            specification_summary="No specification attached",
            source_document="unknown",
            reason="The measured value is missing; the result cannot be evaluated.",
            warnings=["Missing measured value."],
            sample_code=check.sample_code,
            product_name=check.product_name,
        )

    valid_spec, spec_reason = _validate_specification(spec)
    if not valid_spec:
        return ComplianceDecisionResponse(
            status="indetermine",
            decision="indetermine",
            parameter=check.parameter,
            measured_value=check.measured_value,
            unit=check.unit,
            specification_summary="No valid specification",
            source_document=spec.source_document if spec else "unknown",
            reason=spec_reason,
            warnings=["Specification validation failed."],
            sample_code=check.sample_code,
            product_name=check.product_name,
            standard=spec.standard if spec else None,
            edition=spec.edition if spec else None,
            clause=spec.clause if spec else None,
        )

    if check.unit and spec.unit and _normalize_text(check.unit) != _normalize_text(spec.unit):
        return ComplianceDecisionResponse(
            status="indetermine",
            decision="indetermine",
            parameter=check.parameter,
            measured_value=check.measured_value,
            unit=check.unit,
            specification_summary=f"{spec.standard} / {spec.edition} / {spec.clause}",
            source_document=spec.source_document,
            reason="The measured unit does not match the specification unit.",
            warnings=[f"Expected unit '{spec.unit}' but received '{check.unit}'."],
            sample_code=check.sample_code,
            product_name=check.product_name,
            standard=spec.standard,
            edition=spec.edition,
            clause=spec.clause,
        )

    if not _compatible_method(check.test_method, spec.test_method):
        return ComplianceDecisionResponse(
            status="indetermine",
            decision="indetermine",
            parameter=check.parameter,
            measured_value=check.measured_value,
            unit=check.unit,
            specification_summary=f"{spec.standard} / {spec.edition} / {spec.clause}",
            source_document=spec.source_document,
            reason="The test method used is not compatible with the referenced specification method.",
            warnings=[
                f"Specified method '{spec.test_method}' is not compatible with input method '{check.test_method}'."
            ],
            sample_code=check.sample_code,
            product_name=check.product_name,
            standard=spec.standard,
            edition=spec.edition,
            clause=spec.clause,
        )

    if not _compatible_reference(check.reference_conditions, spec.reference_conditions):
        return ComplianceDecisionResponse(
            status="indetermine",
            decision="indetermine",
            parameter=check.parameter,
            measured_value=check.measured_value,
            unit=check.unit,
            specification_summary=f"{spec.standard} / {spec.edition} / {spec.clause}",
            source_document=spec.source_document,
            reason="The reference conditions do not match the specification conditions.",
            warnings=[
                f"Expected reference conditions '{spec.reference_conditions}' but received '{check.reference_conditions}'."
            ],
            sample_code=check.sample_code,
            product_name=check.product_name,
            standard=spec.standard,
            edition=spec.edition,
            clause=spec.clause,
        )

    lower_limit = spec.lower_limit
    upper_limit = spec.upper_limit
    value = check.measured_value

    if lower_limit is not None and value < lower_limit:
        return ComplianceDecisionResponse(
            status="non_conforme",
            decision="non_conforme",
            parameter=check.parameter,
            measured_value=value,
            unit=check.unit or spec.unit,
            specification_summary=f"{spec.standard} / {spec.edition} / {spec.clause}",
            source_document=spec.source_document,
            reason="Measured value is below the minimum specification threshold.",
            warnings=[f"Value {value} is less than lower limit {lower_limit}."] ,
            sample_code=check.sample_code,
            product_name=check.product_name,
            standard=spec.standard,
            edition=spec.edition,
            clause=spec.clause,
        )

    if upper_limit is not None and value > upper_limit:
        return ComplianceDecisionResponse(
            status="non_conforme",
            decision="non_conforme",
            parameter=check.parameter,
            measured_value=value,
            unit=check.unit or spec.unit,
            specification_summary=f"{spec.standard} / {spec.edition} / {spec.clause}",
            source_document=spec.source_document,
            reason="Measured value exceeds the upper specification limit.",
            warnings=[f"Value {value} is greater than upper limit {upper_limit}."] ,
            sample_code=check.sample_code,
            product_name=check.product_name,
            standard=spec.standard,
            edition=spec.edition,
            clause=spec.clause,
        )

    return ComplianceDecisionResponse(
        status="conforme",
        decision="conforme",
        parameter=check.parameter,
        measured_value=value,
        unit=check.unit or spec.unit,
        specification_summary=f"{spec.standard} / {spec.edition} / {spec.clause}",
        source_document=spec.source_document,
        reason="Measured value is within the specification interval.",
        warnings=[],
        sample_code=check.sample_code,
        product_name=check.product_name,
        standard=spec.standard,
        edition=spec.edition,
        clause=spec.clause,
    )
