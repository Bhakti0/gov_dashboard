import os
import sys
import subprocess


PROJECT_PATH = r"D:\Full_AI_Governance_All_Deliverables"


os.chdir(PROJECT_PATH)

print("✅ Project directory switched to:")
print(PROJECT_PATH)

try:
    import streamlit
except ImportError:
    print("⚠ Streamlit not found. Installing now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit"])


print("\n🚀 Launching AI Governance Dashboard...\n")
subprocess.Popen(["streamlit", "run", "advanced_streamlit_app.py"], shell=True)
