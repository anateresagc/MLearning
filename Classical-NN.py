#### Classical NN Exercises


import numpy as np
import pickle
import matplotlib.pyplot as plt
import os
import mpl_toolkits.axisartist as axisartist

#directory = "IMAGES_FOR_DOCUMENT"
#os.makedirs(directory, exist_ok=True) #\PythonWork\results
#os.chdir(directory) 

#filename = "state_preparation.pdf"



def plot(w, w_new):
    menus_one_points_x = [1,4,6]
    menus_one_points_y = [4,-3,2]
    plus_one_points_x = [0,2,4,5]
    plus_one_points_y = [-2,1,-4,6] 

    plt.scatter(menus_one_points_x, menus_one_points_y, color="blue", label = "-1")
    plt.scatter(plus_one_points_x, plus_one_points_y, color="red", marker='+', label = "+1" )

    xx = np.linspace(-1,7)
    yy = (w[0]-w[1]*xx)/(w[2])
    yy_new = (w_new[0]-w_new[1]*xx)/(w_new[2])
    plt.grid(True, color='lightgrey', linestyle='--', linewidth=0.5, zorder=-1)  # Color claro y detrás
    plt.gca().set_axisbelow(True)  # Asegura que el grid esté detrás de los puntos
    plt.plot(xx, yy_new, color="black", label = "Final decision bounday")
    plt.plot(xx, yy, color="gray", label = "Initial decision bounday")
    plt.xlabel(r"$x_1$")                   
    plt.ylabel(r"$x_2$")
    plt.legend()
    plt.show()

w = [-7,2,1]
plot(w,w)

x1 = [0,1,2,4,4,5,6]
x2= [-2,4,1,-4,-3,6,2]
y = [1,-1,1,1,-1,1,-1]
alpha = 0.3
max = 20

def gradient_descent_perceptron(alpha, x1, x2, y, w, max):
    print("gradient descent in working")
    w_1 = []
    w_2 = []
    #Añadimos los wieghts iniciales.
    w_1.append(w[1])
    w_2.append(w[2])

    for i in range(0, len(y)):
        print("POINT", i+1)
        # Bucle para q me repita el calculo de los weights si estos no son los correctos
        for k in range(1,max):
            theta = w[0]
            w_new = [theta, 0,0]
            sum = w[1] * x1[i] + w[2] * x2[i]
            if sum < theta:
                y_algorithm = -1
            else:
                y_algorithm = 1
    
            epsilon = y[i]-y_algorithm

            if epsilon != 0:
                for j in range(1, len(w)):
                    w_new[j] = round(w[j] + alpha*epsilon,2)
                print("incorrect, epsilon =", epsilon, ". New weights:", w_new)
                w = w_new
                w_1.append(w[1])
                w_2.append(w[2])
                continue

            else:
                print("correct, epsilon =", epsilon, "Weights: ", w)
                w_1.append(w[1])
                w_2.append(w[2])
                break

    return(w, w_1, w_2)

w_new, w_1, w_2= gradient_descent_perceptron(alpha, x1, x2, y, w, max)

iteration= np.arange(1, len(w_1)+1)

plt.grid(True, color='lightgrey', linestyle='--', linewidth=0.5, zorder=-1)  # Color claro y detrás
plt.scatter(iteration, w_1, label=r"$\omega_1$")
plt.scatter(iteration, w_2, label=r"$\omega_2$")
plt.xlabel(r"Iteration")                   
plt.ylabel(r"Weights values")
plt.legend()
plt.show()

plot(w, w_new)