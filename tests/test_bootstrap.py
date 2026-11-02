"""Tests for public-only repository scaffold generation."""
import json
import tempfile
import unittest
from pathlib import Path

from tools.bootstrap_repositories import render


class BootstrapTests(unittest.TestCase):
    def test_generates_public_repositories_only(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "generated"
            names = render(output)
            report = json.loads((output / "SCAFFOLD-REPORT.json").read_text())
            self.assertEqual(len(names), 28)
            self.assertEqual(report["count"], 28)
            self.assertNotIn("agent-ecosystem-private", names)
            self.assertNotIn("agent-intelligence-ecosystem", names)
            self.assertTrue((output / "agent-foundation-spec/manifest.json").exists())

    def test_refuses_to_overwrite_without_force(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "generated"
            render(output)
            with self.assertRaises(FileExistsError):
                render(output)


if __name__ == "__main__":
    unittest.main()
