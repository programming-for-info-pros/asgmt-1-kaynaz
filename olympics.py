import csv

# Open the CSV file
with open('2024_medalists_all.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    # Create a dictionary to store the count of gold medals for each country
    gold_medal_count = {}

    # Iterate over each row in the CSV file
    for row in reader:
        country = row[8]
        medal_type = row[3]

        # Check if the medal type is gold
        if medal_type == 'gold':
            # If the country is already in the dictionary, increment the count
            if country in gold_medal_count:
                gold_medal_count[country] += 1
            # If the country is not in the dictionary, add it with a count of 1
            else:
                gold_medal_count[country] = 1

# Sort the dictionary by the count of gold medals in descending order
sorted_gold_medal_count = sorted(gold_medal_count.items(), key=lambda x: x[1], reverse=True)

# Print the country and the count of gold medals
for country, count in sorted_gold_medal_count:
    print(f"{country}: {count} gold medals")