# Business Logic ---------------------------------------------------------------------
# This file stores functions that implement the business logic.
## ------------------------------------------------------------------------------------

# calculate_total function takes in the number of adults and children and returns the total price.
# at peak hours, the prices are 1.5 times the normal price.
# it returns the total price for adults and children separately
def calculate_total( adults, children, peak=False):
    ADULT_PRICE = 10
    CHILD_PRICE = 5
    FAMILY_DISCOUNT = 0.9 # 10% discount for families (Must be 2 adult and at least 1 child)

    if peak:
        ADULT_PRICE *= 1.5
        CHILD_PRICE *= 1.5
        
    if adults == 2 and children >= 1:
        ADULT_PRICE *= FAMILY_DISCOUNT
        CHILD_PRICE *= FAMILY_DISCOUNT
    return adults * ADULT_PRICE, children * CHILD_PRICE

# audio_guides function takes in the number of items and returns the total price.
def audio_guides(items): 
    PRICE_PER_ITEM = 3
    return items * PRICE_PER_ITEM

