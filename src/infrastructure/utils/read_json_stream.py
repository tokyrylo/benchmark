from typing import AsyncGenerator

import json
import aiofiles

from src.domain.entities.benchmarking import BenchmarkingResult


async def read_benchmarking_results(file_path: str) -> AsyncGenerator[BenchmarkingResult, None]:
    """
    Reads a JSON file at the given file_path and yields each benchmarking result found in the "benchmarking_results" key as a BenchmarkingResult object.

    Args:
        file_path (str): The path to the JSON file containing benchmarking results.

    Yields:
        BenchmarkingResult: A BenchmarkingResult object for each item in the JSON file.
    """
    
    async with aiofiles.open(file_path, mode='r') as f:
        content = await f.read()
        data = json.loads(content)
        for item in data.get("benchmarking_results", []):
            yield BenchmarkingResult(**item)
