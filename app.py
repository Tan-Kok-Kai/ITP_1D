import streamlit as st 
import mylibrary # The logic for the calculation is stored in functions in mylibrary.py 
## User Interface ---------------------------------------------------------------------
## This file shows you streamlit code for two parts.
## Data Entry - how to make widgets to get the user inputs. 
## Calculation - how to get the result from the user inputs. 
## ------------------------------------------------------------------------------------


## Data Entry -------------------------------------------------------------------------
## Shows you the code to 
## 1) write a text on the screen
## 2) obtain a number input from the user using a box
## 3) obtain a number input from the user using a slider
## 4) allow user to select one out of several choices using a radio button
## The key attribute enables you to retrieve the data entered for that widget from st.session_state 
## ------------------------------------------------------------------------------------


st.write("Tales of Lanfang Tickets")
# Create one number box per ticket type by looping over the PRICES dictionary.
# The user's answers are stored in counts, e.g. {"adult": 2, "child": 1, "senior": 0, "student": 0}.
# Adding a new ticket type to PRICES automatically adds a new box here.
counts = {}
for category in mylibrary.PRICES:
    #ask senior seperately and stop the creation of senior ticket box
    if category=="senior":
        continue
    counts[category]=st.number_input(f"{category.title()} Tickets", 
                                     min_value=0, 
                                     max_value=10, 
                                     step=1) 
#only show the senior input box if there is at least one adult ticket bought
if counts["adult"]>0:
    st.session_state["seniors"] = min(st.session_state.get("seniors", 0), counts["adult"]) #session state to store number of seniors
    seniors=st.number_input("How many of the adults are above 60 years old?",
                        min_value=0,
                        max_value=counts["adult"],
                        step=1,
                        key="seniors")
else:
    seniors=0
# Tell the user straight away if their group qualifies for the family discount.                                   
if mylibrary.is_family(counts["adult"]-seniors, counts["child"]):
    st.write("You are eligible for a family discount of 10%")
# Slider for the number of audio guides (0 to 3).
guides=st.slider("How many audio guides do you want to rent?",
                    min_value=0, 
                    max_value=3, 
                    step=1)
# Radio button to choose peak or off-peak tickets.
ticket_type=st.radio("Type of Ticket", ["Peak", "Off-Peak"])
# The receipt is only calculated after the user clicks the button.
if st.button("Get Total"):
    visitors= sum(counts.values())
    # Input validation: a booking needs at least one ticket.
    if visitors==0:
        st.warning("Please buy at least one ticket")
    else:
        #Move the old adults to seniors
        counts["senior"]=seniors
        counts["adult"]-= seniors
         # ticket_type == "Peak" gives True or False, which is passed in as peak.
        rows, total=mylibrary.build_receipt(counts,
                                            peak=ticket_type=="Peak",
                                            guides=guides)
# Show the itemised receipt as a table, then the total price.
        st.subheader("Receipt")
        st.table(rows)
        st.write(f"Total Price: ${total:.2f}")












# a = st.number_input("Number of adults", min_value=0, max_value=10, step=1, key="adults")
# b = st.number_input("Number of children", min_value=0, max_value=10, step=1, key="children")
# if mylibrary.is_family(a,b):
#     st.write("You are eligible for a family discount of 10%")
# st.slider("How many audio guides do you want to rent?", min_value=0, max_value=3, step=1, key="rental")

# ## Code is written here to show you how a radio button works
# ticket_type = st.radio( 
#     label = "Type of Ticket",
#     options = ["Peak", "Off-Peak"]
# )
# st.write("Ticket Type Selected: ", ticket_type)


# ## Calculation -------------------------------------------------------------------------
# ## Shows you the code to 
# ## 1) declare a button and detect if it is clicked through the if-statement 
# ## 2) obtain the user's inputs from the respective widgets using st.session_state 
# ## 3) call the functions in mylibrary.py to get the result
# ## 4) display the outcome in a streamlit table using a python dictionary 
# ## ------------------------------------------------------------------------------------ 
# # if st.button('Get Total'):
# st.write('Calculating Your Total ...')
# adults = st.session_state.adults
# children = st.session_state.children 
# rental = st.session_state.rental 
# adults_price, children_price = mylibrary.calculate_total(adults,children, peak=ticket_type == "Peak")
# guides_cost = mylibrary.audio_guides(st.session_state.rental)
# total_price = adults_price + children_price + guides_cost
# data = {"Total Price for Adults": adults_price,
#         "Total Price for Children": children_price, 
#         "ticket_type": ticket_type,
#         "audio_guides cost": guides_cost,
#         "Total you have to pay": total_price
#         }
# st.table(data)
# # else:
# #     st.write('Please Key In The Quantity')