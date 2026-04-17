import io
import os
import sys
import unittest

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import test_capacity.hello_world as hello_world


class HelloWorldTest(unittest.TestCase):
    def test_prints_uppercase_header(self):
        captured = io.StringIO()
        sys_stdout = sys.stdout
        try:
            sys.stdout = captured
            hello_world.main()
        finally:
            sys.stdout = sys_stdout

        output = captured.getvalue().strip().splitlines()
        self.assertGreaterEqual(len(output), 6)
        self.assertEqual(output[0], "HELLO WORLD")
        self.assertEqual(output[1], "")
        self.assertEqual(len(output[2:]), 5)

    def test_prints_five_distinct_languages(self):
        captured = io.StringIO()
        sys_stdout = sys.stdout
        try:
            sys.stdout = captured
            hello_world.main()
        finally:
            sys.stdout = sys_stdout

        output = captured.getvalue().strip().splitlines()[2:]
        languages = [line.split(":", 1)[0].strip() for line in output]
        self.assertEqual(len(languages), 5)
        self.assertEqual(len(set(languages)), 5)

    def test_translations_match_dictionary(self):
        captured = io.StringIO()
        sys_stdout = sys.stdout
        try:
            sys.stdout = captured
            hello_world.main()
        finally:
            sys.stdout = sys_stdout

        output = captured.getvalue().strip().splitlines()[2:]
        for line in output:
            self.assertIn(":", line)
            language, translation = [part.strip() for part in line.split(":", 1)]
            self.assertIn(language, hello_world.TRANSLATIONS)
            self.assertEqual(translation, hello_world.TRANSLATIONS[language])

    def test_translation_pool_has_more_than_five_languages(self):
        self.assertGreater(len(hello_world.TRANSLATIONS), 5)


if __name__ == "__main__":
    unittest.main()
