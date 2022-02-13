traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),
                ('ESP', 'XDA205856')]

# <<< Formatting >>>
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

# <<< Unpacking >>>
for country, _ in traveler_ids:
    print(country)

usa_passport = traveler_ids[0]
country, code = usa_passport

# Swapping value without using a temp variable
country, code = code, country

# Using the * operator
t = (20, 8)
divmod(*t)

# Grab excess items
a, b, *rest = range(5)
a1, *rest1, e = range(5)

# Nested tuples
metro_areas = [('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
               ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
               ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
               ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
               ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
               ]
name, cc, pop, (lat, long) = metro_areas[0]

# <<< Named tuples >>>
from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35, 140))
print(tokyo.population)

# Attributes
print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
delhi._asdict()