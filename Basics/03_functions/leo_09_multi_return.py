def measure():
    """measure temperature and humidity"""

    print("Start measuring...")
    temp = 39
    humidity = 50
    print("Measurement ended...")

    # tuple enables python to return multiple values
    # () can be omitted
    # return (temp, humidity)
    return temp, humidity


# tuple
result = measure()
print(result)

# if we need one of the value
print(result[0])
print(result[1])

# if need return multiple values, and need to process those values
# can declare multiple variables
gl_temp, gl_humidity = measure()
print(gl_temp)
print(gl_humidity)
