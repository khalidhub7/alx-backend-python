#!/usr/bin/env python3
"""a github org client"""
from typing import List, Dict
from utils import (
    get_json, memoize, access_nested_map
)


class GithubOrgClient:
    """a github org client"""
    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        """init method of githuborgclient"""
        self._org_name = org_name

    @memoize
    def org(self) -> Dict:
        """memoize org"""
        return get_json(
            self.ORG_URL.format(org=self._org_name)
        )

    @property
    def _public_repos_url(self) -> str:
        """public repos url"""
        return self.org["repos_url"]

    @memoize
    def repos_payload(self) -> Dict:
        """memoize repos payload"""
        return get_json(self._public_repos_url)

    def public_repos(self, license: str = None
                     ) -> List[str]:
        """public repos"""
        json_payload = self.repos_payload
        public_repos = [
            repo["name"] for repo in json_payload
            if license is None or
            self.has_license(repo, license)
        ]
        return public_repos

    @staticmethod
    def has_license(repo: Dict[str, Dict],
                    license_key: str) -> bool:
        """static: has_license"""
        # license_key cannot be None
        assert license_key is not None
        try:
            has_license = access_nested_map(
                repo, ("license", "key")) == license_key
        except KeyError:
            return False
        return has_license
