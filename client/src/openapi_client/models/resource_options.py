"""
infrastructure-product API

Backend service for the appliedAI infrastructure product

The version of the OpenAPI document: 0.1.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing_extensions import Self


class ResourceOptions(BaseModel):
    """
    ResourceOptions
    """  # noqa: E501

    memory: StrictStr | None = None
    cpu: StrictStr | None = None
    gpu: StrictInt | None = None
    __properties: ClassVar[list[str]] = ["memory", "cpu", "gpu"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self | None:
        """Create an instance of ResourceOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: set[str] = set()

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if memory (nullable) is None
        # and model_fields_set contains the field
        if self.memory is None and "memory" in self.model_fields_set:
            _dict["memory"] = None

        # set to None if cpu (nullable) is None
        # and model_fields_set contains the field
        if self.cpu is None and "cpu" in self.model_fields_set:
            _dict["cpu"] = None

        # set to None if gpu (nullable) is None
        # and model_fields_set contains the field
        if self.gpu is None and "gpu" in self.model_fields_set:
            _dict["gpu"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of ResourceOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "memory": obj.get("memory"),
            "cpu": obj.get("cpu"),
            "gpu": obj.get("gpu"),
        })
        return _obj
