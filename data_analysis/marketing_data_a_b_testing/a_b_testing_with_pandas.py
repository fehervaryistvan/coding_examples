import pandas as pd

# Load the dataset
ad_clicks = pd.read_csv('ad_clicks.csv')

# Display the first few rows of the dataset
print(ad_clicks.head())

# Group by 'utm_source' and count the number of 'user_id' for each source
utm_source = ad_clicks.groupby("utm_source") \
                      .user_id.count() \
                      .reset_index()

# Create a new column 'is_click' to indicate if a user clicked on an ad
ad_clicks['is_click'] = ~ad_clicks \
    .ad_click_timestamp.isnull()

# Group by 'utm_source' and 'is_click' to count the number of users who clicked and didn't click for each source
clicks_by_source = ad_clicks.groupby(["utm_source", "is_click"]).user_id.count() \
                             .reset_index()

# Pivot the 'clicks_by_source' DataFrame to get the count of users who clicked and didn't click for each source
clicks_pivot = clicks_by_source.pivot(
    columns="is_click",
    index="utm_source",
    values="user_id").reset_index()

# Calculate the percentage of users who clicked for each source
clicks_pivot["percent_clicked"] = clicks_pivot[True] / \
    (clicks_pivot[True] + clicks_pivot[False])

print(clicks_pivot)

# Group by 'experimental_group' and count the number of users in each group
experimental_group = ad_clicks.groupby("experimental_group").user_id.count()

# Group by 'experimental_group' and 'is_click' to count the number of users who clicked and didn't click for each group
ad_click = ad_clicks.groupby(["experimental_group", "is_click"]).user_id.count().reset_index()

# Pivot the 'ad_click' DataFrame to get the count of users who clicked and didn't click for each group
clicks_pivot_A_B = ad_click.pivot(
    columns="is_click",
    index="experimental_group",
    values="user_id").reset_index()

# Calculate the percentage of users who clicked for each group
clicks_pivot_A_B["percent_clicked"] = clicks_pivot_A_B[True] / \
    (clicks_pivot_A_B[True] + clicks_pivot_A_B[False])

print(clicks_pivot_A_B)

# Filter data for 'experimental_group' A
a_clicks = ad_clicks[
    ad_clicks.experimental_group
    == 'A']

# Filter data for 'experimental_group' B
b_clicks = ad_clicks[
    ad_clicks.experimental_group
    == 'B']

# Group by 'is_click' and 'day' for group A and count the number of users for each combination
a_clicks_by_day = a_clicks.groupby(["is_click", "day"]).user_id.count().reset_index()

# Pivot the 'a_clicks_by_day' DataFrame to get the count of users who clicked and didn't click for each day in group A
a_clicks_by_day_pivot = a_clicks_by_day.pivot(
    columns="is_click",
    index="day",
    values="user_id").reset_index()

# Calculate the percentage of users who clicked for each day in group A
a_clicks_by_day_pivot["percent_clicked"] = a_clicks_by_day_pivot[True] / \
    (a_clicks_by_day_pivot[True] + a_clicks_by_day_pivot[False])

print(a_clicks_by_day_pivot)

# Group by 'is_click' and 'day' for group B and count the number of users for each combination
b_clicks_by_day = b_clicks.groupby(["is_click", "day"]).user_id.count().reset_index()

# Pivot the 'b_clicks_by_day' DataFrame to get the count of users who clicked and didn't click for each day in group B
b_clicks_by_day_pivot = b_clicks_by_day.pivot(
    columns="is_click",
    index="day",
    values="user_id").reset_index()

# Calculate the percentage of users who clicked for each day in group B
b_clicks_by_day_pivot["percent_clicked"] = b_clicks_by_day_pivot[True] / \
    (b_clicks_by_day_pivot[True] + b_clicks_by_day_pivot[False])

print(b_clicks_by_day_pivot)
