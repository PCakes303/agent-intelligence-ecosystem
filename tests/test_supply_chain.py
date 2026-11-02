import unittest
from tools.validate_supply_chain import validate
VALID={"record_version":"1.0","artifact":{"name":"demo","version":"1","digest":{"algorithm":"sha256","value":"0"*64}},"source":{"repository":"https://example.test/repo","commit":"a"*40},"sbom":{"format":"CycloneDX","uri":"https://example.test/sbom.json"},"verification":{"signature_present":False,"signature_verified":False}}
class Tests(unittest.TestCase):
    def test_valid_shape(self): self.assertEqual(validate(VALID),[])
    def test_digest(self): self.assertTrue(validate({**VALID,"artifact":{**VALID["artifact"],"digest":{"algorithm":"md5","value":"x"}}}))
    def test_source_https(self): self.assertTrue(validate({**VALID,"source":{**VALID["source"],"repository":"http://example.test"}}))
    def test_commit(self): self.assertTrue(validate({**VALID,"source":{**VALID["source"],"commit":"bad"}}))
    def test_signature_logic(self): self.assertTrue(validate({**VALID,"verification":{"signature_present":False,"signature_verified":True}}))
if __name__=="__main__": unittest.main()
