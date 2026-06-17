import streamlit as st
from graph.workflow import graph

# Page Config
st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    page_icon="🔍",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("🤖 Multi-Agent Research Assistant")

    st.markdown("""
    ### Agents

    - 📋 Planner Agent
    - 🔍 Research Agent
    - 📝 Summarizer Agent
    - ✅ Fact Checker Agent
    - 📄 Report Writer Agent
    """)

    st.markdown("---")

    st.info(
        "Powered by LangGraph, Groq, Tavily Search, and Streamlit"
    )

# Main Title
st.title("🔍 Multi-Agent Research Assistant")

st.markdown(
    "Generate professional research reports using a team of AI agents."
)

# Query Input
query = st.text_area(
    "Enter Research Topic",
    placeholder="Example: Analyze the impact of AI Agents on Software Engineering Jobs"
)

# Run Button
if st.button("🚀 Start Research", use_container_width=True):

    if not query.strip():
        st.warning("Please enter a research topic.")
        st.stop()

    with st.spinner("Agents are researching..."):

        try:

            result = graph.invoke(
                {
                    "query": query
                }
            )

            st.success("Research Completed Successfully!")

            # Metrics
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Agents Used", "5")

            with col2:
                st.metric("Workflow", "LangGraph")

            with col3:
                st.metric("Status", "Complete")

            st.markdown("---")

            # Agent Workflow Viewer
            with st.expander("🤖 Agent Workflow"):
                st.write("✅ Planner Agent")
                st.write("✅ Research Agent")
                st.write("✅ Summarizer Agent")
                st.write("✅ Fact Checker Agent")
                st.write("✅ Report Writer Agent")

            # Tabs
            tab1, tab2, tab3, tab4, tab5 = st.tabs(
                [
                    "📋 Plan",
                    "🔍 Research",
                    "📝 Summary",
                    "✅ Fact Check",
                    "📄 Final Report"
                ]
            )

            # Plan
            with tab1:
                st.markdown(
                    result.get(
                        "plan",
                        "No plan generated."
                    )
                )

            # Research
            with tab2:
                st.markdown(
                    result.get(
                        "research",
                        "No research findings available."
                    )
                )

            # Summary
            with tab3:
                st.markdown(
                    result.get(
                        "summary",
                        "No summary generated."
                    )
                )

            # Fact Check
            with tab4:
                st.markdown(
                    result.get(
                        "fact_check",
                        "No fact-check results available."
                    )
                )

            # Final Report
            with tab5:

                report = result.get(
                    "report",
                    "No report generated."
                )

                st.markdown(report)

                st.download_button(
                    label="📥 Download Report",
                    data=report,
                    file_name="research_report.md",
                    mime="text/markdown",
                    use_container_width=True
                )

        except Exception as e:

            st.error("An error occurred while running the research workflow.")

            st.exception(e)
