def format_number(value, prefix= ""):
    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'.replace(".",",")
        value /= 1000
    return f'{prefix} {value:.2f} milhões'.replace(".",",")