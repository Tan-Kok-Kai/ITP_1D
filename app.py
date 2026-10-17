import streamlit as st 

## The logic for the calculation is stored in functions in mylibrary.py 
import mylibrary

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
a = st.number_input("Number of adults", min_value=0, max_value=10, step=1, key="adults")
b = st.number_input("Number of children", min_value=0, max_value=10, step=1, key="children")
if a == 2 and b >= 1:
    st.write("You are eligible for a family discount of 10%")
st.slider("How many audio guides do you want to rent?", min_value=0, max_value=3, step=1, key="rental")

## Code is written here to show you how a radio button works
ticket_type = st.radio( 
    label = "Type of Ticket",
    options = ["Peak", "Off-Peak"]
)
st.write("Ticket Type Selected: ", ticket_type)


## Calculation -------------------------------------------------------------------------
## Shows you the code to 
## 1) declare a button and detect if it is clicked through the if-statement 
## 2) obtain the user's inputs from the respective widgets using st.session_state 
## 3) call the functions in mylibrary.py to get the result
## 4) display the outcome in a streamlit table using a python dictionary 
## ------------------------------------------------------------------------------------ 
# if st.button('Get Total'):
st.write('Calculating Your Total ...')
adults = st.session_state.adults
children = st.session_state.children 
rental = st.session_state.rental 
adults_price, children_price = mylibrary.calculate_total(adults,children, peak=ticket_type == "Peak")
guides_cost = mylibrary.audio_guides(st.session_state.rental)
total_price = adults_price + children_price + guides_cost
data = {"Total Price for Adults": adults_price,
        "Total Price for Children": children_price, 
        "ticket_type": ticket_type,
        "audio_guides cost": guides_cost,
        "Total you have to pay": total_price
        }
st.table(data)
# else:
#     st.write('Please Key In The Quantity')