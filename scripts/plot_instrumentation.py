import argparse
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
from datetime import datetime

def read_csv(file_name):
    """
    Reads a CSV file containing timestamp and JSON data, returns a list of dictionaries.
    """
    ds = []
    try:
        with open(file_name, 'r') as file:

            units = file.readline() # Discard units because they mess up DictReader

            csv_reader = csv.DictReader(file)

            for row in csv_reader:

                # Extract relevant columns and store them in a dictionary
                data_dict = {
                    "timestamp":  float(row["seconds"]),
                    "P_INJECTOR": float(row["P_INJECTOR"]),
                    "P_N2O_FLOW": float(row["P_N2O_FLOW"]),
                    "P_RUN_TANK": float(row["P_RUN_TANK"]),
                    "L_RUN_TANK": float(row["L_RUN_TANK"]),
                    "T_RUN_TANK": float(row["T_RUN_TANK"]),
                    "T_INJECTOR": float(row["T_INJECTOR"])
                }
                ds.append(data_dict)
    except Exception as e:
        print(f"Error reading file {file_name}: {e}")
        exit()
    
    return ds

def remove_local_outliers(df, window_size=50, z_threshold=5):
    """
    Removes rows from the dataframe that are outliers compared to their local neighbors.
    
    Parameters:
    - window_size: Number of neighboring points to consider for local statistics.
    - z_threshold: The number of standard deviations a point must be away from the local mean to be considered an outlier.
    """
    # Define the columns to check for outliers
    columns_to_check = ['P_N2O_FLOW', 'P_RUN_TANK', 'L_RUN_TANK', 'T_RUN_TANK', 'T_INJECTOR']
    
    for col in columns_to_check:
        # Compute rolling mean and std (using a window of 'window_size')
        rolling_mean = df[col].rolling(window=window_size, center=True, min_periods=1).mean()
        rolling_std = df[col].rolling(window=window_size, center=True, min_periods=1).std()

        # Calculate z-scores based on local statistics
        z_scores = (df[col] - rolling_mean) / rolling_std
        
        # Remove rows where the z-score is greater than the threshold (i.e., outliers)
        df = df[np.abs(z_scores) < z_threshold]
    
    return df

def plot_data(df):
    """
    Plots the data with more x-ticks and gridlines.
    """
    timestamps = df['timestamp']
    P_INJECTOR = df['P_INJECTOR']
    P_N2O_FLOW = df['P_N2O_FLOW']
    P_RUN_TANK = df['P_RUN_TANK']
    L_RUN_TANK = df['L_RUN_TANK']
    T_RUN_TANK = df['T_RUN_TANK']
    T_INJECTOR = df['T_INJECTOR']

    # Create the first figure (P_N2O_FLOW, P_RUN_TANK, L_RUN_TANK)
    fig, axes = plt.subplots(4, 1, figsize=(10, 8), sharex=True)

    # Plot P_N2O_FLOW
    axes[0].plot(timestamps, P_N2O_FLOW, color='tab:blue')
    axes[0].set_ylabel('P_N2O_FLOW (psi)')
    axes[0].set_title('P_N2O_FLOW vs Time')
    axes[0].grid(True)

    # Plot P_RUN_TANK
    axes[1].plot(timestamps, P_RUN_TANK, color='tab:green')
    axes[1].set_ylabel('P_RUN_TANK (psi)')
    axes[1].set_title('P_RUN_TANK vs Time')
    axes[1].grid(True)

    # Plot P_INJECTOR
    axes[2].plot(timestamps, P_INJECTOR, color='tab:orange')
    axes[2].set_ylabel('P_INJECTOR (psi)')
    axes[2].set_title('P_INJECTOR vs Time')
    axes[2].grid(True)

    # Plot L_RUN_TANK
    axes[3].plot(timestamps, L_RUN_TANK, color='tab:grey')
    axes[3].set_ylabel('L_RUN_TANK (kg)')
    axes[3].set_title('L_RUN_TANK vs Time')
    axes[3].grid(True)

    # Increase the number of ticks on x-axis by setting the tick frequency
    axes[3].set_xlabel('Time (s)')

    # Set more ticks
    #num_ticks = 30  # You can adjust this value to control how many ticks you want
    #tick_locations = np.linspace(timestamps.min(), timestamps.max(), num_ticks)
    #axes[3].set_xticks(tick_locations)

    plt.tight_layout()

    # Create the second figure (T_RUN_TANK and T_INJECTOR)
    fig2, ax2 = plt.subplots(figsize=(10, 6))

    # Plot T_RUN_TANK and T_INJECTOR on the same plot
    ax2.plot(timestamps, T_RUN_TANK, label='T_RUN_TANK (°C)', color='tab:red')
    ax2.plot(timestamps, T_INJECTOR, label='T_INJECTOR (°C)', color='tab:purple')

    # Labeling and title
    ax2.set_xlabel('Time (seconds since epoch)')
    ax2.set_ylabel('Temperature (°C)')
    ax2.set_title('T_RUN_TANK and T_INJECTOR vs Time')
    ax2.legend()
    ax2.grid(True)  # Add gridlines to the second plot

    # Adjust x-ticks for the second plot
    #ax2.set_xticks(tick_locations)

    plt.tight_layout()

    # Show the plots
    plt.show()

def main():
    # Setup argument parser
    parser = argparse.ArgumentParser(description='Process and plot data from a CSV file containing timestamps and sensor readings.')
    parser.add_argument('csv_file', type=str, help='Path to the CSV file containing the data')
    args = parser.parse_args()

    # Read the CSV data
    ds = read_csv(args.csv_file)

    # Convert the list of dictionaries into a DataFrame for easier manipulation
    df = pd.DataFrame(ds)

    # Remove outliers from the data based on local statistics
    df_clean = remove_local_outliers(df)

    # Plot the cleaned data
    plot_data(df_clean)

if __name__ == "__main__":
    main()

