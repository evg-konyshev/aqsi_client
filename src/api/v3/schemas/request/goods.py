from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field

from api.v3.enums.goods import CalculationItemType, TaxRates, MeasurementUnit, ProductTypes, AccountingMethods, \
    MarkingTypes, PaymentMethod


class GoodImageSchema(BaseModel):
    """Схема изображения товара"""

    data: str | None = Field(None, description="Изображение в формате base64")
    size: int | None = Field(None, description="Размер изображения")
    type: str | None = Field(None, max_length=36, description="MIME тип, например image/png")


class GoodCreateRequestSchema(BaseModel):
    """Модель для создания товара в системе AQSI"""
    id: str = Field(..., max_length=36, description="Уникальный идентификатор товара в рамках аккаунта")
    group_id: str = Field(description="Идентификатор категории")
    type: ProductTypes = Field(..., max_length=36, description="Тип товара")
    productionCost: Decimal | None = Field(default=None, description='Себестоимость')
    marginPercent: Decimal | None = Field(default=None, description='Наценка')
    isWeight: int | None = Field(None, description='Является ли товар весовым')
    tax: Optional[TaxRates] = Field(None, max_length=50, description="Налоговая ставка (НДС и т.п.)")
    unit: str = Field(..., min_length=1,  max_length=16, description="Единица измерения товара")
    unitCode: MeasurementUnit | None = Field(None, description="Единица измерения")
    subject: CalculationItemType = Field(description="Предмет расчета")
    isOrderable: bool | None = Field(description='Возможность закупки товара у населения')
    name: str = Field(..., max_length=128, description="Имя товара")
    sku: str = Field(..., max_length=64, description="Артикул товара")
    cSku: str | None = Field(None, max_length=64, alias='1cSku', description="Артикул товара в 1с")
    barcodes: list[int] | None = Field(None, gt=0, max_digits=22,description='Штрих коды')
    img: GoodImageSchema | None = Field(None, description='Изображение')
    accountingMethod: AccountingMethods = Field(..., description='Тип списания')
    markingType: MarkingTypes | None = Field(None, description='Тип маркировки')
    paymentMethodType: PaymentMethod = Field(..., description='Вид оплаты')
    noReturn: int = Field(0, description='Возможно ли вернуть товар')