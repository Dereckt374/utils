import matplotlib.pyplot as plt

def addlabels(x,y,x_pos=0.1,y_pos=0.1, round_ = 2):
    """
    permet d'ajouter les valeurs des datas affichées dans le plot
    """
    for i in range(len(x)):
        scalex=(max(x)-min(x))/2
        scaley=(max(y)-min(y))/2
        plt.text(x[i]+x_pos*scalex, round(y[i]+y_pos*scaley,1),round(y[i],round_), wrap=True, bbox=dict(facecolor='white',alpha=0.8))
        # plt.text(x[i]+prop*scalex, round(y[i]+prop*scaley,1),round(y[i],1),wrap=True)


        