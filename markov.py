import random

# Define the states of the Markov chain
states = ["A", "B", "C"]

# Define the transition probabilities as a dictionary of dictionaries
transition_probabilities = {
    "A": {"A": 0.5, "B": 0.3, "C": 0.2},
    "B": {"A": 0.2, "B": 0.4, "C": 0.4},
    "C": {"A": 0.1, "B": 0.2, "C": 0.7}
}

# Initialize the current state
current_state = random.choice(states)

# Define the number of steps to simulate
num_steps = 10

# Simulate the Markov chain
for _ in range(num_steps):
    print("Current state:", current_state)

    # Use the transition probabilities to determine the next state
    next_state = random.choices(
        population=states,
        weights=[transition_probabilities[current_state][state] for state in states]
    )[0]

    current_state = next_state
