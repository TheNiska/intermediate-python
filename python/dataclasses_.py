from collections import namedtuple
from typing import NamedTuple, get_type_hints
from dataclasses import dataclass

# Best way to get type hints: get_type_hints(...)

'''## namedtuple ##
Only immutable.
Class syntax: None
To dict: x._asdict()
To get field names: x._fields
To get defaults: x._field_defaults
Get field types: None
New instance with changes: x._replace(...)
New class at runtime: namedtuple(...)
'''
Coordinate_namedtuple = namedtuple('Coordinate_namedtuple', 'lat lon')


'''## NamedTuple ##
Only immutable.
Class syntax: Yes
To dict: x._asdict()
To get field names: x._fields
To get defaults: x._field_defaults
Get field types: x.__annotations__
New instance with changes: x._replace(...)
New class at runtime: NamedTuple(...)
'''
Coordinate_NamedTuple = NamedTuple(
    'Coordinate_NamedTuple',
    [('lat', float), ('lon', float)]
)


class Coordinate_NamedTupleClass(NamedTuple):
    lat: float = 0
    lon: float = 0

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


@dataclass(frozen=True)
class Coordinate_DataClass:
    '''## dataclass ##
    Mutable and immutable.
    Class syntax: Yes
    To dict: dataclasses.asdict(x)
    To get field names: [f.name for f in dataclasses.fields(x)]
    To get defaults: [f.default for f in dataclasses.fields(x)]
    Get field types: x.__annotations__
    New instance with changes: dataclasses.replace(x, ...)
    New class at runtime: dataclasses.make_dataclass(...)
    '''
    lat: float = 0
    lon: float = 0

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


def main():
    init_classes = '''\
    Coordinate_namedtuple(15.2, 18.4)
    Coordinate_NamedTuple(15.2, 18.4)
    Coordinate_NamedTupleClass(15.2, 18.4)
    Coordinate_DataClass(15.2, 18.4)'''

    for cmd in init_classes.split('\n'):
        obj = eval(cmd.strip())

        class_name = str(type(obj))
        left, right = 17, class_name.rfind("'")
        print(f"{class_name[left:right]:-<30}{obj}")


if __name__ == '__main__':
    main()












