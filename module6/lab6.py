from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from scipy.stats import ttest_ind

class AirlineReviewAnalyzer:
    def __init__(self, filename):
        self.df = pd.read_csv(filename, keep_default_na=False, na_values=[''])
        self.df = self.df[self.df.airline.notnull() & self.df.customer_review.notnull() & self.df.cabin.notnull()]

    def filter_reviews(self):
        airline_counts = self.df.groupby('airline').size()
        business_counts = self.df[self.df.cabin == 'Business Class'].groupby('airline').size()
        economy_counts = self.df[self.df.cabin == 'Economy Class'].groupby('airline').size()

        airline_counts = airline_counts[airline_counts >= 500]
        business_counts = business_counts[business_counts >= 100]
        economy_counts = economy_counts[economy_counts >= 200]

        airlines = set(airline_counts.index).intersection(set(business_counts.index)).intersection(set(economy_counts.index))

        self.df = self.df[self.df.airline.isin(airlines)]

    def compute_polarity(self):
        airline_polarities = []
        for airline in self.df.airline.unique():
            business_reviews = self.df[(self.df.airline == airline) & (self.df.cabin == 'Business Class')]['customer_review']
            economy_reviews = self.df[(self.df.airline == airline) & (self.df.cabin == 'Economy Class')]['customer_review']
            business_polarity = business_reviews.apply(lambda x: TextBlob(x).sentiment.polarity)
            economy_polarity = economy_reviews.apply(lambda x: TextBlob(x).sentiment.polarity)
            business_mean = business_polarity.mean()
            economy_mean = economy_polarity.mean()
            t_stat, p_val = ttest_ind(business_polarity, economy_polarity)
            airline_polarities.append((airline, business_mean, economy_mean, p_val))

        self.result_df = pd.DataFrame(airline_polarities, columns=['Airline', 'Business Class Polarity', 'Economy Class Polarity', 'P-Value'])
        self.result_df = self.result_df.set_index('Airline')

    def create_scatter_plot(self):
        airline_counts = self.df.groupby('airline').size()
        self.result_df['Total Reviews'] = airline_counts
        self.result_df = self.result_df[self.result_df['Total Reviews'] > 500]
        plt.figure(figsize=(5, 5))
        plt.scatter(self.result_df['Economy Class Polarity'], self.result_df['Business Class Polarity'], s=self.result_df['Total Reviews'], alpha=0.5)
        plt.xlabel('Average Polarity for Economy Class Reviews')
        plt.ylabel('Average Polarity for Business Class Reviews')
        plt.title('Comparison Between Economy and Business Class Polarity')
        plt.show()

    def create_word_clouds(self, airline_name):
        emirates_reviews = self.df[self.df.airline == airline_name]
        emirates_reviews['customer_review'] = emirates_reviews['customer_review'].str.replace('✅ Trip Verified |', '')

        business_reviews = emirates_reviews[emirates_reviews.cabin == 'Business Class']
        business_text = ' '.join(business_reviews['customer_review'].tolist())
        business_cloud = WordCloud(background_color='white').generate(business_text)

        economy_reviews = emirates_reviews[emirates_reviews.cabin == 'Economy Class']
        economy_text = ' '.join(economy_reviews['customer_review'].tolist())
        economy_cloud = WordCloud(background_color='white').generate(economy_text)

        all_reviews_text = ' '.join(emirates_reviews['customer_review'].tolist())
        all_reviews_cloud = WordCloud(background_color='white').generate(all_reviews_text)

        plt.figure(figsize=(20, 20))
        plt.subplot(1, 3, 1)
        plt.imshow(business_cloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(f'{airline_name} Business Class Reviews')
        plt.subplot(1, 3, 2)
        plt.imshow(economy_cloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(f'{airline_name} Economy Class Reviews')
        plt.subplot(1, 3, 3)
        plt.imshow(all_reviews_cloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(f'{airline_name} All Reviews')
        plt.show()