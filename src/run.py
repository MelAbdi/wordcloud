from wordcloud import WordCloud
from wordcloud import STOPWORDS


class WordCloudGenerator:
    def __init__(self, file_path: str):
        with open(file_path) as f:
            self.text = f.read()

    def run(self, output_path: str, **kwargs) -> None:
        """
        Generate a word cloud image.

        :param output_path: The path to the output file.
        """
        wordcloud = WordCloud(
            **kwargs,
        ).generate(self.text)

        wordcloud.to_file(output_path)


if __name__ == '__main__':
    wc_gen = WordCloudGenerator('data/movies.txt')
    wc_gen.run(
        'output.png'
        , width = 400, height=400,
        background_color='white',
        max_words=500,
        max_font_size=500,
        min_word_length=2,
        stopwords=STOPWORDS.union({'II',}),
    )
