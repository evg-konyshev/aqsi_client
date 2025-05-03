from enum import IntEnum


class NebularApiEnumsDevicePaymentTypeEnum(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15

    def __str__(self) -> str:
        return str(self.value)
