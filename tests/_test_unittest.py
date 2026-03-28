import unittest
from main import add_task, delete_task, clear_tasks, tasks


class TestTodo(unittest.TestCase):

    def setUp(self):
        clear_tasks()

    def test_add_task(self):
        add_task("Task 1")
        self.assertEqual(tasks, ["Task 1"])

    def test_delete_task(self):
        add_task("Task 1")
        delete_task("Task 1")
        self.assertEqual(tasks, [])

    def test_empty_task(self):
        with self.assertRaises(ValueError):
            add_task("")


if __name__ == "__main__":
    unittest.main()
