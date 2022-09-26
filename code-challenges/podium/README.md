# Coding Challenge: "A Dealer For the People"

## Description

The KGB has noticed a resurgence of overly excited reviews for a McKaig Chevrolet Buick,
a dealership they have planted in the United States. In order to avoid attracting
unwanted attention, you’ve been enlisted to scrape reviews for this dealership
from DealerRater.com and uncover the top three worst offenders of these
overly positive endorsements.

Your mission, should you choose to accept it, is to write a tool that:

1. scrapes the first five pages of reviews.

2. identifies the top three most "overly positive" endorsements
   (using criteria of your choosing, documented in the README).
  
3. outputs these three reviews to the console, in order of severity
   Please include documentation on how to run your application along with how
   to run the test suite.

## How to run the code

The language chosen was **Python** (v3.8.3 on Mac OS) and there is no installation
dependencies. The code was run using a terminal.

### Steps

* I had to
  **[Install Certificates.command](https://stackoverflow.com/questions/52805115/certificate-verify-failed-unable-to-get-local-issuer-certificate)**
  to make requests using SSL.
  
* `main.py` is the code that solves the coding challenge and it runs using
  `$ python3 main.py`. The output will be shown in the terminal (console).
  There are some unit tests in the same file.
  
## Design

We can divide the design into two steps as follows.

### Design step 1

Request DealerRater.com to access "McKaig Chevrolet Buick" page and to parse
the relevant review data creating review objects that are needed to be ranked
as "overly positive" endorsements. This step was the most time-consuming.

The only information used from the review was the main text written by the reviewer.
   
### Design step 2

Use some logic to create a number (index) of each review and using this number we
can rank the reviews. **This is step is the most valuable resource because it has
the knowledge of guessing what is "overly positive" endorsements.**

The logic used to rank the reviews was to create an index for each review and
therefore we can sort the indices to rank the reviews.

**The index is the number of positive words divided by the number of total words of
a review**, it is always between 0 and 1. The idea behind it is that too many positive
words indicate that the person is overreacting saying to many compliments (for example).

The positive words set were brought from `POSITIVE_WORDS_URL` (main.py).

### Design issues

* Improve the HTML parsing somehow. Maybe use a better library, or try to use an API.

There are other data that can be analyzed besides the review's text. I am numbering
3 of them:

* If there are too many "employees worked with" in a review. It can be a signal
  that the reviewer is trying to bring too many employees to the review.  

* To many 5 stars given in all metrics (CUSTOMER SERVICE, QUALITY OF WORK, FRIENDLINESS, ...).

* The reviewer's name, if it contains numbers in the name, it can be a signal of a false user. 
  
## Tech issues

I tried [http://api.dealerrater.com/docs/](http://api.dealerrater.com/docs/)
but we need a token and the pagination seems to be different from the challenge
requirement (5 pages requirement). This way, I forgot the API and I just
requested the `MCKAING_URL` (main.py).

I used the `urllib.request` and the [HTML parser](https://docs.python.org/3/library/html.parser.html)
to avoid installing external packages.

I had to visually see and filter (using `grep` and Python) the data parsed with
`html.parser` to check which tags and attributes I had to filter and get the
reviews' text.
