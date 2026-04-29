import json
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Dict, List

VERSION_MANIFEST_URL = "https://piston-meta.mojang.com/mc/game/version_manifest_v2.json"
MODRINTH_SEARCH_URL = "https://api.modrinth.com/v2/search"


class JsonStore:
    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def load(self, default: Any):
        if not self.path.exists():
            return default
        return json.loads(self.path.read_text(encoding="utf-8"))

    def save(self, payload: Any):
        self.path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


class MinecraftCatalog:
    @staticmethod
    def fetch_versions(limit: int = 200) -> List[Dict[str, str]]:
        with urllib.request.urlopen(VERSION_MANIFEST_URL, timeout=20) as response:
            data = json.loads(response.read().decode("utf-8"))
        versions = data.get("versions", [])
        return [
            {"id": v["id"], "type": v["type"], "releaseTime": v["releaseTime"]}
            for v in versions[:limit]
        ]


class LoaderCatalog:
    @staticmethod
    def builtin() -> Dict[str, List[str]]:
        return {
            "vanilla": ["none"],
            "fabric": ["0.15.11", "0.16.10"],
            "forge": ["47.3.11", "50.1.9"],
            "quilt": ["0.26.4", "0.28.1"],
            "neoforge": ["20.4.238", "21.0.0-beta"],
        }


class ModrinthClient:
    @staticmethod
    def search(query: str, project_type: str = "mod", limit: int = 10) -> List[Dict[str, str]]:
        encoded_query = urllib.parse.quote(query)
        facets = urllib.parse.quote(json.dumps([[f'project_type:{project_type}']]))
        url = f"{MODRINTH_SEARCH_URL}?query={encoded_query}&limit={limit}&facets={facets}"
        with urllib.request.urlopen(url, timeout=20) as response:
            data = json.loads(response.read().decode("utf-8"))
        results = []
        for hit in data.get("hits", []):
            results.append(
                {
                    "title": hit.get("title", ""),
                    "slug": hit.get("slug", ""),
                    "downloads": str(hit.get("downloads", 0)),
                }
            )
        return results
