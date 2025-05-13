import pathlib

from dbt.cli.main import dbtRunner

project_dir = pathlib.Path(__file__).parent / "dbt_vivo_project"

# Run dbt run
dbt = dbtRunner()
res = dbt.invoke(["run", "--project-dir", str(project_dir)])

# print results
if res.result:
    for r in res.result:
        print(f"{r.node.name}: {r.status}")
else:
    print("No results returned from dbt run.")
