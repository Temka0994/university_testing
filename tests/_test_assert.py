from main import add_task, delete_task, clear_tasks, tasks


def test_clear_tasks():
    clear_tasks()
    add_task("Test task")
    assert tasks == ["Test task"]


def test_delete_tasks():
    delete_task("Test task")
    assert tasks == []


def test_add_empty_task():
    try:
        add_task("")
        assert False
    except ValueError:
        assert True
