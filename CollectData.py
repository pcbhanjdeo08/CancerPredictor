class CollectData(object):
    """description of class"""


# streamlit_app.py
import streamlit as st

from CheckCancerProbability import CheckCancerProbability

st.title("Corelation of cancer with microplastic")
st.write("This is an interactive webpage built with Python to show correlation between cancer and microplastic.")

text_microplastic_index = st.number_input("Enter microplastic_index")
text_pm25 = st.number_input("Enter pm25")
text_inflammation_index = st.number_input("Enter minflammation_index")
text_exposure_years = st.number_input("Enter exposure_years")

# create a placeholder directly beneath the button
placeholder = st.empty()

def calculateprobability():
    my_array = [text_microplastic_index, text_pm25, text_inflammation_index, text_exposure_years]
    result = CheckCancerProbability(my_array)
    # store result so it persists across reruns
    st.session_state['cancer_result'] = result

st.button("Calculate Cancer Probability", on_click=calculateprobability)

# show the result directly beneath the button
if 'cancer_result' in st.session_state:
    placeholder.write(st.session_state['cancer_result'])



