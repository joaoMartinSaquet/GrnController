import pandas as pd
import matplotlib.pyplot as plt

def main():
    """
    Plot yhat and y_gt against x
    """
    # Read the .txt file into a DataFrame
    df = pd.read_csv('res.txt', delimiter='\s+')
    df.columns = ['x', 'yhat', 'ygt']

    x = df['x']
    yhat = df['yhat']
    y_gt = df['ygt']

    # Plotting
    plt.figure(figsize=(10, 6))

    plt.plot(x, yhat, label='yhat', color='b', linestyle='-', marker='o')
    plt.plot(x, y_gt, label='y_gt', color='r', linestyle='--', marker='x')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Comparison of yhat and y_gt')

    plt.legend()

    plt.show()

if __name__ == "__main__":
    main()
