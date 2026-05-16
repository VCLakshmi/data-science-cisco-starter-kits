import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/raw/jean-pocket-measurements.csv")
print(df)


# avg difference in pocket `height_front` between women's and men's jean
avg_height_front_women = df.query("gender == 'women'")["height_front"].mean()
print(f"\nAverage pocket `height_front` for women: {avg_height_front_women}")

avg_height_front_men = df.query("gender == 'men'")["height_front"].mean()
print(f"Average pocket `height_front` for men: {avg_height_front_men}")

print(f"Average difference in pocket `height_front` between women and men's jean: {avg_height_front_men - avg_height_front_women}")

# Check if there is a significant difference in pocket `height_front` between skinny and straight styles within the same gender
avg_skinny_jean_height_front_women = df.query("gender == 'women' & style == 'skinny'")["height_front"].mean()
avg_straight_jean_height_front_women = df.query("gender == 'women' & style == 'straight'")["height_front"].mean()

print(f"\nWomen:\nSkinny jean average height_front: {avg_skinny_jean_height_front_women}")
print(f"Straight jean average height_front: {avg_straight_jean_height_front_women}")

print(f"Difference: [{avg_straight_jean_height_front_women - avg_skinny_jean_height_front_women}]")


avg_skinny_jean_height_front_men = df.query("gender == 'men' & style == 'skinny'")["height_front"].mean()
avg_straight_jean_height_front_men = df.query("gender == 'men' & style == 'straight'")["height_front"].mean()
print(f"\nMen:\nSkinny jean average height_front: {avg_skinny_jean_height_front_men}")
print(f"Straight jean average height_front: {avg_straight_jean_height_front_men}")

print(f"Difference: [{avg_skinny_jean_height_front_men - avg_straight_jean_height_front_men}]")

# comparing back pocket sizes.
# men
avg_back_pocket_height_men = df.query("gender == 'men'")["height_back"].mean()
avg_back_pocket_width_men = df.query("gender == 'men'")["width_back"].mean()
print(f"\nMen:\nAverage back pocket height: {avg_back_pocket_height_men}")
print(f"Average back pocket width: {avg_back_pocket_width_men}")

# women
avg_back_pocket_height_women = df.query("gender == 'women'")["height_back"].mean()
avg_back_pocket_width_women = df.query("gender == 'women'")["width_back"].mean()
print(f"\nWomen:\nAverage back pocket height: {avg_back_pocket_height_women}")
print(f"Average back pocket width: {avg_back_pocket_width_women}")

avg = df.groupby("gender")[["height_back", "width_back"]].mean()
print(f"\n{avg}")

## Samsung S22 Ultra phone's height 17.27 cm
phone_height = 17.27

# Percentage of men's and women's jeans can comfortably fit your phone in the pockets
## Find the pocket which is tall enough to hold 17.27 cm of phone.
height_front_women = df.query("gender == 'women' & height_front >= 17.27")
height_front_men = df.query("gender == 'men' & height_front >= 17.27")

print("\nWomen:\nWomen's Jean that has front pocket height greater than the phone's height:")
print(height_front_women)
print("\nMen:\nMen's Jean that has front pocket height greater than the phone's height:")
print(height_front_men)


total_women_jean = len(df[df["gender"] == "women"])
total_men_jean = len(df[df["gender"] == "men"])

percentage_of_women_jean = len(height_front_women)/total_women_jean * 100
percentage_of_men_jean = len(height_front_men)/total_men_jean * 100

print(f"\nPercentage of Women's Jean that can fit a phone of heigth 17.27cm in front pocket: {percentage_of_women_jean}")
print(f"\nPercentage of Men's jean that can fit a phone of height 17.27cm in front pocket: {percentage_of_men_jean}")


## Pandas method:
result = df.groupby("gender").apply(
    lambda x: (x >= phone_height).sum()/len(x) * 100
)
print(result)
