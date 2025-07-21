import pandas as pd
import dtale

def read_csv_to_dataframe(csv_path):
    """
    Read a CSV file and convert it to a pandas DataFrame.
    
    Args:
        csv_path (str): Path to the CSV file
        
    Returns:
        pandas.DataFrame: DataFrame containing the CSV data
    """
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_path)
        print(f"Successfully read CSV file: {csv_path}")
        print(f"DataFrame shape: {df.shape}")
        return df
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

def display_with_dtale(df):
    """
    Display a DataFrame using dtale.
    
    Args:
        df (pandas.DataFrame): DataFrame to display
    """
    if df is not None:
        # Launch dtale with the DataFrame - use host='0.0.0.0' to make it accessible from any interface
        d = dtale.show(df, host='0.0.0.0')
        # Get the URL where dtale is running
        print(f"dtale instance running at: {d._main_url}")
        print(f"También puedes acceder usando: http://localhost:40000/dtale/main/1")
        # Keep the script running to maintain the dtale instance
        print("Press Ctrl+C to exit")
        try:
            # This will keep the script running until interrupted
            while True:
                import time
                time.sleep(1)
        except KeyboardInterrupt:
            print("Cerrando dtale...")
        except Exception as e:
            print(f"Error: {e}")
            print("Cerrando dtale...")
        finally:
            print("Sesión de dtale finalizada")

def main():
    # Set up command line argument parsing
    csv_path = "datos_personas.csv"
    
    # Read the CSV file into a DataFrame
    df = read_csv_to_dataframe(csv_path)
    
    # Display the DataFrame using dtale
    display_with_dtale(df)

if __name__ == "__main__":
    main()
