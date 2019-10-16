import streamlit as st
import plotly.figure_factory as ff
import numpy as np

# API: https://streamlit.io/docs/api.html#

st.title('Malt Distillery')

st.header('Operations')

#preconfigured = st.sidebar.selectbox(label='Distillery', options=('New','The Glenlivet','The Macallan'), index=0)

operating_weeks_year = st.slider(label='Operating weeks year:', min_value=0, max_value=52, value=48, step=1,format=None)
liter_tonne_malt = st.slider(label='Litre per Te malt:', min_value=350, max_value=450, value=405, step=5,format=None)
mlpa_year = st.slider(label='Million Litres Pure Alcohol per year:', min_value=0.0, max_value=15.0, value=10.0, step=0.1,format=None)
lpa_year = mlpa_year * 10**6
malt_tonne_year = lpa_year / liter_tonne_malt

# F-type style formatting of float f'{malt_tonne_year:.2f}'

st.subheader('Summary')

st.write('Malt per year (Te):', int(malt_tonne_year))

st.header('Mashing')
mash_tun_number = st.selectbox(label='Mash Tun number:', options=(1,2), index=0)

malt_tonne_week = malt_tonne_year / operating_weeks_year
mashes_week = st.slider(label='Mashes per week:', min_value=0, max_value=50, value=40, step=1,format=None)
liquor_grist_ratio = st.slider(label='Liquor to Grist ratio:', min_value=2.0, max_value=5.0, value=4.0, step=0.1,format=None)

malt_charge = malt_tonne_week / mashes_week / mash_tun_number
wort_volume_week = malt_tonne_week * liquor_grist_ratio

st.write('Malt Charge (Te):', int(malt_charge))
st.write('Wort volume (m3) per week:', int(wort_volume_week))

if malt_charge > 20 or malt_charge < 0:
    st.error('There is an error')
    
if st.checkbox(label='Advanced', value=False):
    mashes_week = st.slider(label='Mashes per week:', min_value=0, max_value=20, value=5, step=1,format=None)
    mashes_week = st.slider(label='Mashes per week:', min_value=0, max_value=20, value=5, step=1,format=None)

st.header('Fermentation')

fermenter_number = st.slider(label='Washbacks:', min_value=1, max_value=50, value=14, step=1,format=None)
fermenter_volume = st.slider(label='Washback Volume (m3):', min_value=1, max_value=100, value=60, step=1,format=None)
fermentation_time = st.slider(label='Fermentation Time (h):', min_value=20, max_value=120, value=65, step=1,format=None)

hours_week = 24 * 7 # 168
fermentations_week = hours_week / fermentation_time 
fermentation_capacity_week = (fermenter_number * fermentations_week) * fermenter_volume
st.write('Fermentation capacity (m3) per week:', int(fermentation_capacity_week))

if wort_volume_week > fermentation_capacity_week:
    st.error('There is an error')

if st.checkbox(label='Advanced', value=False):
    pass

st.header('Distillation')

st.subheader('Wash stills')
wash_still_number = st.slider(label='Wash stills:', min_value=1, max_value=30, value=6, step=1,format=None)
wash_still_volume = st.slider(label='Wash Still Volume (m3):', min_value=1, max_value=30, value=10, step=1,format=None)

st.subheader('Spirit stills')
spirit_still_number = st.slider(label='Spirit stills:', min_value=1, max_value=30, value=6, step=1,format=None)
spirit_still_volume = st.slider(label='Spirit Still Volume (m3):', min_value=1, max_value=30, value=10, step=1,format=None)

if st.checkbox(label='Advanced', value=False):
    pass

#st.header('Utilities')

#st.header('Production Schedule')

st.button('Save')