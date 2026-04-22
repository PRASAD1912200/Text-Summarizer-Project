from pathlib import Path
import os

# Get project root (parent of src folder)
project_root = Path(__file__).parent.parent.parent

config_file_path = project_root / "config" / "config.yaml"
params_file_path = project_root / "params.yaml"

