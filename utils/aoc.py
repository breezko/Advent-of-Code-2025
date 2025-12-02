from dataclasses import dataclass, asdict
from typing import Any, Callable
import time

@dataclass
class AoCResult:
    day: int
    part: int
    answer: Any
    duration_ms: float

    def __str__(self) -> str:
        base = f"Day {self.day}, Part {self.part}: {self.answer}"
        return f"{base}\t(took {self.duration_ms:.3f} ms)"

    __repr__ = __str__

    def to_dict(self) -> dict:
        return asdict(self)

def aoc_part(day: int, part: int):
    def decorator(func: Callable[..., Any]):
        def wrapper(*args, **kwargs) -> AoCResult:
            start = time.perf_counter()
            answer = func(*args, **kwargs)
            end = time.perf_counter()
            result = AoCResult(
                day=day,
                part=part,
                answer=answer,
                duration_ms=(end - start) * 1000,
            )
            print(result)
            return result
        return wrapper
    return decorator