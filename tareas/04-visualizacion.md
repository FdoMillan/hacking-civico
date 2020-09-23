import altair as alt 
import pandas as pd 
import seaborn as sns
from vega_datasets import data

data = sns.utils.load_dataset('penguins')
data.head()

plot_agricola1 = alt.Chart(empleos).mark_area(size = 2, point={"filled": True, "fill": "red"}, color='black').encode(
    x = alt.X( "month:T", title=""), 
    y = alt.Y("nonfarm_change:Q", title = "Sector no agricola EEUU")
   ).properties(width=650, title = "Cambio en el sector no-agrícola de Estados Unidos vs año")


plot_agricola2 = alt.Chart(empleos).mark_line(size = 2, point={"filled": False, "fill": "black"}, color='black').encode(
    x = alt.X( "month:T", title=""), 
    y = alt.Y("nonfarm_change:Q", title = "Sector no agricola EEUU")
   ).properties(width=650, title = "Cambio en el sector no-agrícola de Estados Unidos vs año")
 

plotp1 = alt.Chart(data).mark_bar().encode(
    x = alt.X("mean(flipper_length_mm)", title = "longitud promedio de aleta (mm)"),
    y = alt.Y("species" , title = "Especie"),
   color = alt.Color('species'),
    )
    
 plotp2 = alt.Chart(data).mark_text(size = 20, align='right').encode(
    x = alt.X("mean(flipper_length_mm)"),
    y = alt.Y("species"),
    text = alt.Text("species")
    )
