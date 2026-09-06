from abc import ABC, ABCMeta, abstractmethod
from typing import  Callable, Dict, Optional, Any
import inspect
class BaseRouter(ABC):
    def __init__(self) :
        self. _handlers : Dict[str,Callable] = {}
    def register(self,name: Optional[str]=None)->Callable:
        """Decorator to register a handler func"""
        def decorator(func: Callable)->Callable:
            key = name or func.__name__
            if key in self._handlers:
                raise ValueError("Handler Func Already registered")
            self._handlers[key] = func
            return func
        return decorator
    def execute(self, name: str, *args, **kwargs)->Any:
            handler = self._handlers.get(name)
            if not handler:
                 raise ValueError(f"No Handler registered for the name {name} ")
            return handler (*args, **kwargs)
    def list_handlers(self)->Dict[str, Callable]:
         return self._handlers
    @abstractmethod
    @staticmethod
    def get_version()->str:
         """Return the version of the router"""
         pass
