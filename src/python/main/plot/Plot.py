import matplotlib.pyplot as plt

def plotDf(df, title, fields = None):
    if fields is not None:
        try:
            df = df[fields]
        except KeyError:
            print("ERROR: Incorrect column input")
            return None
    plt.figure(); 
    df.plot(); 
    plt.legend(loc='best')
    plt.title(title)
    plt.show()
