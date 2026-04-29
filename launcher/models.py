from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List


@dataclass
class LoaderChoice:
    name: str
    version: str


@dataclass
class InstallationProfile:
    name: str
    minecraft_version: str
    version_type: str
    loader: LoaderChoice
    game_dir: Path
    java_args: List[str] = field(default_factory=list)
    jvm_path: str = "java"


@dataclass
class ModuleManifest:
    module_id: str
    title: str
    author: str
    entrypoint: str
    style: Dict[str, str]
    description: str = ""
