from ariadne import ScalarType
from datetime import datetime

datetime_scalar = ScalarType("Datetime")


def serialize_datetime(value, *_):
    return value.isoformat()


datetime_scalar.set_serializer(serialize_datetime)
