import streamlit as st
import pandas as pd
import requests
import csv
import io
import os

# Ensure the data directory exists
os.makedirs("data", exist_ok=True)

# Set custom page configuration
st.set_page_config(page_title="🛒 Product Review Analyzer", layout="wide")

# Custom title with markdown for styling
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>🛒 Acme Product Review Analyzer</h1>",
    unsafe_allow_html=True
)

# File uploader section
st.markdown("### 📂 Upload Your CSV File")
uploaded_file = st.file_uploader(
    "Upload a CSV file with product reviews (must include 'product_name' and 'review_text' columns).",
    type=["csv"]
)

# File processing logic
if uploaded_file:
    clean_rows = []
    expected_column_count = 3  # Adjust this to match your CSV

    # Use StringIO to read the uploaded file
    file_content = io.StringIO(uploaded_file.getvalue().decode("utf-8"))
    reader = csv.reader(file_content)
    for row in reader:
        if len(row) == expected_column_count:
            clean_rows.append(row)

    # Save the cleaned data to a temporary file
    cleaned_file_path = "data/cleaned_file.csv"
    with open(cleaned_file_path, "w", newline="", encoding="utf-8") as output_file:
        writer = csv.writer(output_file)
        writer.writerows(clean_rows)

    # Read cleaned data
    df = pd.read_csv(cleaned_file_path)

    # Check for required columns
    required_columns = {"product_name", "review_text"}
    if not required_columns.issubset(df.columns):
        st.error("The uploaded CSV file must include 'product_name' and 'review_text' columns.")
        st.stop()

    # Display the uploaded file
    st.markdown("### 📝 Uploaded Reviews")
    st.dataframe(df)

    # Initialize results list
    results = []

    # Analyze reviews
    with st.spinner("🔍 Analyzing reviews... Please wait."):
        for _, row in df.iterrows():
            review_text = row["review_text"]
            try:
                # Send review text to the backend for analysis
                res = requests.post("http://localhost:8000/analyze/", data={"text": review_text})
                res.raise_for_status()
                data = res.json()

                # Append the result
                results.append({
                    "product_name": row["product_name"],
                    "review_text": review_text,
                    **data
                })
            except requests.exceptions.RequestException as e:
                st.error(f"Error analyzing review: {e}")
                continue

    # Convert results into a DataFrame
    result_df = pd.DataFrame(results)

    # Display results
    st.markdown("### ✅ Analysis Results")
    st.dataframe(result_df)

    # Download button for results
    st.download_button(
        label="💾 Download Results as CSV",
        data=result_df.to_csv(index=False),
        file_name="analysis_results.csv",
        mime="text/csv"
    )

    # Sentiment distribution visualization
    st.markdown("### 📊 Sentiment Distribution")
    st.bar_chart(result_df["sentiment"].value_counts())

    # Topic frequency visualization
    st.markdown("### 📌 Most Discussed Topics")
    cleaned_topics = result_df["topic"].str.strip().str.title()
    st.bar_chart(cleaned_topics.value_counts())
else:
    st.info("Please upload a CSV file to proceed.")

# Footer for additional styling
st.markdown(
    "<hr style='border: 1px solid #ccc;'/>"
    "<p style='text-align: center;'>© 2025 Acme Inc. All rights reserved.</p>",
    unsafe_allow_html=True
)