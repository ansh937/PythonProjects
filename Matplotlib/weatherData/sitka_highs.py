from pathlib import Path
import csv
path=Path("/Users/macm2/Desktop/pythoon/Matplotlib/weatherData/sitka_weather_07-2021_simple.csv")
lines=path.read_text().splitlines()

reader=csv.reader(lines)
header_row=next(reader)
print(header_row)