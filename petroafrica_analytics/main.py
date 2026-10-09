from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any

from petroafrica_analytics import config


def ensure_data_dir() -> None:
    config.DATA_DIR.mkdir(parents=True, exist_ok=True)


def get_connection() -> sqlite3.Connection:
    ensure_data_dir()
    conn = sqlite3.connect(config.DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    ensure_data_dir()
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS compliance_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT NOT NULL,
                sample_code TEXT NOT NULL,
                parameter TEXT NOT NULL,
                measured_value REAL,
                unit TEXT,
                status TEXT NOT NULL,
                decision TEXT NOT NULL,
                specification_summary TEXT,
                source_document TEXT,
                reason TEXT,
                warnings TEXT,
                standard TEXT,
                edition TEXT,
                clause TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.commit()


def save_result(payload: dict[str, Any]) -> int:
    with get_connection() as conn:
        cursor = conn.execute(
            """
            INSERT INTO compliance_results (
                product_name, sample_code, parameter, measured_value, unit, status,
                decision, specification_summary, source_document, reason, warnings,
                standard, edition, clause
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                payload.get("product_name"),
                payload.get("sample_code"),
                payload.get("parameter"),
                payload.get("measured_value"),
                payload.get("unit"),
                payload.get("status"),
                payload.get("decision"),
                payload.get("specification_summary"),
                payload.get("source_document"),
                payload.get("reason"),
                "; ".join(payload.get("warnings", [])),
                payload.get("standard"),
                payload.get("edition"),
                payload.get("clause"),
            ),
        )
        conn.commit()
        return int(cursor.lastrowid)


def list_recent_results(limit: int = 15) -> list[dict[str, Any]]:
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT * FROM compliance_results
            ORDER BY created_at DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
        return [dict(row) for row in rows]
