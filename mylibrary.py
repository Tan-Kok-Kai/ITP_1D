# Business Logic ---------------------------------------------------------------------
# This file stores functions that implement the business logic.
## ------------------------------------------------------------------------------------

# calculate_total function takes in the number of adults and children and returns the total price.
# at peak hours, the prices are 1.5 times the normal price.
# it returns the total price for adults and children separately
PRICES={"adult":10, "child":5, "senior":6, "student":7}
AUDIO_GUIDE_PRICE=3
PEAK_MULTIPLIER=1.5
FOREIGN_MULTIPLIER=1.2
FAMILY_DISCOUNT=0.9 # 10% discount for families (Must be 2 adult and at least 1 child)

def is_family(adults,children):
    return adults == 2 and children >= 1


def get_multiplier(adults,children,peak,foreign):
    multiplier=1
    if peak:
        multiplier*= PEAK_MULTIPLIER
    if foreign:
        multiplier*= FOREIGN_MULTIPLIER
    if is_family(adults,children):
        multiplier*= FAMILY_DISCOUNT
    return multiplier

def calculate_total( adults, children, peak=False):
    adult_price=PRICES["adult"]
    child_price=PRICES["child"]
    FAMILY_DISCOUNT = 0.9 # 10% discount for families (Must be 2 adult and at least 1 child)

    if peak:
        adult_price *= 1.5
        child_price *= 1.5
        
    if is_family(adults, children):
        adult_price *= FAMILY_DISCOUNT
        child_price *= FAMILY_DISCOUNT
    return adults * adult_price, children * child_price

# audio_guides function takes in the number of items and returns the total price.
def audio_guides(items): 
    return items * AUDIO_GUIDE_PRICE
def build_receipt(counts, peak, foreign , guides):
    multiplier= get_multiplier(counts["adult"],counts["child"],peak,foreign)
    rows=[]
    total=0
    for category in PRICES:
        quantity=counts[category]
        if quantity>0:
            unit_price=PRICES[category]*multiplier
            subtotal=quantity*unit_price
            rows.append({"Item":category.title() + " ticket", 
                         "quantity":quantity, 
                         "unit_price":f"${unit_price:.2f}", 
                         "subtotal":f"${subtotal:.2f}"})
            total+=subtotal
    if guides>0:
        guide_cost=audio_guides(guides)
        rows.append({"Item":"Audio Guide",
                        "quantity":guides,
                        "unit_price":f"${AUDIO_GUIDE_PRICE:.2f}",
                        "subtotal":f"${guide_cost:.2f}"})
        total+=guide_cost
    return rows, total



