"""
CODE WRITTEN BY Paul-Emile NEU
Purpose : Predict a trajectory with the help of kalman filters and markov model
Return : A set of chart to plot the true trajectory and the predicted one
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class KalmanMarkovPredictor:
    """
    Class that process the trajectory prediction with kalman and markov 
    The main algorithm is the kalman one but with the help of some markov property (observation and state)
    we improve the prediction. 

    The prediction is only based on the previous state and not the whole state. 
    This algorithm acts like a discret kalman filter for prediction
    """
    def __init__(self, initial_state, transition_matrix, observation_matrix, process_noise_cov, observation_noise_cov):
        """
        Class constructor to set all useful variable
        """
        self.state = initial_state #the current state
        self.transition_matrix = transition_matrix #
        self.observation_matrix = observation_matrix
        self.process_noise_cov = process_noise_cov
        self.observation_noise_cov = observation_noise_cov
        
        self.predicted_state = initial_state
        self.predicted_covariance = np.zeros_like(self.transition_matrix)

    def predict(self):
        self.predicted_state = np.dot(self.transition_matrix, self.state)
        self.predicted_covariance = np.dot(self.transition_matrix, np.dot(self.predicted_covariance, self.transition_matrix.T)) + self.process_noise_cov
        
        return self.predicted_state

    def update(self, observation):

        #difference between observation and predicted observation
        computed_innovation = observation - np.dot(self.observation_matrix, self.predicted_state)

        #calculate the uncertainty in the difference between the predicted state and the observation
        innovation_covariance = np.dot(self.observation_matrix, np.dot(self.predicted_covariance, self.observation_matrix.T)) + self.observation_noise_cov

        #update the predicted state with the 'difference between the predicted state and the observation
        kalman_gain = np.dot(self.predicted_covariance, np.dot(self.observation_matrix.T, np.linalg.inv(innovation_covariance)))
        
        #the new state is updated with the two values calculated above (gain and computed_innovation)
        self.state = self.predicted_state + np.dot(kalman_gain, computed_innovation)
        self.predicted_covariance = np.dot(np.eye(self.predicted_covariance.shape[0]) - np.dot(kalman_gain, self.observation_matrix), self.predicted_covariance)
        
        return self.state

    def generate_trajectory(self, num_steps):
        trajectory = [self.state]
        
        for _ in range(num_steps):
            self.predict()
            observation = np.dot(self.observation_matrix, self.predicted_state) + np.random.multivariate_normal(np.zeros(self.observation_matrix.shape[0]), self.observation_noise_cov)
            self.update(observation)
            trajectory.append(self.state)
            
        return np.array(trajectory)

# Define the parameters for the Kalman filter and Markov model
initial_state = np.array([0, 0, 0, 0])
transition_matrix = np.array([
    [1, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])
observation_matrix = np.array([
    [1, 1 , 1, 0],
    [0, 1, 1, 0]
])
process_noise_cov = 0.01 * np.eye(4) #random disturbance in trajactory
observation_noise_cov = 0.2 * np.eye(2)

# Generate a predict a trajectory
predictor = KalmanMarkovPredictor(initial_state, transition_matrix, observation_matrix, process_noise_cov, observation_noise_cov)
trajectory = predictor.generate_trajectory(100)

# Generate the true trajectory
true_trajectory = np.dot(observation_matrix, trajectory.T).T #.T for Transpose

# Plot the results
fig = plt.figure(800)
ax1 = plt.subplot(2, 2, 1)
ax2 = plt.subplot(2, 2, 2)
ax3 = plt.subplot(2, 1, 2)
append_x_true = []
append_y_true = []
append_x_predicted = []
append_y_predicted = []
copy_x_true = []
copy_y_true = []
line1, = ax1.plot([], [],color="blue")
# line3, = ax2.plot([], [],color="blue")
line2, = ax2.plot([], [],color="orange")
index_1 = 0
index_2 = 0
x_lim = (min(true_trajectory[:,0]), max(true_trajectory[:,0]))
y_lim = (min(true_trajectory[:,1]), max(true_trajectory[:,1]))

x_lim_pred = (min(trajectory[:,0]), max(trajectory[:,0]))
y_lim_pred = (min(trajectory[:,1]), max(trajectory[:,1]))
         

def update_true_plot(frame):
    global index_1, index_2
    if(index_1 < len(true_trajectory[:,0])):
        append_x_true.append(true_trajectory[index_1,0])
        index_1 +=1

    if(index_2 < len(true_trajectory[:,1])):
        append_y_true.append(true_trajectory[index_2,1])
        index_2 +=1
 
    line1.set_data(append_x_true, append_y_true) 

    return line1,

# def copy_true_plot(frame):
#     global index_1, index_2
#     if(index_1 < len(true_trajectory[:,0])):
#         copy_x_true.append(true_trajectory[index_1,0])
#         index_1 +=1

#     if(index_2 < len(true_trajectory[:,1])):
#         copy_y_true.append(true_trajectory[index_2,1])
#         index_2 +=1
 
#     line3.set_data(copy_x_true, copy_y_true) 

#     return line3,

def update_predicted_plot(frame):
    global index_1, index_2

    if(index_1 < len(true_trajectory[:,0])):
        append_x_predicted.append(true_trajectory[index_1,0])
        index_1 +=1

    if(index_2 < len(true_trajectory[:,1])):
        append_y_predicted.append(true_trajectory[index_2,1])
        index_2 +=1
 
    line2.set_data(append_x_predicted, append_y_predicted) 

    return line2,


animation_true = FuncAnimation(fig, update_true_plot, blit=True,interval=600)
# animation_true_copy = FuncAnimation(fig, copy_true_plot, blit=True,interval=100)
animation_predicted = FuncAnimation(fig, update_predicted_plot, blit=True,interval=100)


# assign the FuncAnimation instances to the corresponding subplots
ax1.set_xlim(x_lim)
ax1.set_ylim(y_lim)
ax1.set_title('True trajectory')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.grid(True)
ax1.set_aspect('equal')
ax1.set_aspect('auto')
ax1.legend(['True trajectory'])
ax1.set_aspect('auto')

ax2.set_xlim(x_lim_pred)
ax2.set_ylim(y_lim_pred)
ax2.set_title('Predicted trajectory')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.grid(True)
ax2.set_aspect('equal')
ax2.set_aspect('auto')
ax2.legend(['Predicted trajectory'])
ax2.set_aspect('auto')


#plot both
ax3.plot(true_trajectory[:, 0], true_trajectory[:, 1], label='true')
ax3.plot(trajectory[:, 0], trajectory[:, 1], label='predicted',color="orange")
ax3.legend()


# #plot 1
# plt.subplot(2, 2, 1)
# plt.plot(true_trajectory[:, 0], true_trajectory[:, 1], label='true')
# plt.legend()

# #plot 2
# plt.subplot(2, 2, 2)
# plt.plot(trajectory[:, 0], trajectory[:, 1], label='predicted',color="orange")
# plt.legend()

# #plot both
# plt.subplot(2, 1, 2)
# plt.plot(true_trajectory[:, 0], true_trajectory[:, 1], label='true')
# plt.plot(trajectory[:, 0], trajectory[:, 1], label='predicted',color="orange")
# plt.legend()
plt.show()
