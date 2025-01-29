# Instructions:
# 1. **Remove the TODO comment and pass statement** once you’ve completed the function implementation.
#    - The TODO and pass are placeholders indicating that the function is not yet complete.
#    - Once the function is implemented, these should be removed to keep the code clean.
# 
# 2. **Best Coding Practices**:
#    - In professional programming, finalizing the code means removing unnecessary placeholders.
#    - This ensures your code is ready for review, testing, and does not contain clutter.
# 
# 3. **Adding Docstrings**:
#    - After removing TODO and pass, add a **docstring** for each function.
#    - The docstring should explain the function’s purpose, parameters, and expected output.
#    - Proper documentation improves code readability and helps with debugging and maintenance.

def read_weather_data(file_path: str):
    """
    Reads weather data from a file as List[Tuple(Date: str, Temperature: float, Rainfall: float)]
    """
    content_list = open(file_path).readlines()
    final_list = []
    for i in content_list:
        item_list = i.split(",")
        final_list.append((item_list[0], float(item_list[1]), float(item_list[2])))
    return final_list

def calculate_average_temperature(weather_data):
    """
    Calculates the average temperature from the weather data, outputs float.
    """
    running_total = 0
    for i in weather_data:
        running_total += i[1]
    return running_total/len(weather_data)



def calculate_total_rainfall(weather_data):
    """
    Calculates the total rainfall from the weather data, outputs float.
    """
    running_total = 0
    for i in weather_data:
        running_total += i[2]
    return running_total

def find_highest_temperature(weather_data):
    """
    Finds the highest temperature and the corresponding date from the weather data, outputs Tuple(Date: str, Temperature: float).
    """
    maxi = max([i[1] for i in weather_data])
    for i in weather_data:
        if i[1] == maxi:
            return (i[0], i[1])


def find_lowest_temperature(weather_data):
    """
    Finds the lowest temperature and the corresponding date from the weather data, outputs Tuple(Date: str, Temperature: float).
    """
    mini = min([i[1] for i in weather_data])
    for i in weather_data:
        if i[1] == mini:
            return (i[0], i[1])

def find_day_with_most_rainfall(weather_data):
    """
    Finds the day with the most rainfall from the weather dataoutputs Tuple(Date: str, Rainfall: float).
    """
    maxi = max([i[2] for i in weather_data])
    for i in weather_data:
        if i[2] == maxi:
            return (i[0], i[2])