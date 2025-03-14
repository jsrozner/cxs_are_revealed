from typing import List, Optional, Tuple

import torch
from matplotlib import pyplot as plt
from matplotlib.figure import Figure


def plot_heatmap(tensor: torch.Tensor,
                 xlabels: List[str],
                 ylabels: Optional[List[str]],
                 cmap: str = 'Blues',
                 title=None,
                 add_colorbar=True,
                 fig_size: Optional[Tuple[int, int]] = None,
                 return_fig = False,
                 xlabel_rotation=90
                 ) -> Optional[Figure]:
    """
    Plots a heatmap for a 2D tensor.

    Args:
        ylabels: If given, will also plot on the right hand side
        tensor (torch.Tensor): The 2D tensor to be plotted.
        cmap (str): The color map to use for the heatmap.
    """
    # todo: check this (added for hhi score alts)
    # tensor.fill_diagonal_(0)
    if tensor.dim() != 2:
        raise ValueError("Input tensor must be 2-dimensional.")

    # Convert tensor to NumPy array
    tensor_np = tensor.numpy()

    # plt.xlabel("Column Index")
    # plt.ylabel("Row Index")
    # plt.xticks(ticks=range(tensor.shape[1]), labels=xlabels, rotation=45,
    #            ha='right')
    # plt.yticks(ticks=range(tensor.shape[0]), labels=ylabels)
    # plt.yticks(ticks=range(tensor.shape[0]), labels=xlabels, ha='right')
    # Set primary (left) y-axis labels
    if fig_size:
        fig, ax = plt.subplots(figsize=fig_size)
    else:
        fig, ax = plt.subplots(figsize=(3,3))
    plt.imshow(tensor_np, cmap=cmap, aspect='auto')
    if add_colorbar:
        plt.colorbar()  # Adds a color bar to the side
    if title:
        plt.title(title)

    ax.set_yticks(range(tensor.shape[0]))
    ax.set_xticks(range(tensor.shape[1]))

    if xlabels is not None:
        ax.set_yticklabels(xlabels)
        if xlabel_rotation == 90:
            ax.set_xticklabels(xlabels, rotation=xlabel_rotation, ha='center')
        else:
            ax.set_xticklabels(xlabels, rotation=xlabel_rotation, ha='right', rotation_mode='anchor')

    try:
        # todo: not sure why this is having an issue
        if ylabels is not None:
            # Create secondary y-axis for the right side with different labels
            ax_right = ax.twinx()  # Create a twin y-axis sharing the same x-axis
            ax_right.set_ylim(ax.get_ylim())  # Match the limits of the left axis
            # Set the right y-axis labels and match the tick positions
            ax_right.set_yticks(ax.get_yticks())
            ax_right.set_yticks(range(tensor.shape[0]))

            ax_right.set_yticklabels(ylabels)
            ax_right.yaxis.set_tick_params(right=True, pad=5)
    except Exception as e:
        print(e)

    # add annotations on top
    # y_limits = ax.get_ylim()
    # x_limits = ax.get_xlim()
    # x_size = x_limits[1] - x_limits[0]
    # y_size = y_limits[1] - y_limits[0]
    # inc = x_size/len(xlabels)
    # inc_y = y_size/len(xlabels)
    # # these seem to be off by one
    # y_start1 = y_limits[0] + 9* inc_y
    # y_start2 = y_limits[0] + 5 * inc_y
    # # rect1 = patches.Rectangle((x_start, y_start1), width=increments, height=increments, linewidth=1, edgecolor='red', facecolor='none')
    # # rect2 = patches.Rectangle((x_start, y_start2), width=increments, height=increments, linewidth=1, edgecolor='red', facecolor='none')
    # rect1 = patches.Rectangle((x_limits[0] + 2*inc, y_start1), width=inc, height=inc, linewidth=2, edgecolor='red', facecolor='none')
    # rect2 = patches.Rectangle((x_limits[0] + 2*inc, y_start2), width=inc, height=inc, linewidth=2, edgecolor='red', facecolor='none')
    # ax.add_patch(rect1)
    # ax.add_patch(rect2)
    #
    # Move the right-side ticks inward to avoid overlap
    if not return_fig:
        plt.show()
    else:
        return fig
