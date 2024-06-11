import unittest

from fastapi.testclient import TestClient

from app.main import app


class TestPredictSubjectivity(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_predict_subjectivity(self):
        payload = {"paragraph": """Vice President Kamala Harris said Sunday on ABC’s “This Week” that the Biden administration does not intend to ban TikTok.

Partial transcript as follows:

RACHEL SCOTT: I do want to ask you also about TikTok. We know that bill cleared the house. You have expressed national security concerns over TikTok, so has the president, why does your campaign then have a TikTok account where you’re encouraging Americans to follow it?

HARRIS: So let’s start with this. We do not intend to ban TikTok. That is not at all the goal or the purpose of this conversation. We need to deal with the owner and we have national security concerns about the owner of TikTok but we have no intention to ban TikTok–

SCOTT: It could–

HARRIS: – In fact, what it, it serves in terms of, it’s an income generator for many people. What it does in terms of allowing people to share information in a free way, in a way that allows people to have discourse is very important. But we do have concerns about the national security applications of the owner of TikTok and that has been our position in terms of what I think we need to do to address those concerns.

SCOTT: The ban could happen if its Chinese parent company does not sell the app. Should your campaign stay on TikTok with those national security concerns that you’re voicing?

HARRIS: Well, we’ll address that when we come to it. But right now, we are concerned about the owner of TikTok and the national security implications. We do not intend to ban TikTok and we understand its purpose and its utility and the enjoyment that it gives a lot of folks."""}

        response = self.client.post("/predict_subjectivity_on_texts", json=payload)

        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.assertIsInstance(response_json, list)

        paragraph = payload['paragraph']

        for sent in response_json:
            self.assertEqual(sent['sentence'], paragraph[sent['start_index']:sent['end_index']])


if __name__ == "__main__":
    unittest.main()
