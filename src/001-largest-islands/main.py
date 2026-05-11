import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/raw/largest-islands.csv")


# 10 largest islands in the tropic.
largest_islands = df.sort_values("rank") # df.sort_values("area", ascending=False).head(10)
print("\nTen largest islands in the tropic are:")
print(largest_islands.head(10))


# Largest island in each region
largest_island_region = largest_islands.groupby("region").first()
print("\nLargest islands in each region:")
print(largest_island_region)


# Create a line graph with `area` on the y-axis and `rank` on the x-axis.
plt.plot(largest_islands["rank"], largest_islands["area"])
plt.title("Island Area vs Rank")
plt.xlabel("rank")
plt.ylabel("area [km2]")
plt.savefig("outputs/figures/island_area_classified_by_rank.png")
plt.show()


# islands composed of multiple countries
islands = df.query("countries.str.contains(',')")
print("\nIslands that are composed of multiple countries:")
print(islands)
