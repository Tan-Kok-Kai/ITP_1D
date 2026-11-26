# Business Logic ---------------------------------------------------------------------
# This file stores functions that implement the business logic.
## ------------------------------------------------------------------------------------

# calculate_total function takes in the number of adults and children and returns the total price.
# at peak hours, the prices are 1.5 times the normal price.
# it returns the total price for adults and children separately
PRICES={"adult":10, "child":5, "senior":6}
AUDIO_GUIDE_PRICE=3
PEAK_MULTIPLIER=1.5
FAMILY_DISCOUNT=0.9 # 10% discount for families (Must be 2 adult and at least 1 child)

# is_family takes in the number of adults and children.
# It returns True if the group qualifies as a family (exactly 2 adults and at least 1 child),
# otherwise False.
def is_family(adults,children):
    return adults == 2 and children >= 1

# get_multiplier takes in whether the booking is at peak time.
# It returns the number that every ticket price is multiplied by:
# 1.5 during peak hours, 1 (no change) otherwise.
def get_multiplier(peak):
    multiplier=1
    if peak:
        return PEAK_MULTIPLIER
    return multiplier

# audio_guides function takes in the number of items and returns the total price.
def audio_guides(items): 
    return items * AUDIO_GUIDE_PRICE
# build_receipt takes in:
#   counts - a dictionary of ticket counts, e.g. {"adult": 2, "child": 1, "senior": 0, "student": 0}
#   peak   - True if the tickets are for peak hours
#   guides - the number of audio guides rented
# It returns two values:
#   rows  - a list of dictionaries, one per receipt line (each dictionary becomes a table row)
#   total - the total price of the whole booking
def build_receipt(counts, peak , guides):
    multiplier= get_multiplier(peak)
    family=is_family(counts["adult"], counts["child"])
    rows=[]
    total=0
     # Go through every ticket type in PRICES and add a receipt line for each one bought.
    for category in PRICES:
        quantity=counts[category]
        if quantity>0:
            unit_price=PRICES[category]*multiplier
            if family and category in ["adult", "child"]:
                unit_price*=FAMILY_DISCOUNT
            subtotal=quantity*unit_price
            rows.append({"Item":category.title() + " ticket", 
                         "quantity":quantity, 
                         "unit_price":f"${unit_price:.2f}", 
                         "subtotal":f"${subtotal:.2f}"})
            total+=subtotal
    #ignore if it is not bought
    if guides>0:
        guide_cost=audio_guides(guides)
        rows.append({"Item":"Audio Guide",
                        "quantity":guides,
                        "unit_price":f"${AUDIO_GUIDE_PRICE:.2f}",
                        "subtotal":f"${guide_cost:.2f}"})
        total+=guide_cost
    return rows, total



