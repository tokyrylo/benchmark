from datetime import datetime
from fastapi import HTTPException

def validate_date_range(start_time: str, end_time: str) -> tuple[datetime, datetime]:
    try:
        start = datetime.fromisoformat(start_time)
        end = datetime.fromisoformat(end_time)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid datetime format. Expected ISO 8601.")

    if end < start:
        raise HTTPException(status_code=400, detail="end_time must be after start_time.")

    return start, end
