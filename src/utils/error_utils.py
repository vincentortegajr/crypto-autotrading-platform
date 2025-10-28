"""
Error Utilities Module

Provides universal error handling decorators and utilities for the Vince Quant Whale Helix platform.

Flow: Decorate functions with @retry_on_failure for automatic retries on exceptions.
"""

import time
import logging
from functools import wraps
from typing import Callable, Any, Optional

logger = logging.getLogger(__name__)

# Global constants
AGENT_NAME = "error_utils"
VERTICAL = "universal"  # Applies to all verticals

def retry_on_failure(
    max_retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: tuple = (Exception,),
    log_errors: bool = True
) -> Callable:
    """
    Decorator to retry a function on failure.

    Args:
        max_retries: Maximum number of retry attempts.
        delay: Initial delay between retries in seconds.
        backoff: Multiplier for delay on each retry.
        exceptions: Tuple of exceptions to catch and retry on.
        log_errors: Whether to log errors during retries.

    Returns:
        Decorated function that retries on failure.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            current_delay = delay
            last_exception = None

            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_retries:
                        if log_errors:
                            logger.warning(
                                f"{AGENT_NAME}: Attempt {attempt + 1}/{max_retries + 1} failed for {func.__name__}: {e}. "
                                f"Retrying in {current_delay:.2f}s..."
                            )
                        time.sleep(current_delay)
                        current_delay *= backoff
                    else:
                        if log_errors:
                            logger.error(
                                f"{AGENT_NAME}: All {max_retries + 1} attempts failed for {func.__name__}: {e}"
                            )
                        raise last_exception

            # This should never be reached, but just in case
            raise last_exception

        return wrapper
    return decorator

def log_exceptions(func: Callable) -> Callable:
    """
    Decorator to log exceptions raised by a function.

    Args:
        func: Function to decorate.

    Returns:
        Decorated function that logs exceptions.
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"{AGENT_NAME}: Exception in {func.__name__}: {e}")
            raise

    return wrapper

# Test function
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    @retry_on_failure(max_retries=2, delay=0.1)
    def flaky_function():
        """Test function that fails twice then succeeds."""
        if not hasattr(flaky_function, '_call_count'):
            flaky_function._call_count = 0
        flaky_function._call_count += 1

        if flaky_function._call_count < 3:
            raise ValueError(f"Simulated failure #{flaky_function._call_count}")
        return "Success!"

    try:
        result = flaky_function()
        print(f"✅ {AGENT_NAME}: Test passed - {result}")
    except Exception as e:
        print(f"❌ {AGENT_NAME}: Test failed - {e}")
        raise