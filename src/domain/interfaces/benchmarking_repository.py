from typing import (
    List, 
    Optional, 
    Union, 
    TypeVar, 
    Generic,
)

from abc import ABC

T = TypeVar("T")


class AbstractRepository(ABC, Generic[T]):
    async def add(self, model: T) -> T: ...
    async def get(self, reference: Union[int, str], field: str = "id") -> Optional[T]: ...
    async def update(self, model: T) -> T: ...
    async def delete(self, model: T) -> None: ...
    async def all(self) -> List[T]: ...