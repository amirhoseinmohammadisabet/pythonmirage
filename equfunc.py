import matplotlib.pyplot as plt
import numpy as np

def axbyz(a, b, c):
    x = np.linspace(-10, 10, 100)  # Generate 100 evenly spaced points between -10 and 10
    y = (-a * x - c) / b  # Solve the equation for y

    plt.plot(x, y)  # Plot the line
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph of {}x + {}y + {} = 0'.format(a, b, c))
    plt.grid(True)
    plt.show()

import matplotlib.pyplot as plt
import numpy as np
def devint(array):
    # Calculate the derivative
    derivative = np.gradient(array)
    
    # Calculate the integral
    integral = np.cumsum(array)
    
    # Plot the input array
    plt.subplot(1, 3, 1)
    plt.plot(array, color='blue', label='Input Array')
    plt.legend(loc='best')
    plt.title('Input Array')
    
    # Plot the derivative
    plt.subplot(1, 3, 2)
    plt.plot(derivative, color='red', label='Derivative')
    plt.legend(loc='best')
    plt.title('Derivative')
    
    # Plot the integral
    plt.subplot(1, 3, 3)
    plt.plot(integral, color='green', label='Integral')
    plt.legend(loc='best')
    plt.title('Integral')
    
    # Adjust the layout and display the plot
    plt.tight_layout()
    plt.show()