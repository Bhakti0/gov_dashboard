import streamlit as st
import pandas as pd
import random
import datetime
import sys, os


current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir))
sys.path.append(project_root)


try:
    from governance_tool import governance_decision
except ModuleNotFoundError:
    st.error("⚠ governance_tool.py not found! Please place it in the SAME folder as this file.")
    st.stop()


st.title("AI Governance Control Panel")

prompt = st.text_area("Enter Prompt for Governance Check:")

if st.button("Evaluate"):
    result = governance_decision(prompt)
    st.subheader("Governance Evaluation Result")
    st.json(result)


st.subheader("Simulated Risk Trend")
df = pd.DataFrame({
    "timestamp": [datetime.datetime.now().timestamp() - i*60 for i in range(20)],
    "risk": [random.randint(10, 90) for _ in range(20)]
})
st.line_chart(df.set_index("timestamp"))
