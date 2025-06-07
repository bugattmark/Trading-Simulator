import numpy as np
import time

def pricestream(S0,mu,sigma,dt):
        W = np.random.standard_normal()
        W = np.cumsum(W) * np.sqrt(dt)
        new_price = round(S0*np.exp((mu-0.5*sigma**2)*dt+sigma*W[-1]),2)
        new_price = "{:.2f}".format(new_price)
        return float(new_price)