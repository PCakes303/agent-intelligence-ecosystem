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
            self.assertEqual(len(names), 30)
            self.assertEqual(report["count"], 30)
            self.assertNotIn("agent-ecosystem-private", names)
            self.assertNotIn("agent-intelligence-ecosystem", names)
            self.assertTrue((output / "agent-foundation-spec/manifest.json").exists())
            for name in names:
                target = output / name
                self.assertTrue((target / "tools/starter_build.py").is_file(), name)
                self.assertTrue((target / "docs/ENTRY-LEVEL-BUILD.md").is_file(), name)
                self.assertTrue((target / ".github/workflows/validate.yml").is_file(), name)
                agents = (target / "AGENTS.md").read_text()
                self.assertIn("https://github.com/PCakes303/agent-intelligence-ecosystem", agents)
                self.assertIn("https://github.com/HuffmanMainNode", agents)
            import subprocess, sys
            result = subprocess.run([sys.executable, str(output / names[0] / "tools/starter_build.py")], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            from jsonschema import Draft202012Validator
            schema = json.loads((Path(__file__).resolve().parents[1] / "schemas/repository-manifest.schema.json").read_text())
            validator = Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER)
            for name in names:
                manifest = json.loads((output / name / "manifest.json").read_text())
                self.assertEqual(list(validator.iter_errors(manifest)), [], name)

    def test_refuses_to_overwrite_without_force(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "generated"
            render(output)
            with self.assertRaises(FileExistsError):
                render(output)


if __name__ == "__main__":
    unittest.main()
