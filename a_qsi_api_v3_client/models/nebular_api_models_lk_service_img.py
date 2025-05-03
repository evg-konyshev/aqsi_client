from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsLkServiceImg")


@_attrs_define
class NebularApiModelsLkServiceImg:
    """<div class="apidocs-russian">Модель изображения</div>
    <div class="apidocs-english">Image model</div>

        Attributes:
            data (Union[None, Unset, str]): <div class="apidocs-russian">Изображение в формате base64</div>
                <div class="apidocs-english">The image in base64 format</div>
            name (Union[None, Unset, str]): <div class="apidocs-russian">Название файла с расширением</div>
                <div class="apidocs-english">File name with extension</div>
            size (Union[Unset, int]): <div class="apidocs-russian">Размер файла</div>
                <div class="apidocs-english">File size</div>
            type_ (Union[None, Unset, str]): <div class="apidocs-russian">MIME тип, например  image/png</div>
                <div class="apidocs-english">MIME type, e.g. image / png</div>
    """

    data: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    type_: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        data: Union[None, Unset, str]
        if isinstance(self.data, Unset):
            data = UNSET
        else:
            data = self.data

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        size = self.size

        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if name is not UNSET:
            field_dict["name"] = name
        if size is not UNSET:
            field_dict["size"] = size
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_data(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        size = d.pop("size", UNSET)

        def _parse_type_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type_ = _parse_type_(d.pop("type", UNSET))

        nebular_api_models_lk_service_img = cls(
            data=data,
            name=name,
            size=size,
            type_=type_,
        )

        return nebular_api_models_lk_service_img
