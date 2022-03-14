# twitter-hashtag-sentiment-analysis.py
Python script for analyzing Twitter users' sentiment polarity towards a specific trending hashtag on the platform online.
  - API & Source Platform used: 
    - [Twitter Developer API](https://developer.twitter.com/en/docs/twitter-api) & [Twitter.com](https://twitter.com)
  - Libraries used:
    - `Tweepy`
    - `Textblob`
    - `Pandas`
    - `Numpy`
    - `Matplotlib`

## Fetching the repo
  - Download the [.zip file](https://github.com/kxnyshk/twitter-hashtag-sentiment-analysis.py/archive/refs/heads/master.zip)
  - Unzip the folder
  - Open the [main.py](https://github.com/kxnyshk/twitter-hashtag-sentiment-analysis.py/blob/master/main.py) file in the terminal of your preferred IDE.

## How to use
  - Enter the `#hashtag` you wanna analyze the [sentiment polarity](https://getthematic.com/sentiment-analysis/) of.
  - Wait for the program to analyze the data from the fetched dataset.
  - Dataset used in the analysis, usually ranges between (10, 1000] and is non-customizable by the user.
  
  ### Commands
   - `#hashtag` Trending [hashtag](https://help.twitter.com/en/using-twitter/how-to-use-hashtags) or hot topic you wanna analyze.
   - `-1` Terminates program
   
## Twitter Dev Auth setup
 - The Twitter Developer Authentication for an elevated API has been done through [here](https://developer.twitter.com/en/products/twitter-api).
 - Read the official documentation [here](https://developer.twitter.com/en/docs)
 - The API & TOKEN [keys](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api#:~:text=API%20Key%20and%20Secret%3A%20Essentially,Tokens%20or%20App%20Access%20Token.) are saved via [configparser](https://docs.python.org/3/library/configparser.html) in Python.
 - Therefore, you would need to setup your own keys after [signing up](https://developer.twitter.com/en/portal/petition/essential/basic-info) for your own Twitter Dev account.
 - To setup the config path, create this path/file: `./TwitterDev/config.ini` in the dir/zip.
 - No need to re-setup the path in any code, it has already been declared in [auth.py](https://github.com/kxnyshk/twitter-hashtag-sentiment-analysis.py/blob/master/auth.py)

## About Tweepy
 - The requests between the script and the API has been handled through Tweepy library.
 - Read the official documentation [here](https://docs.tweepy.org/en/stable/)

## Libraries used
  
  ### Textblob
   - TextBlob is a Python (2 and 3) library for processing textual data.
   - It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.
   - Read official documentation [here](https://textblob.readthedocs.io/en/dev/)

  ### Pandas
   - Pandas is a Python library used to analyze data.
   - Read official documentation [here](https://pandas.pydata.org/docs/)

  ### Numpy
   - NumPy is a Python library used for working with arrays. It also has functions for working in domain of linear algebra, fourier transform, and matrices.
   - Read the official documentation [here](https://numpy.org/doc/stable/)

  ### Matplotlib
   - Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.
   - Read the official latest (3.5.1) documentation [here](https://matplotlib.org/3.5.1/)

## Further reading
  - [Sentiment Analysis: Comprehensive Beginners Guide](https://getthematic.com/sentiment-analysis/)
  - [Is More Data Always Better For Building Analytics Models?](https://analyticsindiamag.com/is-more-data-always-better-for-building-analytics-models/)
