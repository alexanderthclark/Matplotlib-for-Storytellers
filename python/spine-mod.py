import matplotlib.pyplot as plt

plt.gca().spines['left'].set_position('zero')
plt.gca().spines['bottom'].set_position('zero')

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)