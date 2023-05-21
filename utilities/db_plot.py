import numpy as np
from matplotlib import pyplot as plt

_all_ = ["plot_boundaries", "contour_boundaries"]


def plot_boundaries(W, B, ax):
    # Plot boundaries
    gen_boundaries(W, B, ax)

    # Set the x and y limits of the plot
    ax.axis("equal")
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)

    # Origin axis
    ax.axhline(y=0, lw=2, color='k', alpha=0.5, zorder=0)
    ax.axvline(x=0, lw=2, color='k', alpha=0.5, zorder=0)

    # Plot options
    ax.set_xlabel(r"$p_1$")
    ax.set_ylabel(r"$p_2$")

    # Set grid and legend on
    plt.grid(True)
    plt.legend()


def gen_boundaries(W, B, ax):
    # Print Boundaries
    pdip = np.linspace(-5, 5, 1000)

    for index, (W_row, B_row) in enumerate(zip(W, B)):
        if not W_row[1]:
            p = (-B_row / W_row[0])
            ax.axvline(x=p, zorder=5, color="yellow", label=f"DB n°{index+1}")
        else:
            p = (1 / W_row[1]) * (-W_row[0] * pdip - B_row)
            ax.plot(pdip, p, label=f"DB n°{index+1}", zorder=5)


def contour_boundaries(X, Y, Z, ax):
    # Create a contour plot
    cs = plt.contour(X, Y, Z, levels=[-1, 1], colors=['blue', 'red'])

    # create a heatmap of the function values
    plt.imshow(Z, origin='lower', extent=[-3, 3, -3, 3], cmap='coolwarm')

    # create a custom legend
    legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label='-1', markerfacecolor='blue', markersize=10),
                       plt.Line2D([0], [0], marker='o', color='w', label='1', markerfacecolor='red', markersize=10)]
    plt.legend(handles=legend_elements)

    # Set the x and y limits of the plot
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)

    # Origin axis
    ax.axhline(y=0, lw=2, color='k', alpha=0.5, zorder=0)
    ax.axvline(x=0, lw=2, color='k', alpha=0.5, zorder=0)

    # Plot options
    ax.set_xlabel(r"$p_1$")
    ax.set_ylabel(r"$p_2$")

    # Set grid on
    plt.grid(True)
