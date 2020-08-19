import numpy as np
import matplotlib.pyplot as plt


INDICATORS_COL_FERTILITY = 0
INDICATORS_COL_MALE_LIFE = 3
INDICATORS_COL_FEMALE_LIFE = 4
INDICATORS_COL_MORTALITY = 5
INDICATORS_COL_GDP = 6
INDICATORS_COL_MALE_EMPL = 7
INDICATORS_COL_FEMALE_EMPL = 8

countries = np.loadtxt("countries.txt", dtype=str, delimiter="\t", skiprows=1)
indicators = np.loadtxt("indicators.txt", dtype=float, delimiter="\t", skiprows=1)

indicators_under_1000 = indicators[indicators[:, INDICATORS_COL_GDP] < 1000]

is_europe_country = countries[:, 1] == "Europe"
europe_countries = countries[is_europe_country]
europe_data = indicators[is_europe_country]

turkey_index = np.where(countries[:, 0] == "Turkey")[0][0]
turkey_employment_data = indicators[:, INDICATORS_COL_MALE_EMPL:INDICATORS_COL_FEMALE_EMPL + 1][turkey_index, :]


# first figure
plt.figure(1)

# Life Expectancy for Europe by Gender
labels = ["Europe Male", "Europe Female"]
life_expectancies = [
    np.mean(europe_data[:, INDICATORS_COL_MALE_LIFE]),      # men
    np.mean(europe_data[:, INDICATORS_COL_FEMALE_LIFE])     # women
]
x = np.arange(len(labels))

plt.subplot(1, 2, 1)
plt.title("Life Expectancy for Europe by Gender")
plt.bar(x[0], life_expectancies[x[0]], label="Men")
plt.bar(x[1], life_expectancies[x[1]], label="Women")
plt.ylabel("Life Expectancy")
plt.xticks(x, labels)   # no need for a new axis, we can set xticks for current plot
plt.legend()


# GDP - Infant Mortality
gdb_under_1000 = indicators_under_1000[:, INDICATORS_COL_GDP]
mortality = indicators_under_1000[:, INDICATORS_COL_MORTALITY]

plt.subplot(1, 2, 2)
plt.title("Infant Mortality with GDP under 1000")
plt.plot(gdb_under_1000, mortality, "*--")
plt.xticks(np.arange(0, 1001, 200))
plt.xlabel("GDP")
plt.ylabel("Infant Mortality")


# second figure
plt.figure(2)

# Employment Rates by Gender in Turkey
labels = ["Male", "Female"]
employment_rates = [
    turkey_employment_data[0],  # male
    turkey_employment_data[1]   # female
]
explode = (0, 0.1)

plt.subplot(2, 1, 1)
plt.title("Employment Rates by Gender in Turkey")
plt.pie(employment_rates, labels=labels, autopct="%2.1f%%", explode=explode)

# Frequency of Fertility Rates for all Countries (4 bins)
plt.subplot(2, 1, 2)
plt.title("Frequency of Fertility Rates for all Countries (4 bins)")
data = plt.hist(indicators[:, INDICATORS_COL_FERTILITY], bins=4)
plt.xticks(data[1])

plt.show()
