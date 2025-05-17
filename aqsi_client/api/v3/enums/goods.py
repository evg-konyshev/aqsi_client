from enum import Enum

class MeasurementUnit(Enum):
    """Enum representing different units of measurement."""

    DEFAULT_CATEGORY =  1197

    PIECE = 0               # Штука или Единица

    # Weight units
    GRAM = 10               # Грамм
    KILOGRAM = 11           # Килограмм
    TON = 12                # Тонна

    # Length units
    CENTIMETER = 20         # Сантиметр
    DECIMETER = 21          # Дециметр
    METER = 22              # Метр

    # Area units
    SQUARE_CENTIMETER = 30  # Квадратный сантиметр
    SQUARE_DECIMETER = 31   # Квадратный дециметр
    SQUARE_METER = 32       # Квадратный метр

    # Volume units
    MILLILITER = 40         # Миллилитр
    LITER = 41              # Литр
    CUBIC_METER = 42        # Кубический метр

    # Energy units
    KILOWATT_HOUR = 50      # Киловатт час
    GIGACALORIE = 51        # Гигакаллория

    # Time units
    DAY = 70                # Сутки (день)
    HOUR = 71               # Час
    MINUTE = 72             # Минута
    SECOND = 73             # Секунда

    # Data units
    KILOBYTE = 80           # Килобайт
    MEGABYTE = 81           # Мегабайт
    GIGABYTE = 82           # Гигабайт
    TERABYTE = 83           # Терабайт

    # Other
    OTHER = 255             # Иное


class TaxRates(Enum):
    """Enum representing different VAT rates."""

    DEFAULT_CATEGORY_RATE = 1      # Ставка НДС по умолчанию на категорию
    RATE_20 = 2                    # Ставка НДС 20%
    RATE_10 = 3                    # Ставка НДС 10%
    CALCULATED_20_120 = 4          # Ставка НДС расч. 20/120
    CALCULATED_10_110 = 5          # Ставка НДС расч. 10/110
    RATE_0 = 6                     # Ставка НДС 0%
    TAX_EXEMPT = 7                 # НДС не облагается
    RATE_5 = 8                     # Ставка НДС 5%
    RATE_7 = 9                     # Ставка НДС 7%
    CALCULATED_5_105 = 10          # Ставка НДС расч. 5/105
    CALCULATED_7_107 = 11          # Ставка НДС расч. 7/107


class CalculationItemType(Enum):
    """Enum representing different types of calculation items."""

    DEFAULT_CATEGORY_ITEM = 1      # Признак предмета расчета по умолчанию на категорию
    GOOD = 2                       # Товар
    EXCISABLE_GOOD = 3             # Подакцизный товар
    WORK = 4                       # Работа
    SERVICE = 5                    # Услуга
    GAMBLING_RATE = 6              # Ставка азартной игры
    GAMBLING_WIN = 7               # Выигрыш азартной игры
    LOTTERY_TICKET = 8             # Лотерейный билет
    LOTTERY_WIN = 9                # Выигрыш лотереи
    IP_PROVIDING = 10              # Предоставление РИД
    PAYMENT = 11                   # Платёж
    AGENT_FEE = 12                 # Агентское вознаграждение
    PAYOUT = 13                    # Выплата
    OTHER_ITEM = 14                # Иной предмет расчета
    PROPERTY_RIGHT = 15            # Имущественное право
    NON_OPERATING_INCOME = 16      # Внереализационный доход
    OTHER_PAYMENTS = 17            # Иные платежи и взносы
    TRADING_FEE = 18               # Торговый сбор
    RESORT_FEE = 19                # Курортный сбор
    DEPOSIT = 20                   # Залог
    EXPENSE = 21                   # Расход
    INDIVIDUAL_PENSION_INSURANCE = 22  # Взносы на обязательное пенсионное страхование ИП
    PENSION_INSURANCE = 23         # Взносы на обязательное пенсионное страхование
    INDIVIDUAL_HEALTH_INSURANCE = 24  # Взносы на обязательное медицинское страхование ИП
    HEALTH_INSURANCE = 25          # Взносы на обязательное медицинское страхование
    SOCIAL_INSURANCE = 26          # Взносы на обязательное социальное страхование
    CASINO_PAYMENT = 27            # Платёж казино
    CASH_ISSUANCE = 28             # Выдача денежных средств
    LOST_EXCISABLE_MARKED_GOOD = 30  # Подакцизный маркированный товар, код маркировки утерян, АТНМ
    EXCISABLE_MARKED_GOOD = 31     # Подакцизный товар с маркировкой, АТМ
    LOST_MARKED_GOOD = 32          # Маркированный товар, код маркировки утерян, ТНМ
    NON_EXCISABLE_MARKED_GOOD = 33 # Неподакцизный товар с маркировкой, ТМ

class PaymentMethodType(Enum):
    """Enum representing different payment method types."""

    FULL_PREPAYMENT = 1        # Предоплата 100%
    PARTIAL_PREPAYMENT = 2     # Частичная предоплата
    ADVANCE = 3                # Аванс
    FULL_PAYMENT = 4           # Полный расчёт
    PARTIAL_PAYMENT_CREDIT = 5 # Частичный расчёт и кредит
    CREDIT_TRANSFER = 6        # Передача в кредит
    CREDIT_PAYMENT = 7         # Оплата кредита

class ProductTypes(str, Enum):
    SIMPLE = 'simple'
    INGREDIENT = 'ingredient'
    COMPLEX = 'complex'

class AccountingMethods(str, Enum):
    CHILDREN = 'children'
    SELF = 'self'
    SELF_FIRST = 'self first'


class MarkingTypes(Enum):
    """Enum representing different types of product markings."""

    NATURAL_FUR_GOODS = 1               # Товары из натурального меха
    MEDICINAL_GOODS = 2                 # Лекарственные товары
    TOBACCO_PRODUCTS = 3                # Табачная продукция
    FOOTWEAR_GOODS = 4                  # Обувные товары
    PERFUMES_EAU_DE_TOILETTE = 5        # Духи и туалетная вода
    NEW_PNEUMATIC_RUBBER_TIRES = 6      # Шины и покрышки пневматические резиновые новые
    # 7 - Use LIGHT_INDUSTRY_GOODS (11) for leather clothing items
    # 8 - Use LIGHT_INDUSTRY_GOODS (11) for knitted blouses
    # 9 - Use LIGHT_INDUSTRY_GOODS (11) for men's outerwear
    # 10 - Use LIGHT_INDUSTRY_GOODS (11) for women's outerwear
    LIGHT_INDUSTRY_GOODS = 11           # Товары легкой промышленности
    CAMERAS_FLASHES = 12                # Фотокамеры (кроме кинокамер), фотовспышки и лампы-вспышки
    DAIRY_PRODUCTS = 13                 # Молочная продукция
    BICYCLES_FRAMES = 14                # Велосипеды и велосипедные рамы
    ALTERNATIVE_TOBACCO_PRODUCTS = 15   # Альтернативная табачная продукция
    DIETARY_SUPPLEMENTS = 16            # Биологически активные добавки к пище (БАД)
    NICOTINE_PRODUCTS = 17              # Никотиносодержащая продукция
    BEER_ALCOHOLIC_DRINKS = 18          # Пиво, напитки, изготовленные на основе пива, и слабоалкогольные напитки с маркировкой ЧЗ, подлежащие списанию в УТМ ЕГАИС
    MEDICAL_DEVICES = 19                # Медицинские изделия
    ANTISEPTICS_DISINFECTANTS = 20      # Антисептики и дезинфицирующие средства
    BOTTLED_WATER = 21                  # Упакованная вода
    EGAIS_ALCOHOL = 22                  # Алкогольная продукция ЕГАИСа
    UNMARKED_LOW_ALCOHOL_DRINKS = 23    # Немаркированные слабоалкогольные напитки, подлежащие списанию в УТМ ЕГАИС
    NON_ALCOHOLIC_BEER = 24             # Безалкогольное пиво
    JUICE_SOFT_DRINKS = 25              # Соковая продукция и безалкогольные напитки
    ANIMAL_FEED = 26                    # Корма для животных
    SEAFOOD = 27                        # Морепродукты
    VETERINARY_DRUGS = 28               # Ветеринарные препараты
    CANNED_GOODS = 29                   # Консервированная продукция
    VEGETABLE_OILS = 30                 # Растительные масла


class PaymentMethod(Enum):
    """Enum representing different payment methods."""

    FULL_PREPAYMENT = 1          # Предоплата 100%
    PARTIAL_PREPAYMENT = 2       # Частичная предоплата
    ADVANCE_PAYMENT = 3          # Аванс
    FULL_PAYMENT = 4             # Полный расчёт
    PARTIAL_PAYMENT_CREDIT = 5   # Частичный расчёт и кредит
    CREDIT_TRANSFER = 6          # Передача в кредит
    CREDIT_PAYMENT = 7           # Оплата кредита