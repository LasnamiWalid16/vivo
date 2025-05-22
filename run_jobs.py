import logging
import subprocess
from pathlib import Path

# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def run_job(job_name: str) -> None:
    """Function to run a given job_name in parameter"""
    project_dir = Path(f"jobs/{job_name}")
    main_script_relative_path = Path(f"src/{job_name}/main.py")

    logger.info(f"******************* Running job: {job_name} *******************")

    try:
        subprocess.run(
            ["poetry", "run", "python", str(main_script_relative_path)],
            cwd=str(project_dir),
            check=True,
        )
        logger.info(f"Job {job_name} executed successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error while running main.py: {e}")


if __name__ == "__main__":
    # Jobs list
    job_names_list = [
        "upload_to_gcs",
        "gcs_bq_external_tables",
        "dbt_vivo",
        "traitement_ad_hook",
    ]
    # Run all the jobs
    for job_name in job_names_list:
        run_job(job_name)
