# Review Analyzer ACME

Welcome to **Review Analyzer ACME** – a simple, powerful tool for analyzing customer reviews and extracting actionable insights. This project combines a Python backend for data processing with an interactive frontend for visualizing and exploring review sentiment.

## Features

- **Automated Sentiment Analysis:** Quickly determine the sentiment of customer reviews (positive, negative, neutral).
- **Cleaned Sample Data:** Includes pre-processed review datasets for easy experimentation.
- **Interactive Frontend:** User-friendly interface for uploading data, running analyses, and viewing results.
- **Extensible Backend:** Modular Python backend for easy customization and integration.

## Project Structure

backend/
main.py # Core backend logic for data processing and sentiment analysis
data/
cleaned_file.csv # Cleaned review data
sample_reviews.csv # Raw sample reviews
frontend/
app.py # Streamlit app for the frontend interface
requirements.txt # Python dependencies


## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/NicholasTheGeek/review-analyzer-acme.git
   cd review-analyzer-acme
Install dependencies:
bash
Copy Code
pip install -r requirements.txt
Run the backend:
bash
Copy Code
python backend/main.py
Launch the frontend:
bash
Copy Code
streamlit run frontend/app.py
Explore the app:
Open your browser and go to http://localhost:8501 to start analyzing reviews!
Usage
Upload your own CSV file of reviews or use the provided sample data.
View sentiment analysis results and summary statistics.
Download cleaned and analyzed data for further use.
Demo
Check out our YouTube walkthrough for a full demo!

Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

License
MIT
