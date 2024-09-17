from abc import ABC, abstractmethod


class BenchmarkRepository(ABC):
    @abstractmethod
    async def get_all_results(self):
        pass

    @abstractmethod
    async def get_results_by_time_window(self, start_time: str, end_time: str):
        pass
