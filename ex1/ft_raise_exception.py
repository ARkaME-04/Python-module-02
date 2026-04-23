def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    value = int(temp_str)
    if 0 >= value:
        raise ValueError(f"{value}°C is too cold for plants (min 0°C)")
    elif 40 <= value:
        raise ValueError(f"{value}°C is too hot for plants (max 40°C)")
    return value


def test_temperature() -> None:
    try:
        result = input_temperature("25")
        print(f"Temperature is now {result}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    try:
        result = input_temperature("abc")
        print(f"Temperature is now {result}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    try:
        result = input_temperature("100")
        print(f"Temperature is now {result}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    try:
        result = input_temperature("-50")
        print(f"Temperature is now {result}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    test_temperature()
