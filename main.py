# main.py

import weather_analysis as wa

def weather_analyze(file_path):
    """
    Analyzes weather data from a file and returns the results as a dictionary.
    """
    data = wa.read_weather_data(file_path)
    dict_out = {}
    dict_out["average_temperature"] = wa.calculate_average_temperature(data)
    dict_out["total_rainfall"] = wa.calculate_total_rainfall(data)
    dict_out["highest_temperature"] = {"date": wa.find_highest_temperature(data)[0], "temperature": wa.find_highest_temperature(data)[1]}
    dict_out["lowest_temperature"] = {"date": wa.find_lowest_temperature(data)[0], "temperature": wa.find_lowest_temperature(data)[1]}
    dict_out["most_rainfall"] = {"date": wa.find_day_with_most_rainfall(data)[0], "rainfall": wa.find_day_with_most_rainfall(data)[1]}
    return dict_out


if __name__ == "__main__":
    
    results = weather_analyze("weather_data.txt") #or the path to the file
    print(results)