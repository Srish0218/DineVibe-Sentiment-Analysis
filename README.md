# FlareDineSentiment

## Overview

FlareDineSentiment is a sophisticated project centered around the realm of sentiment analysis applied to restaurant reviews using advanced Natural Language Processing (NLP) techniques. This application serves as a powerful tool for users to gain insights into the sentiments expressed in restaurant reviews, aiding in the understanding of customer experiences. The heart of the system lies in its ability to predict sentiments, categorizing reviews as either positive or negative, through the utilization of a meticulously trained machine learning model.
## Features
- **User Authentication:** Ensure secure access to the sentiment analysis functionality.
- **Section Selection:** Choose between analyzing one-line or multi-line reviews, or import reviews from an Excel file.
- **Sentiment Analysis:** The application predicts sentiment (Positive/Negative) of restaurant reviews.
- **Visualization:** Visualizes rating and sentiment distribution using line and pie charts.
- **Multi-Review Support:** Supports both one-line and multi-line reviews for analysis.
- **Rating Prediction:** In addition to sentiment, the application estimates a rating (out of 5) for each review.
- **Interactive Word Cloud:** Displays an interactive word cloud highlighting frequently used words in reviews.
- **Review Filtering:** Users can filter reviews based on sentiment and rating.
- **Adjustable Chart Width and Height:** Tailor the visualizations to your preference.

## Installation

### Prerequisites

- Python 3.6 or later

### Setup

1. Clone the repository:

```bash
git clone https://github.com/Srish0218/FlareDineSentiment
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```
## Adding Reviews
**One-Line Reviews**
- Select "One-Line Reviews" in the app.
- Enter each one-line review on a new line in the text area.
- Click "Predict Sentiments" to analyze the reviews.

**Multi-Line Reviews**
- Select "Multi-Line Reviews" in the app.
- Enter multi-line reviews in the text area, separating each review with a new line.
- Click "Predict Sentiments" to analyze the reviews.

**Excel Import**
- Select "Import Excel File" in the app.
- Upload an Excel file containing the 'Review' column.
- Ensure the Excel file structure has two columns named 'Review' and 'Rating'.
- The app will process the reviews and provide sentiment predictions.

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Open your web browser and navigate to the provided URL to interact with the application.

1. **User Authentication:**
    - Enter the correct password ("Srish.18") to access the app.
2. **Select Section:**
   - Choose between "Line Reviews" or "Import Excel File" for analysis.
3. **Adjust Chart Dimensions:**
   - For line chart and pie chart visualizations, use sliders to adjust width and height.
4. **Input Reviews:**
   - Enter reviews either as one-liners or multi-line texts.
5. **Sentiment Analysis:**
   - Click the "Predict Sentiments" button to see the sentiment analysis results.

## File Structure

- app.py: Main Streamlit application script.
- b1_Sentiment_Analysis_Model.ipynb: Jupyter notebook for sentiment analysis model development.
- b2_Sentiment_Predictor.ipynb: Jupyter notebook for sentiment predictor development.
- c1_BoW_Sentiment_Model.pkl: Pickle file containing the Bag of Words (BoW) model.
- c2_Classifier_Sentiment_Model: Joblib file containing the trained classifier model.
- c3_Predicted_Sentiments_Results.tsv: TSV file containing the predicted sentiments results.
- a1_RestaurantReviews_HistoricDump.tsv: Sample dataset for testing.
- a2_RestaurantReviews_FreshDump.tsv: Fresh dataset for testing.
- Book1.xlsx: Sample Excel file for testing.

## Visualizations
1. **Rating Distribution:**
   - Visualizes the distribution of ratings using a line chart.
2. **Sentiment Distribution:**
   - Displays the distribution of sentiments using pie charts and bar charts.

## Built With
- Python
- Streamlit
- Scikit-learn
- NLTK
- Pandas
- Matplotlib
- Seaborn

## Additional Information
- The project uses NLTK for natural language processing.
- Machine learning models are trained on a historic dump of restaurant reviews.
- Built with Streamlit, pandas, scikit-learn, and seaborn.

## Contributors

- Srishti Jaitly: [GitHub](https://github.com/Srish0218)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Special thanks to [Streamlit](https://streamlit.io/) for the interactive app framework.
# DineVibe-Sentiment-Analysis
