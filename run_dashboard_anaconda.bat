@echo off
echo ============================================
echo   LAUNCHING AI GOVERNANCE DASHBOARD (ANACONDA)
echo ============================================
echo.


call C:\Users\User\anaconda3\Scripts\activate.bat


cd /d "D:\Full_AI_Governance_All_Deliverables\src"

echo ✅ Starting Streamlit using Anaconda Python...
echo.

python -m streamlit run advanced_streamlit_app.py

pause
