from pydantic import BaseModel

class BenchmarkingResponse(BaseModel):
    avg_token_count: float
    avg_time_to_first_token: float
    avg_time_per_output_token: float
    avg_total_generation_time: float