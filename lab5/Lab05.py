# Indexes of columns of city data file.
CITY_NAME = 0
CITY_SHORT_CODE = 1
CITY_NUMERIC_CODE = 2
CITY_POPULATION = 3
CITY_METRIC_AREA = 4
CITY_IMPERIAL_AREA = 5
CITY_REGION_CODE = 6

# Indexes of columns of region info file
REGION_CODE = 0
REGION_NAME_TR = 1
REGION_NAME_EN = 2


def import_cities(city_data, city_data_filename):
    """ Construct a dictionary containing name of the city as key and
    other fields in a list as value

    :param city_data: Dictionary to import cities from file
    :param city_data_filename: Name of a file containing information of a city
    """
    with open(city_data_filename) as f_cities:
        for city in f_cities:
            city = city.strip("\n").split("\t")
            city_data[city[CITY_NAME]] = [
                city[CITY_SHORT_CODE],
                int(city[CITY_NUMERIC_CODE]),
                int(city[CITY_POPULATION][1:-1].replace(",", "")),
                (
                    int(city[CITY_METRIC_AREA][1:-1].replace(",", "")),
                    int(city[CITY_IMPERIAL_AREA][1:-1].replace(",", ""))
                ),
                city[CITY_REGION_CODE]
            ]


def import_regions(region_data, region_info_filename):
    """ Construct a dictionary containing region short name as key and
    English and Turkish name of region in a list as value

    :param region_data: Dictionary to import regions from file
    :param region_info_filename: Name of a file containing region information
    """
    with open(region_info_filename) as f_regions:
        for region in f_regions:
            region = region.strip("\n").split("\t")
            region_data[region[REGION_CODE]] = [
                region[REGION_NAME_TR],
                region[REGION_NAME_EN]
            ]


def get_region(region_name, region_lookup):
    """ Get short name of a region from region lookup dictionary

    :param region_name: Name of the region either in English or Turkish
    :param region_lookup: Dictionary to lookup regions, should be the one
        filled by import_regions
    :return: Returns the short name of a region
    """
    for region_code in region_lookup.keys():
        if region_name in region_lookup[region_code]:
            return region_code


def get_cities(city_data, region_name, region_lookup):
    """ Get cities and their populations in specific region.

    :param city_data: Dictionary containing city data, should be the one
        filled by import_cities
    :param region_name: Name of the region
    :param region_lookup: Region lookup dictionary, should be the one
        filled by import_regions
    :return: A tuple of list of city names and tuple of populations.
        List and tuple in the return tuple are parallel to each other.
    """
    cities = []
    populations = ()

    region_code = get_region(region_name, region_lookup)
    for city_name in city_data.keys():
        # To prevent lookup more then once
        current_city = city_data[city_name]

        # Indexes before area tuple are -1 of file index since the only thing
        # shifted is name of the city, however, after area tuple, indexes are
        # -2 of file index, because of joining two values into one, namely
        # area tuple
        if current_city[CITY_REGION_CODE - 2] == region_code:
            cities.append(city_name)
            populations += (current_city[CITY_POPULATION - 1],)

    return cities, populations


def display_city_information(city_data, city_name):
    """ Print city information

    :param city_data: Dictionary containing city data, should be the one
        filled by import_cities
    :param city_name: Name of the city
    """
    city = city_data[city_name]

    # Same indexing rules as in function get_cities
    print(
        "Name: {}\n"
        "Short Code: {}\n"
        "Numeric Code: {}\n"
        "Population: {}\n"
        "Area (km): {}\n"
        "Area (mil): {}\n"
        "Region: {}\n".format(
            city_name,
            city[CITY_SHORT_CODE - 1],
            city[CITY_NUMERIC_CODE - 1],
            city[CITY_POPULATION - 1],
            city[CITY_METRIC_AREA - 1][0],
            city[CITY_METRIC_AREA - 1][1],
            city[CITY_REGION_CODE - 2])
    )


city_data = {}
region_lookup = {}

import_cities(city_data, "city_data.txt")
import_regions(region_lookup, "region_lookup.txt")

choice = 0

while True:
    print("1 - Find Cities in Region\n"
          "2 - Find Average Population of region\n"
          "3 - Display City Information\n"
          "4 - Quit\n")

    choice = int(input("Enter choice: "))

    if choice == 4:
        print("Exiting...")
        # exit(0)
        break

    if choice == 1 or choice == 2:
        region_name = input("\nEnter region name: ")
        cities, populations = get_cities(city_data, region_name, region_lookup)
        if choice == 1:
            print(f"Cities in {region_name}: {cities}")
        else:
            print("Average population of {}: {}".format(
                region_name,
                sum(populations) // len(populations)
            ))
    elif choice == 3:
        city_name = input("\nEnter city name: ")
        display_city_information(city_data, city_name)
    else:
        print("\nInvalid choice")

    print()
