"""
CODE WRITTEN BY Paul-Emile NEU
Purpose : Predict a trajectory with the help of kalman filters and markov model
Return : A set of chart to plot the true trajectory and the predicted one


HOW IT WORKS : 
This program use the default kalman filters to predict a trajectory. Because kalman is good for prediction but may be not as accurate as wanted
and can create irremediable errors we have added markov properties to kalman's calculations making it less prone to errors based solely on measurement, transitions and the previous state when predicting the next state. This algorithm therefore acts as a discrete variable Kalman filter, adding the fact that the probability of being in a place at a time T depends only on the previous state.

The limitations of this algorithm will arise when the parameters passed as input are not very precise, too high to cause correct calculations or too far from reality. The strength of the model relies on the precision of the input parameters (the transition matrix, the observation matrix, the initial state and the measurement noises). The more these parameters are precise and adapted to the statistical model of human movement, the more accurate and precise the predictions will be.
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
        self.state = initial_state 
        self.transition_matrix = transition_matrix 
        self.observation_matrix = observation_matrix
        self.process_noise_cov = process_noise_cov
        self.observation_noise_cov = observation_noise_cov
        
        self.predicted_state = initial_state
        self.predicted_covariance = np.zeros_like(self.transition_matrix)

    def predict(self):
        """
            Predict a trajectory based on the transition matrix and the current state

            PARAM : 
                self : the context
            
            RETURN : 
                the predicted state as a matrix
        """
        # Predict the next state using the transition matrix and current state
        self.predicted_state = np.dot(self.transition_matrix, self.state)
        
        # Predict the covariance of the next state using the transition matrix, current covariance, and process noise covariance
        self.predicted_covariance = np.dot(self.transition_matrix, np.dot(self.predicted_covariance, self.transition_matrix.T)) + self.process_noise_cov
            
        # Return the predicted state
        return self.predicted_state

    def update(self, observation):
        """
            Update the state based on the observation and the previous one

            PARAM : 
                self : the context
                observation (array) : the measurement matrix
            
            RETURN : 
                the new state
        """
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
        """
            Generate a trajectory based on step number and measurements

            PARAM : 
                self : the context
                num_step (int) : the number of steps in the trajectory
            
            RETURN : 
                the trajectory as an array (numpy)
        """
        # Initialize the trajectory with the current state
        trajectory = [self.state]
        
        # Iterate over the specified number of steps
        for _ in range(num_steps):
            # Predict the next state
            self.predict()
            
            # Generate an observation by taking a linear combination of the predicted state and adding observation noise
            observation = np.dot(self.observation_matrix, self.predicted_state) + np.random.multivariate_normal(np.zeros(self.observation_matrix.shape[0]), self.observation_noise_cov)
            
            # Update the state estimate based on the observation
            self.update(observation)
            
            # Add the updated state estimate to the trajectory
            trajectory.append(self.state)
        
        # Return the trajectory as a numpy array
        return np.array(trajectory)


# Define the initial state of the system as a 4-element vector
initial_state = np.array([0, 0, 0, 0])

# Define the transition matrix for the Markov model
transition_matrix = np.array([
    [1, 1, 0, 0],   # The first and second elements of the state are updated based on the previous state
    [0, 1, 0, 1],   # The second and fourth elements of the state are updated based on the previous state
    [0, 0, 1, 0],   # The third element of the state is unchanged
    [0, 0, 0, 1]    # The fourth element of the state is unchanged
])

# Define the observation matrix for the Kalman filter
observation_matrix = np.array([
    [1, 1 , 1, 0],  # elements of the observation are a linear combination of the state
    [0, 1, 1, 0]    
])

# Define the covariance of the process noise, which models random disturbances in the trajectory
process_noise_cov = 0.01 * np.eye(4)

# Define the covariance of the observation noise, which models measurement errors
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
    """
       Update the true trajctory plot in real time (callback)

        PARAM : 
            frame (int) : the current frame
        
        RETURN : 
            updated dataset
    """
    global index_1, index_2
    if(index_1 < len(true_trajectory[:,0])):
        append_x_true.append(true_trajectory[index_1,0])
        index_1 +=1

    if(index_2 < len(true_trajectory[:,1])):
        append_y_true.append(true_trajectory[index_2,1])
        index_2 +=1
 
    line1.set_data(append_x_true, append_y_true) 

    return line1,

def update_predicted_plot(frame):
    """
       Update the predicted trajctory plot in real time (callback)

        PARAM : 
            frame (int) : the current frame
        
        RETURN : 
            updated dataset
    """
    global index_1, index_2

    if(index_1 < len(true_trajectory[:,0])):
        append_x_predicted.append(true_trajectory[index_1,0])
        index_1 +=1

    if(index_2 < len(true_trajectory[:,1])):
        append_y_predicted.append(true_trajectory[index_2,1])
        index_2 +=1
 
    line2.set_data(append_x_predicted, append_y_predicted) 

    return line2,


#callback for plotting animations
animation_true = FuncAnimation(fig, update_true_plot, blit=True,interval=100)
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
