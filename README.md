The assignment was divided into two parts:
1) Calculation of Levenshtein Distance between movie titles in the primary dataset with the movie titles in the secondary dataset. Data was successfully scraped using BeautifulSoup.
The output of the Levenshtein Distance is stored in the Results directory.
Faced some problems here as the calculation of Levenshtein Distance was computationally very expensive. So, I calculated the distance of the first 10 primary dataset movies with all the secondary dataset movie titles. The code can successfully calculate for all the movies in the primary dataset given more time to compute.


2) Using machine learning algorithms to find meaningful insights into the data. I tried to predict the Revenue of the movie by using relevant features from the primary dataset. So, instead of classification, it became a regression problem, so accordingly I used the regression functions for SVM as well Lasso. The models have still not been trained and I am still working on it to correct a small bug in the preprocessing phase of the dataset. I hope to compelete it before it is evaluated.

Note: I really enjoyed working on the assignment, it seemed simple enough given my experience in it, but working with such an unclean data became a challenging task. It was a great learning experience for me and I would really like to work on such projects if I get an oppurtunity to work in this internship. 
