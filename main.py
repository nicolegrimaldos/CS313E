airport_codes = {
    'Houston': 'IAH',
    'Atlanta': 'ATL',
    'Vancouver': 'YVR',
    'Dallas': 'DAL',
    'London': 'LHR'
}

new_airport_codes = {
    'Los Angeles': 'LAX',
    'San Francisco': 'SFO',
    'London': 'LCY'
}

print(airport_codes.get('London', 'na'))
print(airport_codes.get('San Francisco', 'na'))
airport_codes.update(new_airport_codes)
print(airport_codes.get('London', 'na'))
print(airport_codes.get('San Francisco', 'na'))