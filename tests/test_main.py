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


        payload = {"paragraph": "Dozens of road changes are being planned between South Ribble and Preston which highway bosses hope will encourage more people to cycle, walk and use public transport.\nThe traffic calming measures are part of broader plans to upgrade a series of key junctions on the A582, between Lostock Hall and Penwortham, in order to reduce congestion on the busy route.\nHowever, other local roads connecting the two destinations are also in line for a radical revamp \u2013 and the public are being asked for their opinions on those proposals as well.\nRead more: 195 objections to Manchester Road zebra crossing redesign snubbed as plans forced ahead\nThe so-called \u201csustainable travel corridor\u201d is centred on the B5254 \u2013 Leyland Road and Watkin Lane \u2013 but also takes in roads including Cop Lane, Coote Lane and Croston Road.\nThe routes are commonly used as rat runs to avoid the bumper-to-bumper tailbacks that often blight the A582 during the morning and evening rush hours.\nThe aim of the overarching plans is to create a more free-flowing A582 and, according to Lancashire County Council, to \u201cdiscourage through-traffic by using traffic calming and more pedestrian crossings\u201d which the authority says will \u201cimprove road safety and create better local environments with fewer speeding vehicles\u201d and better air quality.\nCounty Hall is also seeking to improve the reliability of bus journeys along the corridor by reducing hold-ups. Passengers will be kept better informed of any delays that do occur via real-time information installed at bus stops.\nAll of the plans require confirmation of government funding previously earmarked for the wider project \u2013 and for which a formal bid will be prepared when the current public consultation is completed.\nWhat\u2019s being planned?\nThe measures for the B5254 corridor and its adjoining routes include:\nWatkin Lane, close to the railway station \u2013 speed cushions\nWatkin Lane, north of Moss Lane \u2013 raised zebra crossing\nCroston Road, close to Westfield \u2013 speed cushions\nCroston Road, near St. Paul\u2019s Park play area \u2013 raised zebra crossing\nCroston Road, south of Church Lane/Fowler Road junction \u2013 speed cushions\nSchool Lane, at junction with Croston Road \u2013 raised zebra crossing\nCoote Lane and Chain House Lane, from Leyland Road to Penwortham Way \u2013 speed cushions\nNew Lane/Pope Lane/Cop Lane \u2013 speed cushions between Leyland Road and Millbrook Way \u2013 speed cushions\nPope Lane/Cop Lane junction \u2013 raised junction and raised zebra crossings\nPope Lane/Hawksbury Drive junction \u2013 raised junction and raised zebra crossings\nMarshall\u2019s Brow/Leyland Road junction \u2013 raised zebra crossing on Marshall\u2019s Brow\nLeyland Road, close to Fir Trees Road \u2013 removal of southbound bus stop layby and addition of new shelter\nLeyland Road/The Cawsey junction \u2013 zebra crossings on Leyland Road (south of the roundabout) and The Cawsey; upgraded crossing points on Leyland Road (north of the roundabout\nLeyland Road to Marshall\u2019s Brow \u2013 speed cushions\nLeyland Road/New Lane junction \u2013 new mini-roundabout\nLeyland Road, south of Brydeck Avenue \u2013 removal of northbound bus stop layby and addition of new shelter\nLeyland Road, south of Buller Avenue \u2013 puffin crossing replaced with raised zebra crossing\nLeyland Road, south of Hawkhurst Road \u2013 new raised crossing point with tactile paving\nLeyland Road \u2013 Marshall\u2019s Brow to north of Talbot Road \u2013 speed cushions\nLeyland Road/Talbot Road junction \u2013 raised table junction\nLeyland Road, close to Penwortham Methodist Church \u2013 raised skewed parallel crossing point\nLeyland Road/Riverside Road junction \u2013 raised junction\nLeyland Road/Riverside Road junction \u2013 raised zebra crossing on Riverside Road\nLeyland Road, north west of Riverside Road \u2013 shared use cycleway and footpath\nLeyland Road, from Riverside Road to Fish House Bridge \u2013 chicanes with priority for westbound traffic\nLeyland Road, south of Valley Road \u2013 raised crossing point\nLeyland Road, between Valley Road and A582 roundabout \u2013 parking restrictions\nHAVE YOUR SAY\nClick here to fill in the survey on the Lancashire County Council website until 21st August.\nSubscribe: Keep in touch directly with the latest headlines from Blog Preston, join our WhatsApp channel and subscribe for our twice-a-week email newsletter. Both free and direct to your phone and inbox.\nRead more: See the latest Preston news and headlines"}
        response = self.client.post("/predict_subjectivity_on_texts", json=payload)

        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.assertIsInstance(response_json, list)

        paragraph = payload['paragraph']

        for sent in response_json:
            print(sent)
            self.assertEqual(sent['sentence'], paragraph[sent['start_index']:sent['end_index']])

if __name__ == "__main__":
    unittest.main()
