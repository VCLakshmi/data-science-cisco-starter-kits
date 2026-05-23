import pandas as pd


df = pd.read_csv("data/raw/first-day-of-week.csv")
print(df)

# Territories that shows Friday, Saturday, Sunday and Monday as first day of the week.
print("\nCount of Territories with different days as first day of the week:")

first_day_fri_territories = df.query("first_day == 'fri'")["territory"].count()
print(f"Territories that starts with Friday: {first_day_fri_territories}")

first_day_sat_territories = df.query("first_day == 'sat'")["territory"].count()
print(f"Territories that starts with Saturday: {first_day_sat_territories}")

first_day_sun_Territories = df.query("first_day == 'sun'")["territory"].count()
print(f"Territories that starts with Sunday: {first_day_sun_Territories}")

first_day_mon_territories = df.query("first_day == 'mon'")["territory"].count()
print(f"Territories that starts with Monday: {first_day_mon_territories}")


# read population data
population_df = pd.read_csv("data/raw/population.csv")
print("\nPopulation in the year 2020 for each territory in millions: ")
print(population_df)

# merge population data with first_day of week data
first_day_of_week = df.merge(population_df, on="alpha3", how="left")
first_day_of_week.to_csv("data/processed/first-day-of-week-with-population.csv")


# population that starts their week on Friday, Saturday, Sunday, Monday
friday_population_df = first_day_of_week.query("first_day == 'fri'")
friday_population = friday_population_df.dropna()["population"].sum()
print(f"Number of people in millions who starts their week on Friday: {friday_population}")

saturday_population_df = first_day_of_week.query("first_day == 'sat'")
saturday_population = saturday_population_df.dropna()["population"].sum()
print(f"Number of people in millions who starts their week on Saturday: {saturday_population}")

sunday_population_df = first_day_of_week.query("first_day == 'sun'")
sunday_population = sunday_population_df.dropna()["population"].sum()
print(f"Number of people in millions who starts their week on Sunday: {sunday_population}")

monday_population_df = first_day_of_week.query("first_day == 'mon'")
monday_population = monday_population_df.dropna()["population"].sum()
print(f"Number of people in millions who starts their week on Monday: {monday_population}")


# read four-regions data
four_regions_df = pd.read_csv("data/raw/four-regions.csv")
print("\nFour regions data:")
print(four_regions_df)

# merge four-regions data with first_day_of_week data
first_day_of_week_with_region = first_day_of_week.merge(four_regions_df, how="left", on="alpha3")
first_day_of_week_with_region.to_csv("data/processed/first-day-of-week-with-population-and-region.csv")
print("\nFirst day of week with population and region data:")
print(first_day_of_week_with_region)

# Regions that starts their week on Sunday and Monday
sunday_region_df = first_day_of_week_with_region.query("first_day == 'sun'")
sunday_region = sunday_region_df.dropna()["four_regions"].value_counts()
print(f"\nRegions that starts their week on Sunday:\n{sunday_region}")

monday_region_df = first_day_of_week_with_region.query("first_day == 'mon'")
monday_region = monday_region_df.dropna()["four_regions"].value_counts()
print(f"\nRegions that starts their week on Monday:\n{monday_region}")
