class CollectData(object):
    """description of class"""


    # streamlit_app.py
import streamlit as st

from CheckCancerProbability import CheckCancerProbability

st.title("My Streamlit Web App")
st.write("This is an interactive webpage built with Python.")

# Add a button and handle the interaction
# Pseudocode / Plan (detailed):
# 1. Remove the Streamlit app code that was accidentally placed inside `CancerPredictorPython\CollectData.py`.
# 2. Ensure `CollectData` is a simple, well-formed class definition with no stray top-level indented blocks.
# 3. Create a separate `streamlit_app.py` (shown below) that imports `CollectData` or `CheckCancerProbability`
#    correctly with no leading spaces before `import` statements.
# 4. Use absolute import: `from CancerPredictorPython.CheckCancerProbability import CheckCancerProbability`
#    at the top of `streamlit_app.py`.
# 5. Verify no unexpected indentation remains (no leading spaces before `import` at top level).
# 6. Provide corrected contents for both `CollectData.py` and `streamlit_app.py` so you can replace files directly.
if st.button("Click Me"):
    st.write("Button clicked!")

    
    my_array = [50, 80, 40, 10]
    result = CheckCancerProbability(my_array)
    st.write(result)

st.write("Hello world")
