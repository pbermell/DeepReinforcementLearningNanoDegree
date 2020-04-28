import gym
import random
import torch
import numpy as np
from collections import deque
import matplotlib.pyplot as plt


env = gym.make('LunarLander-v2')
# env.seed(0)
# print('State shape: ', env.observation_space.shape)
# print('Number of actions: ', env.action_space.n)

# # !python -m pip install pyvirtualdisplay
# from pyvirtualdisplay import Display
# display = Display(visible=0, size=(1400, 900))
# display.start()
#
# is_ipython = 'inline' in plt.get_backend()
# if is_ipython:
#     from IPython import display
#
# plt.ion()