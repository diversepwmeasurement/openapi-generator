# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import re  # noqa: F401
import sys  # noqa: F401
import typing
import urllib3
import functools  # noqa: F401
from urllib3._collections import HTTPHeaderDict

from unit_test_api import api_client, exceptions
import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from unit_test_api import schemas  # noqa: F401



class SchemaFor200ResponseBodyApplicationJson(
    schemas.AnyTypeSchema,
):


    class MetaOapg:
        required = {
            "foo\"bar",
            "foo\nbar",
            "foo\fbar",
            "foo\tbar",
            "foo\rbar",
            "foo\\bar",
        }
        additional_properties = schemas.AnyTypeSchema

    
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["foo\\\"bar"]) -> MetaOapg.additional_properties: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["foo\\nbar"]) -> MetaOapg.additional_properties: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["foo\\fbar"]) -> MetaOapg.additional_properties: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["foo\\tbar"]) -> MetaOapg.additional_properties: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["foo\\rbar"]) -> MetaOapg.additional_properties: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["foo\\\\bar"]) -> MetaOapg.additional_properties: ...
    
    def __getitem__(self, name: str) -> MetaOapg.additional_properties:
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
    ) -> 'SchemaFor200ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )