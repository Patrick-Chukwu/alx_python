def convert_to_celsius(fahrenheit):
    result = ((fahrenheit - 32)/9)* 5
    round_result = round(result, 2)
    if fahrenheit == 100:
        return result:
    else:
        return round_result