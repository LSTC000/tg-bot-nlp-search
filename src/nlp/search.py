import string

import natasha as nt
import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


nltk.download("punkt")


class NLPSearch:
    _newcorpus = PlaintextCorpusReader("newcorpus/", r".*\.txt")
    _sent_tokens = nltk.sent_tokenize(_newcorpus.raw(_newcorpus.fileids()))

    @staticmethod
    def _normalize(text) -> list:
        segmenter = nt.Segmenter()
        morph_vocab = nt.MorphVocab()
        emb = nt.NewsEmbedding()
        morph_tagger = nt.NewsMorphTagger(emb)
        ner_tagger = nt.NewsNERTagger(emb)

        word_token = text.translate(str.maketrans("", "", string.punctuation)).replace(
            "—", ""
        )

        doc = nt.Doc(word_token)
        doc.segment(segmenter)
        doc.tag_morph(morph_tagger)
        doc.tag_ner(ner_tagger)

        for token in doc.tokens:
            token.lemmatize(morph_vocab)
        resDict = {_.text: _.lemma for _ in doc.tokens}

        return [resDict[i] for i in resDict]

    @classmethod
    def response(cls, query: str) -> str:
        query = query.lower()
        robo_response = ""

        cls._sent_tokens.append(query)

        TfidfVec = TfidfVectorizer(tokenizer=cls._normalize)
        tfidf = TfidfVec.fit_transform(cls._sent_tokens)

        vals = cosine_similarity(tfidf[-1], tfidf)
        idx = vals.argsort()[0][-2]

        flat = vals.flatten()
        flat.sort()

        req_tfidf = flat[-2]

        cls._sent_tokens.remove(query)

        if not req_tfidf:
            return robo_response + "Извините, я не нашел ответа..."

        return robo_response + cls._sent_tokens[idx]
