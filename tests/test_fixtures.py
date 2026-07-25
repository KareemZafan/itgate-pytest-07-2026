
import pytest

"""
@pytest.fixture(scope="module",autouse=True)
def open_db_connection():
    # pre-condition code will run before the test function starts
    print("\nOpening database connection...\n")

@pytest.fixture(scope="module",autouse=True)
def close_db_connection():
    # post-condition code will run after the test function completes
    yield
    print("\nClosing database connection...\n")
"""

@pytest.fixture(scope="module", autouse=True)
def db_connection_setup():
    # pre-condition code will run before the test function starts
    print("\nOpening database connection...\n")
    yield
    # post-condition code will run after the test function completes
    print("\nClosing database connection...\n") 



def test_insert_into_db():
    print("\nInserting data into the database...\n")
    assert True

def test_update_in_db():
    print("\nUpdating data in the database...\n")
    assert True

def test_delete_from_db():
    print("\nDeleting data from the database...\n")
    assert True
