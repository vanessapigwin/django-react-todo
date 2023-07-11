from django.test import TestCase
from todo.models import TableTodo
from django.db.utils import IntegrityError

class TodoTest(TestCase):
    
    def setUp(self):
        self.todo_task = TableTodo(
            # task_id = 1
            task_name = 'Bird Watching',
            # task_status = 'not_started',
            # task_description 'Finish youtube 2 hr bird watching video'
            # created_on = ''_
            # finished_on = ''
        )
        self.todo_task.save()

    def test_create_task(self):
        self.assertIsInstance(self.todo_task, TableTodo)
        self.assertEquals(self.todo_task.task_name, 'Bird Watching')

    def test_create_nonunique_task(self):
        with self.assertRaises(IntegrityError):
            new_task = TableTodo(task_name = 'Bird Watching')
            new_task.save()

    def test_read_task(self):
        saved_task = TableTodo.objects.all()
        self.assertEquals(saved_task[0].task_name, 'Bird Watching')

    def test_update_status_completed(self):
        self.todo_task.task_status = 'completed'
        self.todo_task.save()

        saved_task = TableTodo.objects.first()
        self.assertIsNotNone(saved_task.finished_on, f'Date finished not found, actual: {saved_task.finished_on}')

    def test_delete_task(self):
        new_task = TableTodo(task_name='Delete me please')
        new_task.save()

        tasks = TableTodo.objects.all()
        self.assertEqual(tasks.count(), 2, msg='New task for delete test not added')

        new_task.delete()

        tasks = TableTodo.objects.all()
        self.assertEqual(tasks.count(), 1, msg='Task not deleted')
