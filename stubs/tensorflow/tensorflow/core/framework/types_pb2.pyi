"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _DataType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _DataTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_DataType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    DT_INVALID: _DataType.ValueType  # 0
    """Not a legal value for DataType.  Used to indicate a DataType field
    has not been set.
    """
    DT_FLOAT: _DataType.ValueType  # 1
    """Data types that all computation devices are expected to be
    capable to support.
    """
    DT_DOUBLE: _DataType.ValueType  # 2
    DT_INT32: _DataType.ValueType  # 3
    DT_UINT8: _DataType.ValueType  # 4
    DT_INT16: _DataType.ValueType  # 5
    DT_INT8: _DataType.ValueType  # 6
    DT_STRING: _DataType.ValueType  # 7
    DT_COMPLEX64: _DataType.ValueType  # 8
    """Single-precision complex"""
    DT_INT64: _DataType.ValueType  # 9
    DT_BOOL: _DataType.ValueType  # 10
    DT_QINT8: _DataType.ValueType  # 11
    """Quantized int8"""
    DT_QUINT8: _DataType.ValueType  # 12
    """Quantized uint8"""
    DT_QINT32: _DataType.ValueType  # 13
    """Quantized int32"""
    DT_BFLOAT16: _DataType.ValueType  # 14
    """Float32 truncated to 16 bits.  Only for cast ops."""
    DT_QINT16: _DataType.ValueType  # 15
    """Quantized int16"""
    DT_QUINT16: _DataType.ValueType  # 16
    """Quantized uint16"""
    DT_UINT16: _DataType.ValueType  # 17
    DT_COMPLEX128: _DataType.ValueType  # 18
    """Double-precision complex"""
    DT_HALF: _DataType.ValueType  # 19
    DT_RESOURCE: _DataType.ValueType  # 20
    DT_VARIANT: _DataType.ValueType  # 21
    """Arbitrary C++ data types"""
    DT_UINT32: _DataType.ValueType  # 22
    DT_UINT64: _DataType.ValueType  # 23
    DT_FLOAT_REF: _DataType.ValueType  # 101
    """Do not use!  These are only for parameters.  Every enum above
    should have a corresponding value below (verified by types_test).
    """
    DT_DOUBLE_REF: _DataType.ValueType  # 102
    DT_INT32_REF: _DataType.ValueType  # 103
    DT_UINT8_REF: _DataType.ValueType  # 104
    DT_INT16_REF: _DataType.ValueType  # 105
    DT_INT8_REF: _DataType.ValueType  # 106
    DT_STRING_REF: _DataType.ValueType  # 107
    DT_COMPLEX64_REF: _DataType.ValueType  # 108
    DT_INT64_REF: _DataType.ValueType  # 109
    DT_BOOL_REF: _DataType.ValueType  # 110
    DT_QINT8_REF: _DataType.ValueType  # 111
    DT_QUINT8_REF: _DataType.ValueType  # 112
    DT_QINT32_REF: _DataType.ValueType  # 113
    DT_BFLOAT16_REF: _DataType.ValueType  # 114
    DT_QINT16_REF: _DataType.ValueType  # 115
    DT_QUINT16_REF: _DataType.ValueType  # 116
    DT_UINT16_REF: _DataType.ValueType  # 117
    DT_COMPLEX128_REF: _DataType.ValueType  # 118
    DT_HALF_REF: _DataType.ValueType  # 119
    DT_RESOURCE_REF: _DataType.ValueType  # 120
    DT_VARIANT_REF: _DataType.ValueType  # 121
    DT_UINT32_REF: _DataType.ValueType  # 122
    DT_UINT64_REF: _DataType.ValueType  # 123

class DataType(_DataType, metaclass=_DataTypeEnumTypeWrapper):
    """(== suppress_warning documentation-presence ==)
    LINT.IfChange
    """

DT_INVALID: DataType.ValueType  # 0
"""Not a legal value for DataType.  Used to indicate a DataType field
has not been set.
"""
DT_FLOAT: DataType.ValueType  # 1
"""Data types that all computation devices are expected to be
capable to support.
"""
DT_DOUBLE: DataType.ValueType  # 2
DT_INT32: DataType.ValueType  # 3
DT_UINT8: DataType.ValueType  # 4
DT_INT16: DataType.ValueType  # 5
DT_INT8: DataType.ValueType  # 6
DT_STRING: DataType.ValueType  # 7
DT_COMPLEX64: DataType.ValueType  # 8
"""Single-precision complex"""
DT_INT64: DataType.ValueType  # 9
DT_BOOL: DataType.ValueType  # 10
DT_QINT8: DataType.ValueType  # 11
"""Quantized int8"""
DT_QUINT8: DataType.ValueType  # 12
"""Quantized uint8"""
DT_QINT32: DataType.ValueType  # 13
"""Quantized int32"""
DT_BFLOAT16: DataType.ValueType  # 14
"""Float32 truncated to 16 bits.  Only for cast ops."""
DT_QINT16: DataType.ValueType  # 15
"""Quantized int16"""
DT_QUINT16: DataType.ValueType  # 16
"""Quantized uint16"""
DT_UINT16: DataType.ValueType  # 17
DT_COMPLEX128: DataType.ValueType  # 18
"""Double-precision complex"""
DT_HALF: DataType.ValueType  # 19
DT_RESOURCE: DataType.ValueType  # 20
DT_VARIANT: DataType.ValueType  # 21
"""Arbitrary C++ data types"""
DT_UINT32: DataType.ValueType  # 22
DT_UINT64: DataType.ValueType  # 23
DT_FLOAT_REF: DataType.ValueType  # 101
"""Do not use!  These are only for parameters.  Every enum above
should have a corresponding value below (verified by types_test).
"""
DT_DOUBLE_REF: DataType.ValueType  # 102
DT_INT32_REF: DataType.ValueType  # 103
DT_UINT8_REF: DataType.ValueType  # 104
DT_INT16_REF: DataType.ValueType  # 105
DT_INT8_REF: DataType.ValueType  # 106
DT_STRING_REF: DataType.ValueType  # 107
DT_COMPLEX64_REF: DataType.ValueType  # 108
DT_INT64_REF: DataType.ValueType  # 109
DT_BOOL_REF: DataType.ValueType  # 110
DT_QINT8_REF: DataType.ValueType  # 111
DT_QUINT8_REF: DataType.ValueType  # 112
DT_QINT32_REF: DataType.ValueType  # 113
DT_BFLOAT16_REF: DataType.ValueType  # 114
DT_QINT16_REF: DataType.ValueType  # 115
DT_QUINT16_REF: DataType.ValueType  # 116
DT_UINT16_REF: DataType.ValueType  # 117
DT_COMPLEX128_REF: DataType.ValueType  # 118
DT_HALF_REF: DataType.ValueType  # 119
DT_RESOURCE_REF: DataType.ValueType  # 120
DT_VARIANT_REF: DataType.ValueType  # 121
DT_UINT32_REF: DataType.ValueType  # 122
DT_UINT64_REF: DataType.ValueType  # 123
global___DataType = DataType

@typing_extensions.final
class SerializedDType(google.protobuf.message.Message):
    """Represents a serialized tf.dtypes.Dtype"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATATYPE_FIELD_NUMBER: builtins.int
    datatype: global___DataType.ValueType
    def __init__(
        self,
        *,
        datatype: global___DataType.ValueType | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["datatype", b"datatype"]) -> None: ...

global___SerializedDType = SerializedDType