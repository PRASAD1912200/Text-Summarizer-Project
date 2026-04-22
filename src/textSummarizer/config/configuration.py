from pathlib import Path
import os
from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml
from textSummarizer.entity import DataIngestionConfig


class Configuration:
    def __init__(self, config_file_path=None, params_file_path=None):
        # Use absolute paths based on project root
        if config_file_path is None:
            project_root = Path(__file__).parent.parent.parent
            config_file_path = project_root / "config" / "config.yaml"
        if params_file_path is None:
            project_root = Path(__file__).parent.parent.parent
            params_file_path = project_root / "params.yaml"
        
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        return DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir)
        )