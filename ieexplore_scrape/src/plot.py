import matplotlib.pyplot as plt
import numpy as py


def extract_dates(data):
    dates = []
    print len(data)
    for n in data:
        date = n.split(",")[0]
        if date != "None":
            dates.append(int(date))

    return dates


def main():
    with open("../data/ml_years_conf.txt", "r") as f:
        data = f.readlines()

    dates = extract_dates(data)


    bins = py.linspace(py.min(dates), py.max(dates))
    plt.hist(dates, bins, color=(0.9, 0.5, 0.5))
    plt.axis((1960, 2016, 0, 2500))
    plt.title("Publication dates of 14995 'Machine Learning' conference papers scraped from IEEExplore", fontsize=18)
    plt.xlabel("Date")
    plt.ylabel("Frequency")
    plt.show()

if __name__ == "__main__":
    main()
