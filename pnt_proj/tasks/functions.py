def parse_elev(elevations):
    new_list = []
    for idx, elev in enumerate(elevations, 1):
        min_max = elev.split('-')
        if len(elevations) == 1:
            new_list = min_max
        elif idx == 1:
            new_list.append(min_max[0])
        elif idx == len(elevations):
            if len(min_max) == 1:
                new_list = [f'{new_list[0]}+']
            else:
                new_list.append(min_max[1])

    return new_list