import unittest
import main

class FakeVectorizer:
    """
    Minimal stand-in for the real vectorizer.
    We only implement the method scan_url calls: transform().
    """
    def transform(self, items):
        # Return anything that the model's predict() can accept.
        # Here, we just return the same list back.
        return items

class FakeModel:
    """
    Minimal stand-in for the real model.
    We control predict() to force phishing or safe.
    """
    def __init__(self, label):
        self.label = label  # 1 = phishing, 0 = safe

    def predict(self, X):
        return [self.label]

class TestScanURL(unittest.TestCase):
    def test_returns_phishing_when_model_predicts_1(self):
        result = main.scan_url(
            "http://bad.com",
            model_obj=FakeModel(1),
            vectorizer_obj=FakeVectorizer()
        )
        self.assertIn("Phishing", result)

    def test_returns_safe_when_model_predicts_0(self):
        result = main.scan_url(
            "http://good.com",
            model_obj=FakeModel(0),
            vectorizer_obj=FakeVectorizer()
        )
        self.assertIn("Safe", result)

if __name__ == "__main__":
    unittest.main()
