import typing 

class City(typing.NamedTuple):
    continent: str
    name: str
    country: str

cities = [
    City('Asia', 'Tokyo', 'JP'),
    City('Asia', 'Delhi', 'IN'),
    City('North America', 'Mexico City', 'MX'),
    City('North America', 'New York', 'US'),
    City('South America', 'Sao Paulo', 'BR'),
]

def simple_matching(x):
    match x:
        case float():
            print(x, 'is float')
        case int():
            print(x, 'is int')
        case str():
            print(x, 'is string')
        case _:
            print('Unmatched operand')


def match_asian_cities(cities):
    '''Return only countries'''

    results = []
    for city in cities:
        match city:
            case City(continent='Asia', country=cc):
                results.append(cc)
    return results

def match_asian_cities_pos(cities):
    '''__match_args__ must be set for class'''

    results = []
    for city in cities:
        match city:
            case City('Asia'):
                results.append(city)
    return results

def match_asian_cities_pos_v2(cities):
    results = []
    for city in cities:
        match city:
            case City('Asia', _, country):
                results.append(country)
    return results

if __name__ == '__main__':
    res1 = match_asian_cities(cities)
    res2 = match_asian_cities_pos(cities)
    res3 = match_asian_cities_pos_v2(cities)
    print('res1: ', res1)
    print('res2: ', res2)
    print('res3: ', res3)







