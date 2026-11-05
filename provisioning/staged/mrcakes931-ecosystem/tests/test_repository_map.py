import unittest
from tools.generate_repository_map import render

class RepositoryMapTests(unittest.TestCase):
    def test_includes_public_and_excludes_private(self):
        data={"repositories":[
            {"name":"public-one","visibility":"public","layer":"foundation","role":"Public role"},
            {"name":"private-one","visibility":"private","layer":"private","role":"Secret"}
        ]}
        result=render(data)
        self.assertIn("public-one",result)
        self.assertNotIn("private-one",result)
        self.assertNotIn("Secret",result)

    def test_sorts_entries(self):
        data={"repositories":[
            {"name":"zeta","visibility":"public","layer":"foundation"},
            {"name":"alpha","visibility":"public","layer":"foundation"}
        ]}
        result=render(data)
        self.assertLess(result.index("alpha"),result.index("zeta"))

    def test_rejects_bad_registry(self):
        with self.assertRaises(ValueError):
            render({})
        
if __name__=="__main__":
    unittest.main()
