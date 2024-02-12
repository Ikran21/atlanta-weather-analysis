import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file into a Pandas DataFrame
file_path = r'C:\Users\ikran\Downloads\atlanta_weather.csv'
df = pd.read_csv(file_path)

# Step 2: Plotting the data
plt.figure(figsize=(10, 6))

# High temperature line
plt.plot(df['Month'], df['High'], 'b--o', label='High Temperature')

# Low temperature line (corrected format string)
plt.plot(df['Month'], df['Low'], 'g--^', label='Low Temperature')

# Annotate the highest temperature of the year
max_temp = df['High'].max()
max_temp_month = df.loc[df['High'].idxmax()]['Month']
plt.annotate('Highest of the Year',
             xy=(max_temp_month, max_temp),
             xytext=(max_temp_month, max_temp + 2),  # Adjusted xytext for better positioning
             arrowprops=dict(facecolor='red', edgecolor='red', arrowstyle='->', linewidth=2),
             fontsize=12)

# Step 3: Customize the plot
plt.title('Atlanta – Monthly Temperature', fontsize=20)
plt.xlabel('Month', fontsize=16)
plt.ylabel('Temperature (Fahrenheit)', fontsize=16)
plt.legend(fontsize=14)
plt.grid(True)

# Step 4: Save the plot as 'atlanta_weather_plot.jpg'
plt.savefig('atlanta_weather_plot.jpg')

# Step 5: Show the plot (optional)
plt.show()
