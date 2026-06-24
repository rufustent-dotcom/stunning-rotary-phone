"""
Signal layer: monitors a live price feed and detects profitable trending conditions.
"""

import random
import time
from dataclasses import dataclass, field
from typing import Iterator


@dataclass
class PriceEvent:
    asset: str
    price: float
    threshold: float = 0.0
    timestamp: float = field(default_factory=lambda: time.time())

    @property
    def is_profitable(self) -> bool:
        return self.price >= self.threshold


class PriceFeed:
    """Simulates a live market or pricing feed."""

    def __init__(
        self,
        asset: str = "GREED",
        base_price: float = 100.0,
        volatility: float = 5.0,
        profit_threshold: float = 110.0,
        tick_interval: float = 0.5,
    ) -> None:
        self.asset = asset
        self.base_price = base_price
        self.volatility = volatility
        self.profit_threshold = profit_threshold
        self.tick_interval = tick_interval
        self._current_price = base_price

    def _next_price(self) -> float:
        delta = random.gauss(0, self.volatility)
        # Mean-revert slightly toward base to avoid drift.
        reversion = (self.base_price - self._current_price) * 0.05
        self._current_price = max(0.01, self._current_price + delta + reversion)
        return round(self._current_price, 2)

    def stream(self, ticks: int = 0) -> Iterator[PriceEvent]:
        """Yield PriceEvent objects.  If *ticks* is 0 the stream is infinite."""
        count = 0
        while ticks == 0 or count < ticks:
            price = self._next_price()
            event = PriceEvent(
                asset=self.asset,
                price=price,
                threshold=self.profit_threshold,
            )
            yield event
            count += 1
            time.sleep(self.tick_interval)


def detect_trending_peak(feed: PriceFeed, window: int = 5) -> Iterator[PriceEvent]:
    """Yield only the events that represent a trending peak above the threshold.

    A peak is defined as a price that is both above the profit threshold and
    higher than all prices in the preceding *window* ticks.
    """
    history: list[float] = []
    for event in feed.stream():
        history.append(event.price)
        if len(history) > window:
            history.pop(0)
        if event.is_profitable and event.price == max(history):
            yield event
