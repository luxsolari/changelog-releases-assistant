import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from render_template import render  # noqa: E402


class TestRenderTemplate(unittest.TestCase):
    def test_substitutes_known_placeholder(self):
        self.assertEqual(render("Hello {{NAME}}!", {"NAME": "whiting"}), "Hello whiting!")

    def test_substitutes_multiple_placeholders(self):
        result = render("{{A}} and {{B}}", {"A": "one", "B": "two"})
        self.assertEqual(result, "one and two")

    def test_missing_key_raises(self):
        with self.assertRaises(KeyError):
            render("Hello {{NAME}}!", {})

    def test_no_placeholders_returns_text_unchanged(self):
        self.assertEqual(render("plain text", {}), "plain text")


if __name__ == "__main__":
    unittest.main()
