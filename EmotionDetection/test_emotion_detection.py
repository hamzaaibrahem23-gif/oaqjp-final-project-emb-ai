import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        first_result = emotion_detector("I am glad this happened")
        self.assertEqual(first_result['dominant_emotion'], "joy")
        second_result = emotion_detector("I am really mad about this")
        self.assertEqual(second_result['dominant_emotion'], "anger")
        third_result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(third_result['dominant_emotion'], "disgust")
        fourth_result = emotion_detector("I am so sad about this")
        self.assertEqual(fourth_result['dominant_emotion'], "sadness")
        fifth_result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(fifth_result['dominant_emotion'], "fear")


unittest.main()
