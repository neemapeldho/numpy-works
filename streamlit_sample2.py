import streamlit

expense = []

amount = []

exp = streamlit.text_input("enter the item : ")

amt = streamlit.text_input("enter the amount : ")

if streamlit.button("Add expense"):

    expense.append(exp)
    amount.append(int(amt))

print(sum(amount))

if streamlit.button("Total expense"):
    
    streamlit.success(sum(amount))

