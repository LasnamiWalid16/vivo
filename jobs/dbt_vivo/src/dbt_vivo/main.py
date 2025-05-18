import pathlib

from dbt.cli.main import dbtRunner

project_dir = pathlib.Path(__file__).parent / "dbt_vivo_project"

# Initialize dbt runner
dbt = dbtRunner()

# Run dbt deps - install packages
deps_result = dbt.invoke(["deps", "--project-dir", str(project_dir)])
if deps_result.success:
    print("dbt deps completed successfully.")
else:
    print("dbt deps failed.")
    exit(1)

# Run dbt build
run_result = dbt.invoke(["build", "--project-dir", str(project_dir)])

# Print results
if run_result.result:
    for r in run_result.result:
        print(f"{r.node.name}: {r.status}")
else:
    print("No results returned from dbt build.")
