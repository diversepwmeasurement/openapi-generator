# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import typing  # noqa: F401
import functools  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from unit_test_api import schemas  # noqa: F401


class NotMoreComplexSchema(
    schemas.ComposedSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        additional_properties = schemas.AnyTypeSchema
        
        
        class not_schema(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                class properties:
                    foo = schemas.StrSchema
                    __annotations__ = {
                        "foo": foo,
                    }
                additional_properties = schemas.AnyTypeSchema
            
            foo: MetaOapg.properties.foo
            
            @typing.overload
            def __getitem__(self, name: typing.Literal["foo"]) -> MetaOapg.properties.foo: ...
            
            def __getitem__(self, name: str) -> MetaOapg.additional_properties:
                # dict_instance[name] accessor
                return super().__getitem__(name)
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                foo: typing.Union[MetaOapg.properties.foo, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
            ) -> 'not_schema':
                return super().__new__(
                    cls,
                    *args,
                    foo=foo,
                    _configuration=_configuration,
                    **kwargs,
                )

    
    def __getitem__(self, name: str) -> MetaOapg.additional_properties:
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
    ) -> 'NotMoreComplexSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )