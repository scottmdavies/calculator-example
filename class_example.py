import streamlit as st
import plotly.graph_objects as go

class Distillery:

    MLPA_label = "MLPA:"
    MLPA_min = 1
    MLPA_max = 20
    MLPA_step = 1
    MLPA_value = 10
    MLPA_type = "slider"

    OPERATING_WEEKS_label = "Operating Weeks:"
    OPERATING_WEEKS_min = 1
    OPERATING_WEEKS_max = 52
    OPERATING_WEEKS_step = 1
    OPERATING_WEEKS_value = 48
    OPERATING_WEEKS_type = "slider"


    def __init__(self, MLPA=MLPA_value, Operating_Weeks=OPERATING_WEEKS_value):
        self.MLPA = MLPA
        self.LPA = self.MLPA * 10**6
        self.Operating_Weeks = Operating_Weeks

class LauterTun:

    LPA_per_TE_label = "LPA per Te:"
    LPA_per_TE_min = 300
    LPA_per_TE_max = 450
    LPA_per_TE_step = 1
    LPA_per_TE_value = 405
    LPA_per_TE_type = "slider"

    def __init__(self, LPA_per_TE=LPA_per_TE_value):
        self.LPA_per_TE = LPA_per_TE


def main():
    create_distillery()
    create_mashing_plant()

def create_distillery():
    st.sidebar.header('Operation')
    MLPA = st.sidebar.slider(label=Distillery.MLPA_label,min_value=Distillery.MLPA_min,max_value=Distillery.MLPA_max,value=Distillery.MLPA_value,step=Distillery.MLPA_step)
    Operating_Weeks = st.sidebar.slider(label=Distillery.OPERATING_WEEKS_label,min_value=Distillery.OPERATING_WEEKS_min,max_value=Distillery.OPERATING_WEEKS_max, value=Distillery.OPERATING_WEEKS_value,step=Distillery.OPERATING_WEEKS_step)

    distillery = Distillery(MLPA=MLPA,Operating_Weeks=Operating_Weeks)
    st.write("LPA: ", distillery.LPA)

def create_mashing_plant():
    st.sidebar.header('Mashing')
    LPA_per_TE = st.sidebar.slider(label=LauterTun.LPA_per_TE_label,min_value=LauterTun.LPA_per_TE_min,max_value=LauterTun.LPA_per_TE_max,value=LauterTun.LPA_per_TE_value,step=LauterTun.LPA_per_TE_step)

    lautertun = LauterTun(LPA_per_TE=LPA_per_TE)
    st.write(lautertun.LPA_per_TE_label, lautertun.LPA_per_TE)


if __name__ == "__main__":
    main()