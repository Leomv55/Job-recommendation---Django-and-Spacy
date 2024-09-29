class SpacyModel:

    @classmethod
    def get_instance(cls):
        if hasattr(cls, "_instance"):
            return cls._instance

        cls._instance = SpacyModel()
        cls._instance._model = cls._instance._load_spacy()
        return cls._instance

    @classmethod
    def get_vector(cls, x):
        model = cls.get_instance()._model
        return model(x).vector

    @classmethod
    def _load_spacy(cls):
        try:
            import spacy
            nlp = spacy.load("en_core_web_md")
            return nlp
        except Exception as e:
            raise RuntimeError("Failed to load spaCy model") from e


class SBertModel:

    @classmethod
    def get_instance(cls):
        if hasattr(cls, "_instance"):
            return cls._instance

        cls._instance = SBertModel()
        cls._instance._model = cls._instance._load_sbert()
        return cls._instance

    @classmethod
    def get_vector(cls, x):
        model = cls.get_instance()._model
        return model.encode(x)

    @classmethod
    def _load_sbert(cls):
        try:
            from sentence_transformers import SentenceTransformer
            nlp = SentenceTransformer('all-MiniLM-L6-v2')
            return nlp
        except Exception as e:
            raise RuntimeError("Failed to load sbert model") from e
