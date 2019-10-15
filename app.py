import streamlit as st

# API: https://streamlit.io/docs/api.html#

st.title('Distillery Calculator')

st.header('Operations')

operating_weeks_year = st.slider(label='Operating weeks year:', min_value=0, max_value=52, value=48, step=1,format=None)
liter_tonne_malt = st.slider(label='Litre per Te malt:', min_value=350, max_value=450, value=400, step=5,format=None)
mlpa_year = st.slider(label='Million Litres Pure Alcohol per year:', min_value=0.0, max_value=15.0, value=10.0, step=0.1,format=None)
lpa_year = mlpa_year * 10**6
malt_tonne_year = lpa_year / liter_tonne_malt

# F-type style formatting of float f'{malt_tonne_year:.2f}'

st.subheader('Summary')

st.write('Tonne of malt per year:', int(malt_tonne_year))

st.header('Mashing')
mash_tun = st.selectbox(label='Mash Tun number:', options=(1,2), index=0)

malt_tonne_week = malt_tonne_year / operating_weeks_year
mashes_week = st.slider(label='Mashes per week:', min_value=0, max_value=20, value=5, step=1,format=None)
malt_charge = malt_tonne_week / mashes_week 

if malt_charge > 15 or malt_chart < 0:
    st.error('There is an error')

st.write('Malt Charge (Te):', int(malt_charge))

st.header('Fermentation')

st.header('Distillation')