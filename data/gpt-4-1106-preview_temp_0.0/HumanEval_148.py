def bf(planet1, planet2):
    solar_system = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in solar_system or planet2 not in solar_system:
        return ()
    index1, index2 = solar_system.index(planet1), solar_system.index(planet2)
    if index1 > index2:
        index1, index2 = index2, index1
    return tuple(solar_system[index1 + 1:index2])
