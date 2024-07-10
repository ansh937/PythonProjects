import plotly.express as px
#px.data.medals_long() this is the default dataset given by plotly
df = px.data.medals_long()

fig = px.bar(df, x="medal", y="count", color="nation",
            pattern_shape="nation", pattern_shape_sequence=[".", "x", "+"])
fig.show()


import plotly.express as px
df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
fig = px.pie(df, values='pop', names='country', title='Population of European continent')
fig.show()