from enum import IntEnum


class NebularApiEnumsAgentTypeEnum(IntEnum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_4 = 4
    VALUE_8 = 8
    VALUE_16 = 16
    VALUE_32 = 32
    VALUE_64 = 64

    def __str__(self) -> str:
        return str(self.value)
