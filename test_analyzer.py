import unittest

from analyzer import analyze_text


class TestTextAnalyzer(unittest.TestCase):

    def test_word_count(self):
        result = analyze_text("Hello GitHub")
        self.assertEqual(result["words"], 2)

    def test_character_count(self):
        result = analyze_text("Hello GitHub")
        self.assertEqual(result["characters"], 12)

    def test_line_count(self):
        result = analyze_text("Hello\nGitHub")
        self.assertEqual(result["lines"], 2)

    def test_empty_text(self):
        self.assertEqual(
            analyze_text(""),
            {
                "words": 0,
                "characters": 0,
                "lines": 0,
            },
        )

    def test_combined_metrics(self):
        self.assertEqual(
            analyze_text("hello world\nGit is fun"),
            {
                "words": 5,
                "characters": 22,
                "lines": 2,
            },
        )


if __name__ == "__main__":
    unittest.main()