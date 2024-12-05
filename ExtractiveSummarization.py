from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def extractive_summary(text, num_sentences=3):
    """
    Summarizes the input text using the LexRank algorithm.
    
    :param text: The input text to summarize.
    :param num_sentences: Number of sentences to include in the summary.
    :return: Extracted summary as a string.
    """
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, num_sentences)
    
    return " ".join([str(sentence) for sentence in summary])

# Example usage
text = "Your long article or document goes here."
print(extractive_summary(text))
