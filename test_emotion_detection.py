from EmotionDetection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        test_matrix = [
            ("I am glad this happened", 'joy'),
            ("I am really mad about this", 'anger'),
            ("I feel disgusted just hearing about this", 'disgust'),
            ("I am so sad about this", 'sadness'),
            ("I am really afraid that this will happen", 'fear'),
        ]

        for text, emotion in test_matrix:
            test = emotion_detector(text)
            self.assertEqual(test['dominant_emotion'], emotion)
        

if __name__ == "__main__":
    unittest.main()