import streamlit

expense = []

amount = []

exp = streamlit.text_input("enter the item : ")

amt = streamlit.number_input("enter the amount : ")

if streamlit.button("Add expense"):

    expense.append(exp)
    amount.append(amt)

print(sum(amount))

if streamlit.button("Total expense"):

    result = 0 

    for i in amount :
         result += i 
    
         streamlit.success(sum(result))
         exit()
