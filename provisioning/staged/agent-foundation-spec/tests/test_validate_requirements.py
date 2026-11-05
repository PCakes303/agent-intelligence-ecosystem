import unittest
from tools.validate_requirements import validate
ITEM={"id":"FND-1","title":"Trust","statement":"Validate input.","priority":"MUST"}
class Tests(unittest.TestCase):
 def test_valid(self): self.assertEqual(validate({"requirements":[ITEM]}),[])
 def test_duplicate(self): self.assertTrue(any("duplicate" in e for e in validate({"requirements":[ITEM,ITEM]})))
 def test_priority(self): self.assertTrue(validate({"requirements":[{**ITEM,"priority":"NO"}]}))
 def test_shape(self): self.assertTrue(validate({}))
if __name__=="__main__": unittest.main()
