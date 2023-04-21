
import unittest

from ghastoolkit.octokit.github import GitHub, Repository


class TestGitHub(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        # reset
        GitHub.instance = "https://github.com"
        GitHub.api_rest = "https://api.github.com"
        GitHub.api_graphql = "https://api.github.com/graphql"

        return super().tearDown()

    def test_default(self):
        GitHub.init("GeekMasher/ghastoolkit")
        
        self.assertEqual(GitHub.instance, "https://github.com")
        self.assertEqual(GitHub.api_rest, "https://api.github.com")
        self.assertEqual(GitHub.api_graphql, "https://api.github.com/graphql")

    def test_server(self):
        GitHub.init("GeekMasher/ghastoolkit", instance="https://github.geekmasher.dev")
        
        self.assertEqual(GitHub.instance, "https://github.geekmasher.dev")
        self.assertEqual(GitHub.api_rest, "https://github.geekmasher.dev/api")
        self.assertEqual(GitHub.api_graphql, "https://github.geekmasher.dev/api/graphql")

    def test_parseReference(self):
        repo = Repository.parseRepository("GeekMasher/ghastoolkit")
        self.assertEqual(repo.owner, "GeekMasher")
        self.assertEqual(repo.repo, "ghastoolkit")

        repo = Repository.parseRepository("GeekMasher/ghastoolkit@main")
        self.assertEqual(repo.owner, "GeekMasher")
        self.assertEqual(repo.repo, "ghastoolkit")
        self.assertEqual(repo.branch, "main")
        self.assertEqual(repo.reference, "refs/heads/main")

