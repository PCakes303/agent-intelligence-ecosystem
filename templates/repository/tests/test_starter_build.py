import json
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class StarterTemplateTests(unittest.TestCase):
    def test_manifest_exists_and_is_public(self):
        data=json.loads((ROOT/"manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(data["visibility"],"public")
        for key in ("id","name","maturity","summary","repository_url"):
            self.assertTrue(data.get(key),key)
    def test_safety_docs_exist(self):
        self.assertTrue((ROOT/"AGENTS.md").is_file())
        self.assertTrue((ROOT/"SECURITY.md").is_file())
if __name__=="__main__": unittest.main()
