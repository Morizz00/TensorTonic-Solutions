import numpy as np

def bootstrap_mean(x: list, n_bootstrap: int = 1000, ci: float = 0.95, seed: int = 0) -> dict:
    """
    Returns a dictionary with bootstrap_mean, lower, and upper.
    """
    # Write code here
    x = np.array(x,dtype=float)
    bs_mean = []
    N = len(x)
    rng = np.random.default_rng(seed)
    for _ in range(n_bootstrap):
        samp = rng.choice(x,size=N,replace=True)
        bs_mean.append(np.mean(samp))
    bootstrap_mean = float(np.mean(bs_mean))
    alpha = (1-ci)/2
    lower = float(np.percentile(bs_mean,alpha *100))
    upper = float(np.percentile(bs_mean,(1-alpha) * 100))
    return {
        "bootstrap_mean" : bootstrap_mean,
        "lower" : lower,
        "upper" : upper
    }
    
    pass