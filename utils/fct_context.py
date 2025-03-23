from contextlib import contextmanager
import matplotlib.pyplot as plt

@contextmanager
def plot(title='xxx', x_label='xxx', y_label='xxx'):
    # Start the timer
    plt.rcParams["figure.figsize"] = [15,10]
    plt.rcParams['font.size'] = '12'

    # PLOT
    yield

    # End the timer
    plt.minorticks_on() #Grille mineure
    plt.grid(True, which='both') 
    plt.grid(alpha=0.7,which='both', linestyle='--')

    # LEGEND
    # plt.legend(bbox_to_anchor=(1.05, 0.5, 0.3, 0.2), loc='upper left')
    plt.legend(loc = 'best',ncol = 1)

    plt.title(title, fontweight="bold")

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()



@contextmanager
def temp_file():
    # Start the timer
    import os

    path_cwd = os.getcwd()
    path_temp_dir = "temp_dir"

    if not os.path.exists(path_temp_dir):
        os.makedirs(path_temp_dir)

    os.chdir(path_temp_dir)

    # PLOT
    yield

    # End the timer
    os.chdir(path_cwd)
    os.rmdir(path_temp_dir)
