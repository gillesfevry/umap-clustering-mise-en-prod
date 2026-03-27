"""
main 
"""

from pathlib import Path
from argparse import ArgumentParser, Namespace
from config_loader import load_configs_from_files
import logging 
import importlib

logger = logging.getLogger(Path(__file__).stem)


def parse_args() -> Namespace:
    """Parse arguments from CLI 

    Returns: 
        namespace containing parsed arguments in its attributes
    """

    parser = ArgumentParser(description="Parse arguments from CLI")
    parser.add_argument("configs", nargs="+", help="Config files for a job")
    parser.add_argument(
        "-e",
        "--extras",
        nargs="*",
        default=[],
        help="Config strings for the job, in JSON like format"
    )
    
    return parser.parse_args()


def logger_configure():
    pass


def main() -> None:
    """Run the desired application"""

    args = parse_args()
    config_paths: list[str] = args.configs

    file_config = config_loader.load_configs_from_files(config_paths)
    extra_config = config_loader.load_configs_from_strings(args.extras)

    job_config = config
    job_name = Path(config_paths[-1])  # .stem.replace("-", "_")

    # job_module = importlib.import_module(name=f"name_package.{job_name}")

    logger.info(f"Launching job {job_name}...")

    # job_module.job(config=job_config)

