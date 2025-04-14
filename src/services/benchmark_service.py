from datetime import datetime
from typing import List

from src.domain import BenchmarkingResult
from src.domain import AbstractRepository


class BenchmarkService:
    def __init__(self, repository: AbstractRepository[BenchmarkingResult]):
        """
        Initialize the BenchmarkService with a repository.

        Args:
            repository (AbstractRepository[BenchmarkingResult]): 
                An abstract repository instance for managing benchmarking results.
        """

        self.repository = repository

    async def get_average_statistics(self) -> dict:
        """
        Get average statistics for all stored benchmarking results.

        Returns:
            dict: A dictionary containing keys for average token count, average time to first token, 
                average time per output token and average total generation time.
        """
        items = await self.repository.all()
        return self._compute_averages(items)

    async def get_average_statistics_between(self, start_time: str, end_time: str) -> dict:
        """
        Get average statistics for benchmarking results between the given start and end times.

        Args:
            start_time (str): The start time in ISO 8601 format.
            end_time (str): The end time in ISO 8601 format.

        Returns:
            dict: A dictionary containing keys for average token count, average time to first token, 
                average time per output token and average total generation time.
        """
        start, end = self._validate_date_range(start_time, end_time)

        items = await self.repository.all()
        filtered = [i for i in items if start <= datetime.fromisoformat(i.timestamp) <= end]
        return self._compute_averages(filtered)

    def _compute_averages(self, items: List[BenchmarkingResult]) -> dict:
        """
        Compute the average of the benchmarking results.

        Args:
            items (List[BenchmarkingResult]): The list of benchmarking results.

        Returns:
            dict: A dictionary containing keys for average token count, average time to first token, 
                average time per output token and average total generation time.
        """
        if not items:
            return {}

        return {
            "avg_token_count": sum(i.token_count for i in items) / len(items),
            "avg_time_to_first_token": sum(i.time_to_first_token for i in items) / len(items),
            "avg_time_per_output_token": sum(i.time_per_output_token for i in items) / len(items),
            "avg_total_generation_time": sum(i.total_generation_time for i in items) / len(items),
        }

    def _validate_date_range(self, start_time: str, end_time: str) -> tuple[datetime, datetime]:
        """
        Validate the datetime range and return parsed start and end times.

        Args:
            start_time (str): The start time in ISO 8601 format.
            end_time (str): The end time in ISO 8601 format.

        Returns:
            tuple: A tuple containing parsed start_time and end_time as datetime objects.

        Raises:
            ValueError: If the datetime format is invalid or if end_time is earlier than start_time.
        """
        try:
            start = datetime.fromisoformat(start_time)
            end = datetime.fromisoformat(end_time)
        except ValueError:
            raise ValueError("Invalid datetime format. Expected ISO 8601.")

        if end < start:
            raise ValueError("end_time must be after start_time.")

        return start, end