import numpy as np

def compute_advantage(states: list, rewards: list, V: list, gamma: float) -> np.ndarray:
    """
    Returns the advantages as a NumPy array.
    """
    # Write code here
    n = len(rewards)
    returns = np.zeros(n)
    adv = np.zeros(n)
    G = 0
    for t in reversed(range(n)):
        G = rewards[t] + gamma * G
        returns[t] = G
    for t in range(n):
        adv[t] = returns[t] - V[states[t]]
    return adv

    
    pass