import json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class Tests(unittest.TestCase):
 def test_schemas_parse(self):
  paths=list((ROOT/"schemas").rglob("*.schema.json")); self.assertTrue(paths)
  for p in paths: self.assertIsInstance(json.loads(p.read_text(encoding="utf-8")),dict)
 def test_dialect(self):
  for p in (ROOT/"schemas").rglob("*.schema.json"): self.assertEqual(json.loads(p.read_text(encoding="utf-8"))["$schema"],"https://json-schema.org/draft/2020-12/schema")
 def test_ids_unique(self):
  ids=[json.loads(p.read_text(encoding="utf-8"))["$id"] for p in (ROOT/"schemas").rglob("*.schema.json")]; self.assertEqual(len(ids),len(set(ids)))
if __name__=="__main__": unittest.main()
