import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from scipy import stats

def plot_t_distribution(t_value, df, canvas_frame):
    x = np.linspace(-4, 4, 1000)
    y = stats.t.pdf(x, df)

    fig, ax = plt.subplots()
    ax.plot(x, y, 'b-', label=f't-distribution df={df}')
    ax.fill_between(x, y, 0, where=(x >= t_value), color='red', alpha=0.5)
    ax.fill_between(x, y, 0, where=(x <= -t_value), color='red', alpha=0.5)
    ax.axvline(t_value, color='red', linestyle='dashed', linewidth=2, label=f't-value = {t_value:.4f}')
    ax.axvline(-t_value, color='red', linestyle='dashed', linewidth=2)
    ax.legend()
    ax.set_title('t-distribution with Highlighted t-value')

    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()