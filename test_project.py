import pytest
from project import find_keys,make_folder,split_text_extension



def test_function_1():
    assert find_keys("mp3") == "Audio"
    assert find_keys("zip") == "Compressed"
    assert find_keys("py") == "Code"
    assert find_keys("pdf") == "Documents"
    assert find_keys("jpg") == "Images"
    assert find_keys("exe") == "Softwares"
    assert find_keys("mp4") == "Videos"

def test_section_2():
    with pytest.raises(FileExistsError):
        make_folder("mp3")
    with pytest.raises(FileExistsError):
        make_folder("zip")
    with pytest.raises(FileExistsError):
        make_folder("py")
    with pytest.raises(FileExistsError):
        make_folder("pdf")
    with pytest.raises(FileExistsError):
        make_folder("jpg")
    with pytest.raises(FileExistsError):
        make_folder("exe")
    with pytest.raises(FileExistsError):
        make_folder("mp4")

def test_function_3():
    assert any("png" in d for d in split_text_extension()) 
