# A customer of a grocery store is purchasing 6 items. The names and prices of the items are as follows:
#	1. Penne 16 oz Pack of 12 - $16.68
#	2. Arrabiata Pasta Sauce 24 oz - $6.98
#	3. Bag of 20 Organic Garlic Cloves - $16.78
#	4. Italian Seasoning 1.5 oz Bottle - $15.26
#	5. Artisan Baguettes Twin Pack - $3.00
#	6. 12 oz Bag of Meatballs - $4.39
# In a .py file, write a program which calculates the subtotal of all 6 of these items using an expression.  The subtotal is just the sum of all of their prices.
# Use print() to display the result of the expression with round.

penne_12pack = 16.68
pasta_24oz = 6.98
organic_clove_20 = 16.78
italian_season_bottle = 15.26
baguettes_twin_pack = 3.00
meat_balls_12oz = 4.39

print(round(penne_12pack + pasta_24oz + organic_clove_20 + italian_season_bottle + baguettes_twin_pack + meat_balls_12oz, 2))