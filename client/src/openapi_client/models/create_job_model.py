"""
the jobq cluster workflow management tool backend

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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing_extensions import Self

from openapi_client.models.execution_mode import ExecutionMode
from openapi_client.models.job_options import JobOptions


class CreateJobModel(BaseModel):
    """
    CreateJobModel
    """  # noqa: E501

    name: StrictStr
    file: StrictStr
    image_ref: StrictStr
    mode: ExecutionMode
    options: JobOptions
    submission_context: dict[str, Any] | None = None
    __properties: ClassVar[list[str]] = [
        "name",
        "file",
        "image_ref",
        "mode",
        "options",
        "submission_context",
    ]

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
        """Create an instance of CreateJobModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of options
        if self.options:
            _dict["options"] = self.options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of CreateJobModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "file": obj.get("file"),
            "image_ref": obj.get("image_ref"),
            "mode": obj.get("mode"),
            "options": JobOptions.from_dict(obj["options"])
            if obj.get("options") is not None
            else None,
            "submission_context": obj.get("submission_context"),
        })
        return _obj
