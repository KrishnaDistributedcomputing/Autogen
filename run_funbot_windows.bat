:: Step 1: Clone the repository
git clone https://github.com/KrishnaDistributedcomputing/Autogen.git
cd Autogen

:: Step 2: Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

:: Step 3: Install dependencies
pip install autogen openai random

:: Step 4: Set the API key
set OPENAI_API_KEY=your_api_key_here

:: Step 5: Run the Python script
python funbot.py
