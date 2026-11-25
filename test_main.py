from main import track_parcel


def test_valid_tracking():
    assert track_parcel("PKG123") == "In Transit"


def test_invalid_tracking():
    assert track_parcel("XYZ999") == "Parcel Not Found"
