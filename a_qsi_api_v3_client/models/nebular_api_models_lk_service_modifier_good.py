from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nebular_api_models_lk_service_modifier_option import NebularApiModelsLkServiceModifierOption


T = TypeVar("T", bound="NebularApiModelsLkServiceModifierGood")


@_attrs_define
class NebularApiModelsLkServiceModifierGood:
    """Модификатор товара

    Attributes:
        id (UUID): <div class="apidocs-russian">Идентификатор модификатора</div>
            <div class="apidocs-english">Modifier identifier</div>
        name (str): <div class="apidocs-russian">Название модификатора</div>
            <div class="apidocs-english">Modifier name</div>
        type_ (str): <div class="apidocs-russian">Тип модификатора (возможные значения: radio-button, checkbox)</div>
            <div class="apidocs-english">Modifier type (possible values: radio-button, checkbox)</div>
        min_options (Union[Unset, int]): <div class="apidocs-russian">Минимум для выбора (по умолчанию 0)</div>
            <div class="apidocs-english">Minimum for selection (default 0)</div> Default: 0.
        max_options (Union[None, Unset, int]): <div class="apidocs-russian">Максимум  для выбора (по умолчанию 0)</div>
            <div class="apidocs-english">Maximum for selection (default 0)</div>
        options (Union[None, Unset, list['NebularApiModelsLkServiceModifierOption']]): <div class="apidocs-
            russian">Массив опций модификатора</div>
            <div class="apidocs-english">Array of modifier options</div>
    """

    id: UUID
    name: str
    type_: str
    min_options: Union[Unset, int] = 0
    max_options: Union[None, Unset, int] = UNSET
    options: Union[None, Unset, list["NebularApiModelsLkServiceModifierOption"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        type_ = self.type_

        min_options = self.min_options

        max_options: Union[None, Unset, int]
        if isinstance(self.max_options, Unset):
            max_options = UNSET
        else:
            max_options = self.max_options

        options: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, list):
            options = []
            for options_type_0_item_data in self.options:
                options_type_0_item = options_type_0_item_data.to_dict()
                options.append(options_type_0_item)

        else:
            options = self.options

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type_,
            }
        )
        if min_options is not UNSET:
            field_dict["minOptions"] = min_options
        if max_options is not UNSET:
            field_dict["maxOptions"] = max_options
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nebular_api_models_lk_service_modifier_option import NebularApiModelsLkServiceModifierOption

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        type_ = d.pop("type")

        min_options = d.pop("minOptions", UNSET)

        def _parse_max_options(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_options = _parse_max_options(d.pop("maxOptions", UNSET))

        def _parse_options(data: object) -> Union[None, Unset, list["NebularApiModelsLkServiceModifierOption"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                options_type_0 = []
                _options_type_0 = data
                for options_type_0_item_data in _options_type_0:
                    options_type_0_item = NebularApiModelsLkServiceModifierOption.from_dict(options_type_0_item_data)

                    options_type_0.append(options_type_0_item)

                return options_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NebularApiModelsLkServiceModifierOption"]], data)

        options = _parse_options(d.pop("options", UNSET))

        nebular_api_models_lk_service_modifier_good = cls(
            id=id,
            name=name,
            type_=type_,
            min_options=min_options,
            max_options=max_options,
            options=options,
        )

        return nebular_api_models_lk_service_modifier_good
