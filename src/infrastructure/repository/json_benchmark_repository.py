from typing import List, Optional, Union

from src.domain.entities import BenchmarkingResult
from src.domain import AbstractRepository
from src.infrastructure.utils import read_benchmarking_results


class JSONBenchmarkRepository(AbstractRepository[BenchmarkingResult]):
    def __init__(self, file_path: str):
        """
        Initialize a JSONBenchmarkRepository instance.

        Args:
            file_path (str): The path to a JSON file containing benchmarking results.
        """
        self.file_path = file_path

    async def all(self) -> List[BenchmarkingResult]:
        """
        Returns all benchmarking results stored in the JSON file.

        This method reads the JSON file and returns all stored results as a list of BenchmarkResult objects.
        """
        return [item async for item in read_benchmarking_results(self.file_path)]
    
    async def get(self, reference: Union[int, str], field: str = "request_id") -> Optional[BenchmarkingResult]:
        """
        Retrieve a benchmarking result by a specified field.

        This asynchronous method searches through the JSON file for a benchmarking 
        result that matches the given reference value in the specified field.

        Args:
            reference (Union[int, str]): The value to search for in the specified field.
            field (str): The field to search within, default is "request_id".

        Returns:
            Optional[BenchmarkResult]: The matching BenchmarkResult object if found, 
            otherwise None.
        """

        async for item in read_benchmarking_results(self.file_path):
            if getattr(item, field) == reference:
                return item
        return None
    
    async def add(self, model: BenchmarkingResult) -> BenchmarkingResult:
        """
        Adds a new benchmarking result to the JSON file.

        This method is not implemented for the JSON repository because it is a read-only repository.

        Args:
            model (BenchmarkResult): The benchmarking result to add to the repository.

        Returns:
            BenchmarkResult: The newly added benchmarking result.

        Raises:
            NotImplementedError: Always, because add operation is not supported for JSON repository.
        """
        raise NotImplementedError("Add operation not supported for JSON repository")
    
    async def update(self, model: BenchmarkingResult) -> BenchmarkingResult:    
        """
        Updates an existing benchmarking result in the JSON file.

        This method is not implemented for the JSON repository because it is a read-only repository.

        Args:
            model (BenchmarkResult): The benchmarking result to update in the repository.

        Returns:
            BenchmarkResult: The updated benchmarking result.

        Raises:
            NotImplementedError: Always, because update operation is not supported for JSON repository.
        """

        raise NotImplementedError("Update operation not supported for JSON repository")
    
    async def delete(self, model: BenchmarkingResult) -> None:
        """
        Deletes an existing benchmarking result from the JSON file.

        This method is not implemented for the JSON repository because it is a read-only repository.

        Args:
            model (BenchmarkResult): The benchmarking result to delete from the repository.

        Raises:
            NotImplementedError: Always, because delete operation is not supported for JSON repository.
        """
        
        raise NotImplementedError("Delete operation not supported for JSON repository")