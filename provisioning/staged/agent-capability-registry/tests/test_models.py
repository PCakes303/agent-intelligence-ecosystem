import json
import unittest
from pathlib import Path
from jsonschema import Draft202012Validator
from capability_registry import Capability, Requirement, ValidationError

ROOT = Path(__file__).resolve().parents[1]
def load_schema(name):
    schema = json.loads((ROOT / "schemas" / name).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)

CAP = load_schema("capability.schema.json")
REQ = load_schema("requirement.schema.json")

class ModelTests(unittest.TestCase):
    def test_valid_models_match_schemas(self):
        c = Capability("text.summarize", "agent.one", "Summarizes text", "1.2.3", {"domain": "text"})
        r = Requirement("text.summarize", {"domain": "text"})
        c.validate(); r.validate()
        self.assertEqual(list(CAP.iter_errors({"capability_id":c.capability_id,"agent_id":c.agent_id,"description":c.description,"version":c.version,"attributes":dict(c.attributes)})), [])
        self.assertEqual(list(REQ.iter_errors({"capability_id":r.capability_id,"attributes":r.attributes})), [])

    def test_identifier_length_boundaries(self):
        for c in (Capability("c"*129,"agent.one","Description","1.0.0",{}), Capability("cap.one","a"*129,"Description","1.0.0",{})):
            with self.assertRaises(ValidationError): c.validate()
            self.assertTrue(list(CAP.iter_errors({"capability_id":c.capability_id,"agent_id":c.agent_id,"description":c.description,"version":c.version,"attributes":dict(c.attributes)})))
        r=Requirement("c"*129,{})
        with self.assertRaises(ValidationError): r.validate()
        self.assertTrue(list(REQ.iter_errors({"capability_id":r.capability_id,"attributes":r.attributes})))

    def test_description_and_version_bounds(self):
        for c in (Capability("cap.one","agent.one","   ","1.0.0",{}), Capability("cap.one","agent.one","Description","v1",{}), Capability("cap.one","agent.one","d"*1025,"1.0.0",{})):
            with self.assertRaises(ValidationError): c.validate()
            self.assertTrue(list(CAP.iter_errors({"capability_id":c.capability_id,"agent_id":c.agent_id,"description":c.description,"version":c.version,"attributes":dict(c.attributes)})))

    def test_attribute_key_count_and_value_bounds(self):
        for attrs in ({"bad key":"x"},{f"k{i}":"v" for i in range(33)},{"domain":"x"*257}):
            c=Capability("cap.one","agent.one","Description","1.0.0",attrs)
            with self.assertRaises(ValidationError): c.validate()
            self.assertTrue(list(CAP.iter_errors({"capability_id":c.capability_id,"agent_id":c.agent_id,"description":c.description,"version":c.version,"attributes":dict(c.attributes)})))
            r=Requirement("cap.one",attrs)
            with self.assertRaises(ValidationError): r.validate()
            self.assertTrue(list(REQ.iter_errors({"capability_id":r.capability_id,"attributes":r.attributes})))

    def test_unknown_properties_rejected_by_schemas(self):
        c={"capability_id":"cap.one","agent_id":"agent.one","description":"Description","version":"1.0.0","attributes":{},"extra":True}
        r={"capability_id":"cap.one","attributes":{},"extra":True}
        self.assertTrue(list(CAP.iter_errors(c)))
        self.assertTrue(list(REQ.iter_errors(r)))

if __name__ == "__main__":
    unittest.main()
