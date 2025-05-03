from enum import IntEnum


class NebularApiEnumsUnitCodeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_20 = 20
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_30 = 30
    VALUE_31 = 31
    VALUE_32 = 32
    VALUE_40 = 40
    VALUE_41 = 41
    VALUE_42 = 42
    VALUE_50 = 50
    VALUE_51 = 51
    VALUE_70 = 70
    VALUE_71 = 71
    VALUE_72 = 72
    VALUE_73 = 73
    VALUE_80 = 80
    VALUE_81 = 81
    VALUE_82 = 82
    VALUE_83 = 83
    VALUE_255 = 255

    def __str__(self) -> str:
        return str(self.value)
