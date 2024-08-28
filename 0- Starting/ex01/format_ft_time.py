import time
from datetime import date

# Get the current time in seconds since the epoch
current_time = time.time()

# Split the time into whole seconds and fractional seconds
whole_seconds, fractional_seconds = divmod(current_time, 1)

# Format the whole seconds with commas
formatted_seconds = "{:,.0f}".format(whole_seconds)

# Convert the fractional seconds to a string, remove the "0." at the start, and append it to the formatted whole seconds
formatted_time = formatted_seconds + "{:.4f}".format(fractional_seconds)[1:]

# Scientific format the time in scientific notation
sci_formatted_time = "{:.2e}".format(current_time)

# Print the formatted time
print("Seconds since January 1, 1970:", formatted_time, "or ", sci_formatted_time, " in scientific notation")

# Get the current date
current_date = date.today()

# Format the date
formatted_date = current_date.strftime("%b %d %Y")

print(formatted_date)
