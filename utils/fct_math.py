from statsmodels.tsa.stattools import adfuller
import numpy as np
import pandas as pd
from scipy import stats


def Rsquared(Y,Yreg):
    """
    calcul le coefficient de determination R² entre les séries Y et Yreg
    """
    correlation_matrix = np.corrcoef(Y, Yreg)
    correlation_xy = correlation_matrix[0,1]
    r_squared = correlation_xy**2
    return(r_squared)

def regrpoly(x,y,d=1,R2=False):
    """
    retourne un object polynome correspondant à la regression polynomiale de degrès d des séries y, x 
    """
    f=np.poly1d(np.polyfit(x, y, d))
    if R2==True:
        Yreg=[]
        for i in x:
            Yreg.append(f(i))
        print("Coef. de determination R²=",round(Rsquared(y,Yreg),3))
    return(f)

def RacineP2nd(a,b,c):
    """
    racine d'un polynome de 2nd degrès
    """
    delta=b**2-4*a*c
    # print("delta = ",delta)
    if delta>0 :
        r=[((-b+np.sqrt(delta))/(2*a)),((-b-np.sqrt(delta))/(2*a))]
        return r
    elif delta ==0 : 
        r=-b/(2*a)
        return r
    else : return(False)    



def racine(poly,evalu=0):
    """
    retounre les racines d'un polynomes, avec second membre ou sans
    """
    list1 = poly.coef
    list2 = list1.copy()
    p = np.poly1d(list2)
    p[0]=p[0]-evalu
    return(p.r)

def OffsetPoly(poly,offset=0):
    """
    le polynome avec un offset (offset de la constante) différent
    """
    poly[0]=poly[0]-offset
    return(poly)

def RegMultiple(X,Y):
    """
    retourne une regression linéaire multiple, X variables dépendantes, Y variables indépendantes (sorties)
    retourne en premier les paramètres de chaque variables dans X (chaque ligne), puis la constante
    regression de degrès 1, si suppérieur : augmenter les degrès dans X
    """
    X = np.transpose(X) # transpose so input vectors
    X = np.c_[X, np.ones(X.shape[0])]  # add bias term
    linreg = np.linalg.lstsq(X, Y, rcond=None)[0]
    return(linreg)


def Integtrapeze( f, a, b, n=1000):
    h = ( b - a ) / n
    s = 0.5 * ( f( a ) + f( b ) ) + \
        sum( map( f, ( a + h * i for i in range( 1, n ) ) ) )
    return s * h

def Intergrptapt(x,y):
    total=0
    for i in range(0,len(x)-1):
        s=((y[i]+y[i+1])*(x[i+1]-x[i]))/2
        total=total+s
    return(total)

def sinusoidal(t, A, period, phi, offset):
    return A * np.sin((2* np.pi)/period * t + phi) + offset

def premier_ordre(t, K, e0, tau):
    return K * (1-np.exp(-t/tau)) + e0


def ajouter_bruit(fonction, x, amplitude_bruit, seed=None):
    """
    Ajoute du bruit gaussien à une fonction.

    Parameters:
    - fonction: fonction qui prend un tableau numpy x et retourne un tableau numpy des valeurs.
    - x: tableau numpy des valeurs d'entrée pour la fonction.
    - amplitude_bruit: amplitude du bruit gaussien à ajouter.
    - seed: (optionnel) valeur pour initialiser le générateur de nombres aléatoires.

    Returns:
    - Tableau numpy des valeurs de la fonction avec bruit ajouté.
    """
    if seed is not None:
        np.random.seed(seed)  # Pour la reproductibilité

    # Calculer les valeurs de la fonction
    valeurs = fonction(x)

    # Générer du bruit gaussien
    bruit = amplitude_bruit * np.random.randn(len(x))

    # Ajouter le bruit aux valeurs de la fonction
    valeurs_bruitees = valeurs + bruit

    return valeurs_bruitees



def len_reg(x,y):
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    return(slope, intercept)



def reg_plot(x,y):
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    equation = f'y = {slope:.5f} x + {intercept:.2f} R² : {r_value:.2f}'
    print(equation)
    data_x = [min(x), max(x)]
    data_y = [(slope * data_x[0] + intercept ),(slope * data_x[1] + intercept ) ]
    return([data_x, data_y])

def give_x_for_given_y(a, b, y=10):
    return((y-b)/a)

def simulation_données_orbite(temps, amplitude1=100, amplitude2=50, periode1=1.5, periode2=3*30*24, tendance=1500, bruit_amplitude=10):
    """
    temps: tableau de temps en heures sur un an (par ex. np.linspace(0, 365*24, nombre_de_points))
    amplitude1: amplitude du premier sinus
    amplitude2: amplitude du second sinus
    periode1: période du premier sinus (en heures)
    periode2: période du second sinus (en heures)
    tendance: valeur initiale à t=0
    bruit_amplitude: amplitude du bruit aléatoire
    """
    # Sinus à la première période (paramétrable)
    sinus_1 = amplitude1 * np.sin(2 * np.pi * temps / periode1)
    
    # Sinus à la deuxième période (paramétrable)
    sinus_2 = amplitude2 * np.sin(2 * np.pi * temps / periode2)
    
    # Tendance croissante sur un an (x2 en 1 an)
    tendance_croissante = tendance * (1 + temps / (365 * 24))
    
    # Bruit aléatoire gaussien
    bruit = bruit_amplitude * np.random.randn(len(temps))
    
    # Signal total
    signal = sinus_1 + sinus_2 + tendance_croissante + bruit
    
    return signal


def analyse_fourier(signal, sampling_rate):
    """
    Effectue une analyse de Fourier sur le signal.
    
    :param signal: Le signal d'entrée (array).
    :param sampling_rate: La fréquence d'échantillonnage (Hz).
    :return: fréquences, amplitudes
    """
    # Nombre de points dans le signal
    N = len(signal)
    
    # Appliquer la transformée de Fourier
    fft_values = np.fft.fft(signal)
    
    # Calculer les fréquences correspondantes
    freq = np.fft.fftfreq(N, d=1/sampling_rate)
    
    # Calculer les amplitudes
    amplitudes = np.abs(fft_values) / N  # Normalisation
    
    return freq[:N//2], amplitudes[:N//2]  # Retourner uniquement les fréquences positives
    df_fft = pd.DataFrame(analyse_fourier(signal, sampling_rate), index=['frequence', 'amplitude']).T.set_index('frequence')
    
# Appliquer l'analyse de Fourier
# df_fft = pd.DataFrame(analyse_fourier(signal, sampling_rate), index=['frequence', 'amplitude']).T.set_index('frequence')



def adf_test(timeseries):
    print ('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    if dfoutput['p-value'] <= 0.05:
        print("The series is likely stationary")
    else:
        print("The series is likely non-stationary")
    return(dfoutput)
