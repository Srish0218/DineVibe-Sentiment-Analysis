# main_app.py
import pickle
import re
import joblib
import matplotlib.pyplot as plt
import nltk
import pandas as pd
import seaborn as sns
import streamlit as st
from nltk import PorterStemmer
from nltk.corpus import stopwords

# Add nltk data path
nltk.data.path.append("D:/Users/srish/PycharmProjects/MajorProject/SentimentAnalyzerApp/DineVibeSentiment/Lib/site-packages/nltk")

# Set pandas option
pd.set_option('mode.use_inf_as_na', True)

# Initialize PorterStemmer
ps = PorterStemmer()

# Disable deprecated warning for pyplot usage
st.set_option('deprecation.showPyplotGlobalUse', False)

# Download nltk stopwords
nltk.download('stopwords')

# Load BoW model
cv_file = 'c1_BoW_Sentiment_Model.pkl'
cv = pickle.load(open(cv_file, "rb"))

# Load classifier model
classifier_file = 'c2_Classifier_Sentiment_Model'
classifier = joblib.load(classifier_file)

# Load English stopwords
all_stopwords = stopwords.words('english')
all_stopwords.remove('not')  # Remove 'not' from stopwords


# Function to preprocess and predict sentiment
def analyze_sentiment(review):
    review = re.sub('[^a-zA-Z]', ' ', review).lower().split()
    review = [ps.stem(word) for word in review if word not in set(all_stopwords)]
    review = ' '.join(review)

    # Transform using BoW model
    input_transformed = cv.transform([review]).toarray()

    # Make prediction
    return classifier.predict(input_transformed)[0]


# Function to visualize rating distribution using line chart
def visualize_rating_distribution(df):
    width1 = 8
    height1=6
    fig, ax = plt.subplots(figsize=(width1, height1))
    sns.lineplot(x='Rating', y='Count', data=df.groupby('Rating').size().reset_index(name='Count'), ax=ax)
    plt.xlabel('Rating')
    plt.ylabel('Count')
    plt.title('Rating Distribution')
    st.pyplot(fig)


# Function to visualize sentiment distribution using bar chart
def visualize_sentiment_distribution_bar(df):
    chart_width = 8
    chart_height = 6
    fig, ax = plt.subplots(figsize=(chart_width, chart_height))
    sns.countplot(x='Sentiment', data=df, ax=ax)
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.title('Sentiment Distribution')
    st.pyplot(fig)

# Function to visualize sentiment distribution using pie chart
def visualize_sentiment_distribution_pie(df):
    fig1, ax1 = plt.subplots()
    ax1.pie(df['Sentiment'].value_counts(), labels=df['Sentiment'].unique(), autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Sentiment Distribution (Pie Chart)')
    st.pyplot(fig1)


# Function to visualize sentiment distribution using horizontal bar chart
def visualize_sentiment_distribution_horizontal_bar(df):
    fig, ax = plt.subplots()
    df['Sentiment'].value_counts().plot(kind='barh')
    plt.xlabel('Count')
    plt.ylabel('Sentiment')
    plt.title('Sentiment Distribution (Horizontal Bar Chart)')
    st.pyplot(fig)

# Function to visualize sentiment distribution using heatmap
def visualize_sentiment_distribution_heatmap(df):
    heatmap_data = pd.crosstab(df['Rating'], df['Sentiment'])
    plt.figure(figsize=(10, 6))
    sns.heatmap(heatmap_data, annot=True, fmt='d', cmap="YlGnBu")
    plt.title('Sentiment Distribution Heatmap')
    plt.xlabel('Sentiment')
    plt.ylabel('Rating')
    st.pyplot()


def main_app():
    st.title("MoodMunch Insights App 🍽️😋")
    st.markdown("---")

    # Main app
    section = st.selectbox("Select Section:", ["Line Reviews", "Import Excel File"])
    if section == "Line Reviews":
        review_type = st.selectbox("Select Review Type:", ["One-Line Reviews", "Multi-Line Reviews"])

        user_input = st.text_area(f"Enter {review_type.lower()} (each on a new line):")
        show_instructions = st.checkbox("Show Instructions for Adding Reviews using Line Review")

        if show_instructions:
            st.info("1. Be specific about your experience.\n"
                    "2. Mention key details like food quality, service, and ambiance.\n"
                    "3. Avoid using excessive capitalization or punctuation.")

        if st.button("Predict Sentiments"):
            if user_input:
                st.success("Sentiment Analysis Result:")
                reviews = user_input.split('\n') if review_type == "Multi-Line Reviews" else [user_input]
                results = {'Review': [], 'Sentiment': []}
                for i, review in enumerate(reviews):
                    original_review = review
                    sentiment = 'Positive' if analyze_sentiment(review) == 1 else 'Negative'

                    st.write(f"Review {i + 1}: {original_review}")
                    st.write(f"Sentiment: {sentiment} :yum:" if sentiment == 'Positive' else f"Sentiment: {sentiment} :broken_heart:")

                    results['Review'].append(original_review)
                    results['Sentiment'].append(sentiment)

                col1, col2 = st.columns(2)

                with col1:
                    with st.expander("Sentiment Distribution (Pie Chart)"):
                        visualize_sentiment_distribution_pie(pd.DataFrame(results))
                with col2:
                    with st.expander("Sentiment Distribution (Bar Chart)"):
                        visualize_sentiment_distribution_bar(pd.DataFrame(results))

            else:
                st.warning("Please enter a review.")
    elif section == "Import Excel File":
        st.subheader("Import Excel File")
        excel_file = st.file_uploader("Choose a file", type=["xlsx", "xls"])
        show_instructions = st.checkbox("Show Instructions for Adding Reviews using Excel Import")

        if show_instructions:
            st.info("Adding Reviews using excel import \n1. Select 'Import Excel File' in the app.\n2. Upload an "
                    "Excel file containing the 'Review' and 'Rating' columns.\n3. Ensure the Excel file structure has two "
                    "columns named 'Review' and 'Rating'.\n4. The app will process the reviews and provide sentiment predictions.")

        if excel_file is not None:
            try:
                df = pd.read_excel(excel_file)
                st.write("Loaded Data:")
                st.dataframe(df)

                st.success("Sentiment Analysis Result:")
                results = {'Review': [], 'Rating': [], 'Sentiment': []}
                for i, row in df.iterrows():
                    review = row['Review'] if 'Review' in row else ''
                    rating = row['Rating'] if 'Rating' in row else 0

                    sentiment = 'Positive 😋' if rating >= 4 else 'Negative 💔'

                    results['Review'].append(review)
                    results['Rating'].append(rating)
                    results['Sentiment'].append(sentiment)

                df_results = pd.DataFrame(results)
                st.write(df_results)

                col1, col2 = st.columns(2)

                with col1:
                    with st.expander("Rating Distribution"):
                        visualize_rating_distribution(df)

                with col2:
                    with st.expander("Sentiment Distribution (Bar Chart)"):
                        visualize_sentiment_distribution_bar(pd.DataFrame(results))

                col1, col2 = st.columns(2)

                with col1:
                    with st.expander("Sentiment Distribution (Pie Chart)"):
                        visualize_sentiment_distribution_pie(pd.DataFrame(results))

                with col2:
                    with st.expander("Sentiment Distribution (Horizontal Bar Chart)"):
                        visualize_sentiment_distribution_horizontal_bar(pd.DataFrame(results))

                with st.expander("Sentiment Distribution (Heatmap)"):
                    visualize_sentiment_distribution_heatmap(pd.DataFrame(results))


            except Exception as e:
                st.error(f"Error: {e}")


if __name__ == "__main__":
    main_app()
