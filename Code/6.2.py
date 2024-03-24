menuprices = {
    'Salad': 300,
    'Samosa': 150,
    'Pasta': 200,
    'Biryani': 700,
    'Pav Bhaji': 150,
    'Misal Pav': 100,
    'Aloo Paratha': 250,
    'Chole Bhature': 300,
}
ratings = {
    'Salad': 4.0,
    'Samosa': 4.2,
    'Pasta': 3.8,
    'Biryani': 4.4,
    'Pav Bhaji': 2.9,
    'Misal Pav': 3.9,
    'Aloo Paratha': 4.3,
    'Chole Bhature': 4.8,
}

pricemorethan500 = {item: price for item, price in menuprices.items() if price > 500}
print("Items with price > 500:", pricemorethan500)

highest_rated = max(ratings, key=ratings.get)
print("Highest Rated item is:", highest_rated)

sortwithrating = sorted(ratings.items(), key=lambda item: item[1], reverse=True)
print("Menu items arranged in Highest to lowest rating:\n",sortwithrating)