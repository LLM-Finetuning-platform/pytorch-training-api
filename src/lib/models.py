from dataclasses import dataclass
from enum import Enum
from typing import Optional
class ModelNames(Enum):
    Qwen3 = "qwen3b"

class PeftMethod(Enum):
    LORA = "lora"
    QLORA = "qlora"

@dataclass
class Model:
    name: ModelNames
    allowed_peft_method:PeftMethod
    epochs: int
    parameters_in_b: Optional[float]