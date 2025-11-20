import streamlit
import seaborn
import pandas
from matplotlib import pyplot

data = {
    "students" : ["arun","ram","anu"],
    "maths" : [80,90,87],
    "science" : [75,67,54]
}

pyplot.figure(figsize=(3,3)) # Create a new figure, or activate an existing figure

# as streamlit needs a single image object to display we use figure()
# using this we can adjust the size,layout

seaborn.barplot(data = data, x = "students" , y = "science",color= "yellow")
streamlit.pyplot(pyplot)
seaborn.barplot(data = data, x = "students" , y = "maths",palette= "coolwarm")
streamlit.pyplot(pyplot)