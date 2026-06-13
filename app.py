import streamlit as st

from graph.workflow import graph

st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    layout="wide"
)

st.title("🔍 Multi-Agent Research Assistant")

query = st.text_input(
    "Research Topic"
)

if st.button("Start Research"):

    with st.spinner("Researching..."):

        result = graph.invoke(
            {
                "query": query
            }
        )

        st.subheader("Research Report")

        st.markdown(result["report"])
