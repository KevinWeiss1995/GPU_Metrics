import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gpu_usage_442.log')
print("First few rows of the data:")
print(df.head())

print("\nColumn names in the data:")
print(df.columns)

df.columns = df.columns.str.strip()

if 'power.draw [W]' not in df.columns:
    print("\n'power.draw [W]' column not found! Available columns:")
    print(df.columns)
else:
    print("\n'power.draw [W]' column found successfully!")

df['timestamp'] = pd.to_datetime(df['timestamp'])

start_time = df['timestamp'].min()
end_time = df['timestamp'].max()

duration = end_time - start_time
duration_minutes = duration.total_seconds() // 60
duration_seconds = duration.total_seconds() % 60

duration_label = f"Total duration: {int(duration_minutes)} min {int(duration_seconds)} s"

plt.figure(figsize=(12, 7))
plt.plot(df['timestamp'], df['utilization.gpu [%]'], label='GPU Utilization (%)', color='b')

if 'power.draw [W]' in df.columns:
    plt.plot(df['timestamp'], df['power.draw [W]'], label='Power Draw (W)', color='r')

plt.xlabel('Timestamp')
plt.ylabel('Usage')
plt.title('A100: Large Grid GPU Utilization and Power Draw Over Time')

plt.legend(loc='upper left')

plt.gca().text(0.98, 0.98, duration_label, transform=plt.gca().transAxes,
               fontsize=12, color='black',
               ha='right', va='top',
               bbox=dict(boxstyle='round,pad=0.5', edgecolor='black', facecolor='white'))

plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()
