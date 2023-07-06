import gym
from gym import spaces
import numpy as np

class CloudEnvironment(gym.Env):
    def __init__(self):
        # Define the action space and observation space
        self.action_space = spaces.Discrete(2)  # Example: two possible actions (increase or decrease resources)
        self.observation_space = spaces.Box(low=0, high=1, shape=(4,))  # Example: four observation features

        # Define other necessary variables and parameters for your environment
        self.current_performance = 0.0  # Current performance metric
        self.current_cost = 0.0  # Current cost metric
        self.max_resources = 10  # Maximum available resources
        self.min_resources = 1  # Minimum available resources
        self.current_resources = 5  # Initial available resources

    def step(self, action):
        # Perform the selected action and update the environment
        if action == 0:  # Decrease resources
            self.current_resources -= 1
        elif action == 1:  # Increase resources
            self.current_resources += 1

        # Update performance and cost metrics based on the current resource allocation
        self.current_performance = self._calculate_performance()
        self.current_cost = self._calculate_cost()

        # Define the reward based on the cost-to-performance ratio
        reward = self.current_performance / self.current_cost

        # Print the current state and reward
        print("State:", [self.current_performance, self.current_cost, self.current_resources])
        print("Reward:", reward)

        # Example: Determine if the episode is finished based on a condition (e.g., reaching a performance threshold)
        done = False
        if self.current_performance >= 0.9:  # Example: Finishing condition if performance reaches 0.9
            done = True

        # Return the updated state, reward, done flag, and additional information (optional)
        return np.array([self.current_performance, self.current_cost, self.current_resources]), reward, done, {}

    def reset(self):
        # Reset the environment to the initial state
        self.current_performance = 0.0
        self.current_cost = 0.0
        self.current_resources = 5

        # Print the initial state
        print("Initial State:", [self.current_performance, self.current_cost, self.current_resources])

        # Return the initial state as an observation
        return np.array([self.current_performance, self.current_cost, self.current_resources])

    def _calculate_performance(self):
        # Implement a function to calculate the performance metric based on the current resource allocation
        # Example: Calculate performance based on a formula or simulation

        performance = 1 - (self.current_resources - self.min_resources) / (self.max_resources - self.min_resources)

        # Print the calculated performance
        print("Performance:", performance)

        return performance

    def _calculate_cost(self):
        # Implement a function to calculate the cost metric based on the current resource allocation
        # Example: Calculate cost based on a formula or simulation

        cost = self.current_resources / self.max_resources

        # Print the calculated cost
        print("Cost:", cost)

        return cost


# Create an instance of the environment
env = CloudEnvironment()

# Reset the environment
initial_state = env.reset()

# Perform some steps in the environment
for _ in range(5):
    action = env.action_space.sample()  # Random action for demonstration
    state, reward, done, _ = env.step(action)

    if done:
        break

# Print final results
print("Final Performance Metric:", env._calculate_performance())
print("Final Cost Metric:", env._calculate_cost())
