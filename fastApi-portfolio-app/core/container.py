"""
Dependency injection container for the application.
Manages singleton instances and dependencies.
"""

from typing import Optional
from kiteconnect import KiteConnect

class Container:
    """Dependency injection container."""
    
    _instance = None
    _kite_instance: Optional[KiteConnect] = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Container, cls).__new__(cls)
        return cls._instance
    
    @classmethod
    def get_kite_instance(cls) -> Optional[KiteConnect]:
        """Get the singleton KiteConnect instance."""
        return cls._kite_instance
    
    @classmethod
    def set_kite_instance(cls, instance: KiteConnect) -> None:
        """Set the singleton KiteConnect instance."""
        cls._kite_instance = instance
