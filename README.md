# Black-Scholes Option Pricer

Interactive Black–Scholes option pricer built with Python and Streamlit. The app lets you:
- Input option parameters (spot, strike, time to maturity, volatility, risk‑free rate)
- See the resulting call and put prices

Main files:
- `BlackScholes.py` – core Black–Scholes pricing logic
- `streamlitapp.py` – Streamlit UI and visualization
- `requirements.txt` – Python dependencies

## Setup & Local Run

1. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv .venv
   # Windows (PowerShell)
   .venv\Scripts\Activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run streamlitapp.py
   ```

The app will open in your browser (or visit the URL shown in the terminal, usually http://localhost:8501).

## Deploying on Streamlit Community Cloud

1. Push this repository to GitHub.
2. Go to https://streamlit.io → **Sign in** → **New app**.
3. Select this GitHub repo and branch.
4. Set **Main file path** to:
   ```text
   streamlitapp.py
   ```
5. Click **Deploy**.

After the first build, Streamlit will give you a public URL for your live app.

The URL generated should be: https://interactive-black-scholes.streamlit.app/

