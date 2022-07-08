"""Main code to rank top three most "overly positive" endorsements for
McKaig Chevrolet Buick from DealerRater.com.
"""
import html.parser
import urllib.request

AUTHOR_PREFIX = '- '

MCKAING_URL = (
    'https://www.dealerrater.com/dealer/'
    'McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page')
POSITIVE_WORDS_URL = (
    'https://gist.githubusercontent.com/mkulakowski2/'
    '4289437/raw/1bb4d7f9ee82150f339f09b5b1a0e6823d633958/positive-words.txt')

NUMBER_OF_PAGES = 5
RANK_SIZE = 3

def main():
    positive_words = get_positive_words(POSITIVE_WORDS_URL)
    parser = get_review_parser(MCKAING_URL, positive_words, number_of_pages=5)

    # We sort by the positive index (reversed) to show the most
    # "overly positive" endorsements.
    print(f'TOP 3 rank of overly positive reviews using an over positive index\n')
    for i, review in enumerate(sorted(
            parser.reviews, key=lambda x: x.positive_index, reverse=True)[:RANK_SIZE]):
        print(f'Review {i+1}')
        print(f'Review author: {review.author}')
        print(f'Review text {review.raw_text}')
        print(f'Over positive index: {review.positive_index:.3f}\n')


class Review:
    def __init__(self, author=None, raw_text=None):
        self.author = author
        self.positive_index = -1
        self.raw_text = raw_text

    def calculate_positive_index(self, positive_words):
        """Main logic to classify "overly positive" endorsements.

        We create an index that is the ratio between the number of positive words
        and the number of total words (tokens) of a review's text.
        It is always 0 <= index <= 1. Greater the index, greater the
        "overly positive" endorsements.
        """
        normalized_tokens = normalize_to_tokens(self.raw_text)
        positives = sum(1 for token in normalized_tokens if token in positive_words)
        self.positive_index = positives / len(normalized_tokens)
        return self.positive_index


class ReviewHTMLParser(html.parser.HTMLParser):
    def __init__(self, positive_words=None):
        super(ReviewHTMLParser, self).__init__()

        self.reviews = []

        self._current_review = None
        # Boolean attrs to track the 'span' tag that contains the author and the
        # 'p' tag that contains the review's text.
        self._span_author = self._p_review = False
        self._positive_words = positive_words

    def handle_starttag(self, tag, attrs):
        # We need this condition to find the Author.
        if tag == 'span' and attrs == [('class', 'italic font-18 black notranslate')]:
            self._span_author = True

        # We need this condition to find the review's text.
        if tag == 'p' and attrs == [(
                'class', 'font-16 review-content margin-bottom-none line-height-25')]:
            self._p_review = True

    def handle_endtag(self, tag):
        """We just "close" the logical tags when we found them."""
        if tag == 'span' and self._span_author:
            self._span_author = False
        if tag == 'p' and self._p_review:
            self._p_review = False

    def handle_data(self, data):
        # We need this condition to filter the name of the author.
        if self._span_author and data.startswith(AUTHOR_PREFIX):
            self._current_review = Review(data.lstrip(AUTHOR_PREFIX))
        if self._p_review:  # We need this condition to filter the review's text.
            self._current_review.raw_text = data
            self._current_review.calculate_positive_index(self._positive_words)
            self.reviews.append(self._current_review)


def get_review_parser(url, positive_words, number_of_pages):
    parser = ReviewHTMLParser(positive_words)
    for page_number in range(number_of_pages):
        page = urllib.request.urlopen(f'{url}{page_number}')
        parser.feed(str(page.read()))
    return parser


def get_positive_words(url):
    page = urllib.request.urlopen(f'{url}')
    splitted_content = str(page.read()).split('\\n')  # Splitted into lines.
    # Ignoring first line because it starts with a "b'".
    # All the rest o the lines, that are positive words, start with an "alpha" character.
    return {line for line in splitted_content[1:] if line and line[0].isalpha()}


def normalize_to_tokens(text):
    """Normalize to lower and create a list of tokens (words)."""
    text = text.lower()
    return text.split()


# Test section

def main_tests():
    test_get_positive_words()
    test_normalize_to_tokens()
    test_review()


def test_get_positive_words():
    for word in get_positive_words(POSITIVE_WORDS_URL):
        # Some words have '-' or  '+' char.
        assert word.isalpha() or '-' in word or '+' in word

def test_normalize_to_tokens():
    assert normalize_to_tokens('NorMaLiZe TexT') == ['normalize', 'text']


def test_review():
    positive_words = {'good', 'awesome', 'brave'}

    # 'brave' not in the review_text
    review_text = 'This is a good and awesome review'
    review = Review('Author', review_text)

    assert review.author == 'Author'
    assert review.raw_text == review_text
    # (len(positive words - 'brave')) / len(total words) is the positive index.
    assert review.calculate_positive_index(positive_words) == \
           (len(positive_words) -1) / len(review_text.split())


if __name__ == '__main__':
    main()
    main_tests()
