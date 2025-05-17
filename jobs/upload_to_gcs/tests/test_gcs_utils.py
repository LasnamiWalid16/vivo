import os

from src.upload_to_gcs.gcs_utils import list_file_paths_in_directory


def test_list_file_paths_in_directory(tmp_path):
    # Setup test directory and files
    file1 = tmp_path / "test1.csv"
    file2 = tmp_path / "test2.json"
    file1.write_text("dreug1,drug2,drug3")
    file2.write_text('[{"drug": "test"}]')

    # Run function
    result = list_file_paths_in_directory(str(tmp_path))

    # Check results
    assert len(result) == 2
    assert any("test1.csv" in path for path in result)
    assert any("test2.json" in path for path in result)
