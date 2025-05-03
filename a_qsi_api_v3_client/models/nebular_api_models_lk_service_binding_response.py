from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NebularApiModelsLkServiceBindingResponse")


@_attrs_define
class NebularApiModelsLkServiceBindingResponse:
    """
    Attributes:
        qr_data (Union[None, Unset, str]): <div class="apidocs-russian">Токен для QR (время жизни: 1 час с момента
            получения)</div>
            <div class="apidocs-english">QR Token</div>
    """

    qr_data: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        qr_data: Union[None, Unset, str]
        if isinstance(self.qr_data, Unset):
            qr_data = UNSET
        else:
            qr_data = self.qr_data

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if qr_data is not UNSET:
            field_dict["qrData"] = qr_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_qr_data(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        qr_data = _parse_qr_data(d.pop("qrData", UNSET))

        nebular_api_models_lk_service_binding_response = cls(
            qr_data=qr_data,
        )

        return nebular_api_models_lk_service_binding_response
