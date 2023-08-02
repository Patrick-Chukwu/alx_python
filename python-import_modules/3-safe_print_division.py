def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Inside result: None")
    except TypeError:
        print("Inside result: None")
    else:
        print("Inside result: {}".format(result))
    finally:
        return result if 'result' in locals() else None
