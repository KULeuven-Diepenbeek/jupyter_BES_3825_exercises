import numpy as np
from scipy.optimize import curve_fit


def zwevendGemiddelde(xs,n):
    ''' geef het zwevend gemiddelde terug uit xs met een periode van n

    :param xs ([double]): de lijst getallen waarvan je het zwevend gemiddelde wil
    :param n (int): de periode voor het zwevend gemiddelde, bv. 7
    :return ([float]): De lijst met het zwevend gemiddelde met de opgegeven periode.
                        De lijst die terug gegeven wordt, is even lang als in de invoerlijst xs
                        voor de eerste n-1 getallen wordt het gewogen gemiddelde van het begin tot het getal gegeven
    '''
    xFilt = list()
    xFilt.append(xs[0])

    for i in range(1, n):
        xFilt.append(np.mean(xs[0:i+1]))

    for i in range(n, len(xs)):
        xFilt.append(np.mean(xs[i-n:i]))
    return xFilt

def fitVeelterm(xs,ys, graad):
    """ genereert functie die een veelterm-curve fit is in de opgegeven graad

    :param xs ([float]): lijst met x-waarden
    :param ys ([float]): lijst met y-waarden
    :param graad (int): de gewenste graad van de veelterm
    :return (functie float -> float): veeltermfunctie die de curve fit is van xs op ys
    """
    z = np.polyfit(xs,ys, graad)
    return np.poly1d(z)

def fitExp(xs, ys):
    """ genereert functie die een exponentiële curve fit is

    :param xs ([float]): lijst met x-waarden
    :param ys ([float]): lijst met y-waarden
    :return (functie float -> float): exponentiële functie die de curve fit is van xs op ys
    """

    # bron: https://towardsdatascience.com/basic-curve-fitting-of-scientific-data-with-python-9592244a2509
    def exponential(x, a, b):
        return a * np.exp(b * x)

    pars, cov = curve_fit(f=exponential, xdata=xs, ydata=ys, p0=[0, 0], bounds=(-np.inf, np.inf))

    return lambda x : pars[0] * np.exp(pars[1] * x)

def fitLog(xs, ys):
    """ genereert functie die een logaritmische curve fit is

    :param xs ([float]): lijst met x-waarden
    :param ys ([float]): lijst met y-waarden
    :return (functie float -> float): logaritmische functie die de curve fit is van xs op ys
    """

    # bron: https://towardsdatascience.com/basic-curve-fitting-of-scientific-data-with-python-9592244a2509 en
    #   en  https://stackoverflow.com/questions/3433486/how-to-do-exponential-and-logarithmic-curve-fitting-in-python-i-found-only-poly
    def logarithmic (x, a, b):
        return a + b * np.log(x)

    pars, cov = curve_fit(f=logarithmic , xdata=xs, ydata=ys, p0=[0, 0], bounds=(-np.inf, np.inf))

    return lambda x : pars[0] + pars[1] * np.log(x)

def rKwadraat(xs, ys, f):
    ''' geef de r²-waarde voor ys t.o.v. de functie toegepast op xs

    :param xs ([double]): waarden op de x-as
    :param ys ([double]): waarden op de y-as:
    :param f (functie: double -> double): functie toe te passen op xs
    :return: de r²-waarde tussen ys en f(xs). Des te dichter bij 1 des te beter
    '''
    correlaties = np.corrcoef(ys, list(map(f,xs)))
    r2 = correlaties[0, 1]
    return r2