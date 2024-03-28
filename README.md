# MoodMunchInsights Analyser


> **Project Database Update:**
> 
> This project is currently doesn't utilize any database and performs optimally. For those interested in using MySQL with Workbench, kindly wait as I will be using database gor restaurant owner to login, kindly wait navigate to [EpicureGlow Sentiment Analysis](https://github.com/Srish0218/EpicureGlowSentiment). Database is added but facing issues in deploying, presently it is in streamlit but will use flask and mysql.
>
>The project is currently undergoing enhancements, primarily focusing on transitioning to MySQL for improved scalability and additional features. While the core logic remains unchanged, this update aims to provide a more robust and versatile solution.
>
>**Key Upgrades and Features in Progress:**
>
>- **Database:** Adding MySQL for enhanced performance and scalability.
>- **Transition of framework**: Migrating from streamlit to flask.
>- **Security Algorithms:** Implementing advanced security measures to safeguard sensitive data.
>- **Customer Login Provision:** Enabling customers to utilize the web app for exploring local restaurants, reading reviews, and contributing their feedback.
>- **Streamlined Data Input:** Restaurant owners are encouraged to provide review and rating data in Excel format for a seamless integration process.
>
>**Future Plans:**
>EpicureGlow Sentiment Analysis will not only adhere to the current logic but also introduce new features and capabilities. These include a MySQL database, advanced security measures, and a customer login portal for an enriched user experience.
> 
>We appreciate your patience and understanding as we work diligently to bring you an improved and feature-rich sentiment analysis solution.
>For more details, feel free to explore the more project on [GitHub](https://github.com/Srish0218/).
>
>Thank you for your continued support.
>
>Best regards,


MoodMunchInsights Analysis is a Streamlit-based web application designed for restaurant owners to analyze and visualize customer sentiments based on reviews. The application employs Natural Language Processing (NLP) techniques to determine sentiments and provides insightful visualizations.

## Overview

This project comprises a Streamlit-based web application, consisting of authentication functionality for restaurant owners, sentiment analysis, and visualization of customer reviews. The sentiment analysis is powered by a Bag of Words model and a classifier trained on customer reviews.

## Features

- Sentiment analysis of customer reviews.
- Visualizations of sentiment distribution and rating trends.
- Multi-line and Excel file review import options.

## Installation

To run the DineVibe Sentiment Analysis application, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/Srish0218/MoodMunchInsights.git
cd MoodMunchInsights-Analysis
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv myvenv
# On Mac, use : source venv/bin/activate
# On Windows, use: myvenv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

## How to Add Reviews and Tips

### Single-Line/Multi-Line Reviews

1. Navigate to the "Line Reviews" section.
2. Choose the review type (single-line or multi-line) from the dropdown.
3. Enter your reviews in the text area, with each review on a new line.
4. Optionally, show instructions for adding reviews.
5. Click the "Predict Sentiments" button to perform sentiment analysis.

### Excel File Import

1. Navigate to the "Import Excel File" section.
2. Upload an Excel file containing "Review" and "Rating" columns.
3. Ensure the Excel file structure has two columns named "Review" and "Rating."
4. The app will process the reviews and provide sentiment predictions.

## Usage


1. **Line Reviews**: Analyze sentiments of one-line or multi-line customer reviews. Enter reviews in the provided text area and click the "Predict Sentiments" button.

2. **Import Excel File**: Alternatively, import an Excel file with customer reviews and ratings. The app processes the data and provides sentiment predictions.

3. **Visualizations**: Explore visualizations such as rating distribution, sentiment distribution, and sentiment distribution in bar chart format.

## File Structure

The project structure is organized as follows:

```plaintext
MoodMunchInsights/
│
├── Book1.xlsx (Sample Excel file for importing reviews)
├── c1_BoW_Sentiment_Model.pkl (Bag of Words Sentiment Model)
├── c2_Classifier_Sentiment_Model (Classifier Sentiment Model)
├── app.py
└──requirements.tx
```


## Visualizations

1. ### Sentiment Distribution Pie Chart

The Sentiment Distribution Pie Chart provides a visual representation of the proportion of positive and negative sentiments in the reviews. Each section of the pie chart corresponds to a sentiment category, with the size of each section representing the percentage of reviews with that sentiment.

2. ### Sentiment Distribution Bar Chart

The Sentiment Distribution Bar Chart displays the count of positive and negative sentiments in the reviews using vertical bars. The x-axis represents the sentiment categories, while the y-axis represents the count of reviews. This chart allows for easy comparison between the number of positive and negative sentiments.

3. ### Rating Distribution Line Chart

The Rating Distribution Line Chart illustrates the distribution of ratings given by users. Each point on the line chart represents a rating value, and the corresponding y-value indicates the count of reviews with that rating. This visualization helps to understand the distribution of user ratings across different levels.

4. ### Sentiment Distribution Horizontal Bar Chart

The Sentiment Distribution Horizontal Bar Chart provides a horizontal representation of the count of positive and negative sentiments. Similar to the bar chart, this visualization makes it easy to compare the number of positive and negative sentiments, with the sentiment categories displayed on the y-axis and the count of reviews on the x-axis.

5. ### Sentiment Distribution Heatmap

The Sentiment Distribution Heatmap offers a comprehensive view of sentiment distribution across different rating levels. Each cell in the heatmap represents the count of reviews with a specific sentiment and rating combination. The color intensity of each cell indicates the count, with darker shades representing higher counts. This heatmap helps identify patterns and correlations between sentiment and rating levels.

---
## Demo

For a live demo, visit the [MoodMunch Insights App 🍽️😋](https://srish0218-moodmunchinsights.streamlit.app/) website.

---

Feel free to contribute to this project or report any issues by opening an [issue](https://github.com/Srish0218/MoodMunchInsights/issues) on GitHub. We welcome your feedback and contributions!

## License

This project is licensed under the [MIT License](LICENSE.md).

**Enjoy analyzing the sentiments of your restaurant's reviews with DineVibe!** 🍽️😋


















