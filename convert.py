def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      0°C × 9/5) + 32 = 32°F
      convert_temp("f", "c", 212) => 100.0
      (32°F − 32) × 5/9 = 0°C

    """
    if not(unit_in in ["f", "c"] and unit_out in ["f", "c"]):
        # raise ValueError("unit must be in Celcius (c) or Fahrenheit (f)")
        return f"Invalid unit {unit_in}" if not(unit_in in ["f", "c"]) else f"Invalid unit {unit_out}"
    if unit_in == unit_out:
        return temp
    if unit_in.lower() == "f" and unit_out.lower() == "c":
        return (temp-32)*5/9
    elif unit_in.lower() == "c" and unit_out.lower() == "f":
        return (temp * 9/5) + 32
    # YOUR CODE HERE


print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")
