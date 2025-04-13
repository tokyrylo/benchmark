from datetime import datetime
from dataclasses import dataclass

@dataclass
class BenchmarkingResult:
    request_id: str
    prompt_text: str
    generated_text: str
    token_count: int
    time_to_first_token: int
    time_per_output_token: int
    total_generation_time: int
    timestamp: datetime



