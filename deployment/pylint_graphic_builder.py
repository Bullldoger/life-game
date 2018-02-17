import matplotlib.pyplot as plt


def generate_graphic():
    rates = []
    with open('../reports/pylint_report.txt', 'r') as stream:
        lines = stream.readlines()
        for line in lines:
            if 'rated at ' in line:
                pos1 = line.index('rated at ')
                pos2 = line.index(' (previous')
                rate = [float(num) for num in line[pos1 + len('rated at '): pos2].split('/')]
                rates.append(rate[0] / rate[1])
    plt.figure(figsize=(15, 7))
    plt.plot(range(len(rates)), rates)
    plt.savefig('../reports/pylint_report_graphic.png')


if __name__ == 'main':
    generate_graphic()
