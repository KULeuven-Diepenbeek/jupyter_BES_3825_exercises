from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot

##############################
# versies voor een DataFrame #
##############################

def plotDataFrame(data, kolomX, kolomY, titel = None, kleur='k', nieuwePlot = True, label = False):
    """ plot een reeks data volgens de opgegeven parameters
        # voorbeelden van oproepen
        #   plotData(df, "x", "y") : toont de plot van df["x"] t.o.v. df["y"], in zwart en in nieuw venster
        #   plotData(df, "x", "y1", kleur = 'r', nieuwePlot = False) : voegt df["y1"] toe aan de vorige grafiek in het rood toe
        #   plt = plotData(df, "x", "y1", kleur = 'b', titel="helaba") : maakt nieuwe grafiek met df["y1"] in het blauw met als titel "helaba"
        #   plt.xscale('symlog')  # zet de x-as logaritmisch

    :param data (DataFrame): het dataframe waar de gegevens uit komen
    :param kolomX (string): de naam van de kolom die op de x-as moet komen
    :param kolomY (string): de naam van de kolom die op de y-as moet komen
    :param titel (string, optional): titel van de grafiek, kolomY indien niks ingevuld
    :param kleur (kleur, optional): kleur van de grafiek volgens https://matplotlib.org/api/_as_gen/matplotlib.pyplot.colors.html
    :param nieuwePlot (boolean, optional): moet deze grafiek in een nieuw venster (True) of toegevoegd aan de vorige figuur (False)
    :param label (boolean, optional): of al dan niet een label IN de plot moet verschijnen
    :return: het plt-object zodat je nadien nog verdere fijntuning kan doen
    """
    if nieuwePlot:
        plt.figure()
    if label:
        plt.plot(data[kolomX], data[kolomY], kleur, label = kolomY)
        plt.legend()
    else:
        plt.plot(data[kolomX], data[kolomY], kleur)
    plt.xlabel(kolomX)
    plt.ylabel(kolomY)
    if titel == None:
        plt.title(kolomY)
    else:
        plt.title(titel)
    plt.grid(True)
    # plt.show()
    return plt

def plotDataFrameTweeAssen(data, kolomX, kolomLinksY, kolomRechtsY, titel = None, label = False):
    """ maak een figuur met één plot met twee verschillende assen

    :param data (DataFrame): het dataframe waar de gegevens uit komen
    :param kolomX (string): de naam van de kolom die op de x-as moet komen
    :param kolomLinksY (string): de naam van de kolom die op de linkse y-as moet komen
    :param kolomRechtsY (string): de naam van de kolom die op de rechtse y-as moet komen
    :param titel (string, optional): titel van de grafiek
    :param label (boolean, optional): of al dan niet een label IN de plot moet verschijnen
    :return: het plt-object zodat je nadien nog verdere fijntuning kan doen
    """
    xAs = data[kolomX]
    yAsLinks = data[kolomLinksY]
    yAsRechts = data[kolomRechtsY]

    as1 = host_subplot(111)

    kleur = 'tab:red'
    as1.set_xlabel(kolomX)
    as1.set_ylabel(kolomLinksY, color=kleur)
    if label:
        as1.plot(xAs, yAsLinks, color=kleur, label = kolomLinksY)
    else:
        as1.plot(xAs, yAsLinks, color=kleur)
    as1.tick_params(axis='y', labelcolor=kleur)

    kleur = 'tab:blue'
    as2 = as1.twinx()
    as2.set_xlabel(kolomX)
    as2.set_ylabel(kolomRechtsY, color=kleur)
    if label:
        as2.plot(xAs, yAsRechts, color=kleur, label = kolomRechtsY)
    else:
        as2.plot(xAs, yAsRechts, color=kleur)
    as2.tick_params(axis='y', labelcolor=kleur)


    if not (titel == None):
        plt.title(titel)
    if label:
        plt.legend()
    plt.grid(True)
    plt.show()
    return plt

def plotDataFrameNaastElkaar(data, kolomLinksX, kolomLinksY, kolomRechtsX, kolomRechtsY, titelLinks = None, titelRechts = None, label = False):
    """ maak een figuur met twee aparte plots naast elkaar met verschillende assen

    :param data (DataFrame): het dataframe waar de gegevens uit komen
    :param kolomLinksX (string): de naam van de kolom die op de linkse x-as moet komen
    :param kolomLinksY (string): de naam van de kolom die op de linkse y-as moet komen
    :param kolomRechtsX (string): de naam van de kolom die op de rechtse x-as moet komen
    :param kolomRechtsY (string): de naam van de kolom die op de rechtse y-as moet komen
    :param titelLinks (string, optional): titel van de linkse grafiek
    :param titelRechts (string, optional): titel van de rechtse grafiek
    :param label (boolean, optional): of al dan niet een label IN de plot moet verschijnen
    :return: het plt-object zodat je nadien nog verdere fijntuning kan doen
    """
    xAsLinks = data[kolomLinksX]
    yAsLinks = data[kolomLinksY]
    xAsRechts = data[kolomRechtsX]
    yAsRechts = data[kolomRechtsY]

    figs, axes = plt.subplots(1,2)
    if label:
        axes[0].plot(xAsLinks, yAsLinks, label = kolomLinksY)
        axes[0].legend()
    else:
        axes[0].plot(xAsLinks, yAsLinks)
    axes[0].grid(True)
    axes[0].set_xlabel(kolomLinksX)
    axes[0].set_ylabel(kolomLinksY)
    if titelLinks == None:
        axes[0].title.set_text(kolomLinksY)
    else:
        axes[0].title.set_text(titelLinks)


    if label:
        axes[1].plot(xAsRechts, yAsRechts, label = kolomLinksY)
        axes[1].legend()
    else:
        axes[1].plot(xAsRechts, yAsRechts)
    axes[1].grid(True)
    axes[1].set_xlabel(kolomRechtsX)
    axes[1].set_ylabel(kolomRechtsY)
    if titelRechts == None:
        axes[1].title.set_text(kolomRechtsY)
    else:
        axes[1].title.set_text(titelRechts)
    plt.show()
    return plt


##############################
# versies voor functies      #
##############################

def plotFunctie(f, naamF, domeinX, naamX, titel = None, kleur='k', nieuwePlot = True, label = False):
    """ plot een reeks data volgens de opgegeven parameters

    :param f (functie met één parameter): de functie die geplot moet worden
    :param naamF (string): de naam van de functie die op de y-as moet komen
    :param domeinX (lijst met waarden): het inputdomein dat geplot moet worden
    :param naamX (string): de naam die op de x-as moet komen
    :param titel (string, optional): titel van de grafiek, naamF indien niks ingevuld
    :param kleur (kleur, optional): kleur van de grafiek volgens https://matplotlib.org/api/_as_gen/matplotlib.pyplot.colors.html
    :param nieuwePlot (boolean, optional): moet deze grafiek in een nieuw venster (True) of toegevoegd aan de vorige figuur (False)
    :param label (boolean, optional): of al dan niet een label IN de plot moet verschijnen
    :return: het plt-object zodat je nadien nog verdere fijntuning kan doen
    """
    if nieuwePlot:
        plt.figure()
    if label:
        plt.plot(list(domeinX), list(map(f, domeinX)), kleur, label=naamF)
        plt.legend()
    else:
        xAs = list(domeinX)
        yAs = list(map(f, domeinX))
        plt.plot(xAs, yAs, kleur)

    plt.xlabel(naamX)
    plt.ylabel(naamF)
    if titel == None:
        plt.title(naamF)
    else:
        plt.title(titel)
    plt.grid(True)
    # plt.show()
    return plt


def plotFunctiesTweeAssen(f1, naamF1, f2, naamF2, domeinX, naamX, titel = None, label = False):
    """ maak een figuur met één plot met twee verschillende assen

    :param f1 (functie met één parameter): de eerste functie die geplot moet worden
    :param naamF1 (string): de naam van de functie f1 die op de linkse y-as komt
    :param f2 (functie met één parameter): de tweede functie die geplot moet worden
    :param naamF2 (string): de naam van de functie f2 die op de rechtse y-as komt
    :param domeinX (lijst met waarden): het inputdomein dat geplot moet worden
    :param naamX (string): de naam die op de x-as moet komen
    :param titel (string, optional): titel van de grafiek
    :param label (boolean, optional): of al dan niet een label IN de plot moet verschijnen
    :return: het plt-object zodat je nadien nog verdere fijntuning kan doen
    """
    xAs = list(domeinX)
    yAsLinks = list(map(f1, domeinX))
    yAsRechts = list(map(f2, domeinX))

    as1 = host_subplot(111)

    kleur = 'tab:red'
    as1.set_xlabel(naamX)
    as1.set_ylabel(naamF1, color=kleur)
    if label:
        as1.plot(xAs, yAsLinks, color=kleur, label=naamF1)
    else:
        as1.plot(xAs, yAsLinks, color=kleur)
    as1.tick_params(axis='y', labelcolor=kleur)

    as2 = as1.twinx()

    kleur = 'tab:blue'
    as2.set_xlabel(naamX)
    as2.set_ylabel(naamF2, color=kleur)
    if label:
        as2.plot(xAs, yAsRechts, color=kleur, label=naamF2)
    else:
        as2.plot(xAs, yAsRechts, color=kleur)
    as2.tick_params(axis='y', labelcolor=kleur)

    if not (titel == None):
        plt.title(titel)
    plt.grid(True)
    if label:
        plt.legend()
    plt.show()
    return plt

def plotTweeFunctiesNaastElkaar(f1, naamF1, domeinF1, naamDomeinF1, f2, naamF2, domeinF2, naamDomeinF2, titelLinks = None, titelRechts = None, label = False):
    """ maak een figuur met twee aparte plots naast elkaar met verschillende assen

    :param f1 (functie met één parameter): de eerste functie die geplot moet worden
    :param naamF1 (string): de naam van de functie f1 die op de y-as van de linkse grafiek komt
    :param domeinF1 (lijst met waarden): het inputdomein dat links geplot moet worden
    :param naamDomeinF1 (string): de naam die op de linkse x-as moet komen
    :param f2 (functie met één parameter): de tweede functie die geplot moet worden
    :param naamF2 (string): de naam van de functie f2 die op de y-as van de rechtse grafiek komt
    :param domeinF2 (lijst met waarden): het inputdomein dat rechts geplot moet worden
    :param naamDomeinF2 (string): de naam die op de rechtse x-as moet komen
    :param titelLinks (string, optional): titel van de linkse grafiek
    :param titelRechts (string, optional): titel van de rechtse grafiek
    :param label (boolean, optional): of al dan niet een label IN de plot moet verschijnen
    :return: het plt-object zodat je nadien nog verdere fijntuning kan doen
    """
    xAsLinks = list(domeinF1)
    yAsLinks = list(map(f1, domeinF1))
    xAsRechts = list(domeinF2)
    yAsRechts = list(map(f2, domeinF2))

    figs, axes = plt.subplots(1,2)
    if label:
        axes[0].plot(xAsLinks, yAsLinks, label=naamF1)
        axes[0].legend()
    else:
        axes[0].plot(xAsLinks, yAsLinks)
    axes[0].grid(True)
    axes[0].set_xlabel(naamDomeinF1)
    axes[0].set_ylabel(naamF1)
    if titelLinks == None:
        axes[0].title.set_text(naamF1)
    else:
        axes[0].title.set_text(titelLinks)

    if label:
        axes[1].plot(xAsRechts, yAsRechts, label=naamF2)
        axes[1].legend()
    else:
        axes[1].plot(xAsRechts, yAsRechts)

    axes[1].grid(True)
    axes[1].set_xlabel(naamDomeinF2)
    axes[1].set_ylabel(naamF2)
    if titelRechts == None:
        axes[1].title.set_text(naamF2)
    else:
        axes[1].title.set_text(titelRechts)
    plt.show()
    return plt


#######################################
# oorspronkelijke namen in de cursus  #
#######################################
def plotData(data, kolomX, kolomY, titel = None, kleur='k', nieuwePlot = True):
    plotDataFrame(data, kolomX, kolomY, titel, kleur, nieuwePlot)

def plotGrafiekTweeAssen(data, kolomX, kolomLinksY, kolomRechtsY, titel = None):
    plotDataFrameTweeAssen(data, kolomX, kolomLinksY, kolomRechtsY, titel)

def plotTweeGrafiekenNaastElkaar(data, kolomX, kolomLinksY, kolomRechtsY, titelLinks = None, titelRechts = None):
    plotDataFrameNaastElkaar(data, kolomX, kolomLinksY, kolomX, kolomRechtsY, titelLinks, titelRechts)

