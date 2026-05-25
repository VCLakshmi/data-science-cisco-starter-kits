import pandas as pd

df = pd.read_csv("data/raw/people-on-banknotes.csv")
df = df.drop(columns=["value"])
df = df.drop_duplicates(subset="name")
print(df)


# portion of individuals featured are male versus female
count_of_individuals = df["gender"].value_counts()
print(f"\nCount by gender:\n{count_of_individuals}")

# portion of individuals featured: writer vs politician
count_of_individuals_by_occupation = df["occupation"].value_counts()
print(f"\nCount by occupation:\n{count_of_individuals_by_occupation}")

writer_count = count_of_individuals_by_occupation["Writer"]
politician_count = count_of_individuals_by_occupation["Politician"]
print(f"\nNumber of writers featured: {writer_count}")
print(f"Number of politicians featured: {politician_count}")


# percentage of Musicians featured on bank notes
musicians_percentage = df["occupation"].value_counts(normalize=True)["Musician"] * 100
print(f"\nPercentage of musicians featured: {musicians_percentage}")


# percentage of bank notes issued before the person's death
notes_before_death = df["first_death_diff"].isna().sum() + df.query("first_death_diff < 0").shape[0]
print(f"\nNumber of bank notes issued before the person's death: {notes_before_death}")
percentage_of_notes_before_death = (notes_before_death / df.shape[0]) * 100
print(f"Percentage of bank notes issued before the person's death: {percentage_of_notes_before_death}")


# oldest historical figure featured on a bank note
oldest = df.loc[df["death"].dropna().idxmin()]
print(f"\nOldest historical figure featured on a bank note: {oldest['name']}")


# countries that figures oldest historical figures on their bank notes
# convert the death field to numeric
df["death"] = pd.to_numeric(df["death"], errors="coerce")
historic_persons = df.groupby("country")["death"].median().sort_values()
historic_persons.columns = ["country", "median_death_year"]
print("\nCountries that figures oldest historical persons on their bank notes:")
print(historic_persons.head(5))


# percentage of individuals died atleast 100 years before appearing on the bank notes
individuals_died_100_years_before = (df["first_death_diff"] >= 100).mean() * 100
print(f"\nPercentage of individuals who died at least 100 years before appearing on the bank notes:{individuals_died_100_years_before}")


# individuals who appeared on a banknote just one year after their death
individuals_appeared_one_year_after_death = df.query("first_death_diff == 1")
print(f"\nIndividuals who appeared on a banknote just one year after their death:")
print(individuals_appeared_one_year_after_death)
