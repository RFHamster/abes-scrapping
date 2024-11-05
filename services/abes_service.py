def convert_to_int(value):
    value = value.strip().replace('$', '')

    if 'B' in value:
        return int(float(value.replace('B', '').strip()) * 1_000_000_000)
    elif 'T' in value:
        return int(float(value.replace('T', '').strip()) * 1_000_000_000_000)
    elif 'M' in value:
        return int(float(value.replace('M', '').strip()) * 1_000_000)
    else:
        return int(float(value))


def format_pizza_br_x_la(dict_data):
    sorted_data = sorted(
        dict_data, key=lambda x: x['study_year'], reverse=True
    )
    labels = ['Brasil', 'América Latina']
    datasets = []

    for item in sorted_data:
        label = 'BRxLA_' + item['study_year']
        data = []
        background_color = ['rgba(0, 148, 64, 0.8)', 'rgba(255, 100, 0, 0.8)']

        data.append(convert_to_int(item['brazil_movement']))
        data.append(convert_to_int(item['latin_america_investment']))

        data_dict = {
            'label': label,
            'data': data,
            'backgroundColor': background_color,
        }

        datasets.append(data_dict)

    return {'labels': labels, 'datasets': datasets}
