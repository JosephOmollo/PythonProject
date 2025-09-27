import sys
import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/sci2pro/code-fastfoundations/refs/heads/main/day3/FAOSTAT_data_7-23-2022.csv"
data = pd.read_csv(url)



print("Available Areas in dataset:")
print(data["Area"].unique())

data = data[["Area", "Year", "Element", "Item", "Value"]] #inner bracket - list of column names,  outer = pandas' selecting data
def create_ghana_table():
    ghana_data = data[data["Area"] == "Ghana"]
    ghana_table = ghana_data.pivot(index="Year", columns="Element",  values="Value")
    return ghana_table[["Area harvested", "Yield", "Production"]]

def create_cote_dIvoire_table():
    cote_dIvoire_data = data[data["Area"] == "Côte d'Ivoire" ]
    cote_dIvoire_table = cote_dIvoire_data.pivot(index="Year", columns="Element",  values="Value")
    return cote_dIvoire_table[["Area harvested", "Yield" , "Production"]]
#only valid parameters for pivot are index, columns and values. item isn't a valid parameter
ghana_table = create_ghana_table()
cote_dIvoire_table = create_cote_dIvoire_table()

def scatter_plot(ghana_table, cote_dIvoire_table):
    ghana = create_ghana_table()
    cote_dIvoire = create_cote_dIvoire_table()

    #ghana plot
    fig, ax = plt.subplots()
    ax.scatter(ghana.index, ghana["Yield"])
    ax.set_title("Ghana scatter plot Cocoa yield.")
    ax.set_xlabel("Year")
    ax.set_ylabel("Yield")
    plt.show()

    # cote_dIvoire plot
    fig, ax = plt.subplots()
    ax.scatter(cote_dIvoire.index, cote_dIvoire["Yield"])
    ax.set_title("Cote dIvoire scatter plot Cocoa yield.")
    ax.set_xlabel("Year")
    ax.set_ylabel("Yield")
    plt.show()

def plot_barchart(ghana_table, cote_dIvoire_table):
    ghana = create_ghana_table()
    cote_dIvoire = create_cote_dIvoire_table()

    #ghana bar chart
    fig, ax = plt.subplots()
    ax.bar(ghana.index, ghana["Area harvested"])
    ax.set_title("Ghana bar chart Cocoa yield.")
    ax.set_xlabel("Year")
    ax.set_ylabel("Area harvested")
    plt.show()
    #cote_dIvoire bar chart
    fig, ax = plt.subplots()
    ax.bar(cote_dIvoire.index, cote_dIvoire["Area harvested"])
    ax.set_title("Cote dIvoire bar chart Cocoa yield.")
    ax.set_xlabel("Year")
    ax.set_ylabel("Area harvested")
    plt.show()


print(f"ghana_table = \n{ghana_table}")
print(f"cote_dIvoire_table = \n{cote_dIvoire_table}")

def plot_multiplot_and_export(ghana_table, cote_dIvoire_table):
    ghana = create_ghana_table()
    cote_dIvoire = create_cote_dIvoire_table()

    #scatter plot multiplot and export
    fig, ax = plt.subplots(1,2,figsize=(16,6))
    fig.suptitle("Cote dIvoire and Ghana scatter plot Cocoa yield.", color="purple",fontsize=20,fontweight="bold")
    ax[0].scatter(ghana.index, ghana["Yield"])
    ax[0].set_title("Ghana scatter plot Cocoa yield.")
    ax[0].set_xlabel("Year")
    ax[0].set_ylabel("Yield")

    ax[1].scatter(cote_dIvoire.index, cote_dIvoire["Yield"])
    ax[1].set_title("Cote dIvoire bar chart Cocoa yield.")
    ax[1].set_xlabel("Year")
    ax[1].set_ylabel("Yield")
    plt.show()
    fig.savefig("plot_multiplot_and_export_scatter_plot.png")
    plt.close(fig)

    #bar chart multiplot and export
    fig, ax = plt.subplots(1,2, figsize=(16,6))
    fig.suptitle("Cote dIvoire and Ghana multiplot bar chart Cocoa yield.", color="green",fontsize=20,fontweight="bold")
    ax[0].bar(ghana.index, ghana["Area harvested"])
    ax[0].set_title("Ghana bar chart Cocoa yield.")
    ax[0].set_xlabel("Year")
    ax[0].set_ylabel("Area harvested")

    ax[1].bar(cote_dIvoire.index, cote_dIvoire["Area harvested"])
    ax[1].set_title("Cote dIvoire bar chart Cocoa yield.")
    ax[1].set_xlabel("Year")
    ax[1].set_ylabel("Area harvested")
    plt.show()
    fig.savefig("plot_multiplot_and_export_bar_chart_plot.png")
    plt.close(fig)

    # 4 panels in single plot
    fig, ax = plt.subplots(1,4, figsize=(20, 8))
    fig.suptitle("Ghana and Cote dIvoire multiplot bar chart and scatter plot Cocoa yield.", color="blue",fontsize=20,fontweight="bold")
    ax[0].bar(ghana.index, ghana["Area harvested"])
    ax[0].set_title("Ghana bar chart Cocoa yield.")
    ax[0].set_xlabel("Year")
    ax[0].set_ylabel("Area harvested")
    ax[1].bar(cote_dIvoire.index, cote_dIvoire["Area harvested"])
    ax[1].set_title("Cote dIvoire bar chart Cocoa yield.")
    ax[1].set_xlabel("Year")
    ax[1].set_ylabel("Area harvested")
    ax[2].scatter(ghana.index, ghana["Yield"])
    ax[2].set_title("Ghana scatter plot Cocoa yield.")
    ax[2].set_xlabel("Year")
    ax[2].set_ylabel("Yield")
    ax[3].scatter(cote_dIvoire.index, cote_dIvoire["Yield"])
    ax[3].set_title("Cote dIvoire bar chart Cocoa yield.")
    ax[3].set_xlabel("Year")
    ax[3].set_ylabel("Yield")
    fig.savefig("plot_multiplot_and_export_scatter_and_bar_chart.pdf", format="pdf")
    plt.show()
    #fig.savefig("plot_multiplot_and_export_scatter_and_bar_chart_plots.png")
    plt.close(fig)



def main():
    scatter_plot(ghana_table, cote_dIvoire_table)
    plot_barchart(ghana_table, cote_dIvoire_table)
    plot_multiplot_and_export(ghana_table, cote_dIvoire_table)
    return 0

if __name__ == "__main__":
    sys.exit(main())