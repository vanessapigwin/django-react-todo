# # Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime


class TableTodo(models.Model):
    AVAILABLE_STATUS = [
        ('completed', 'Completed'),
        ('on_going', 'Ongoing'),
        ('not_started', 'Not Started')
    ]
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=100, unique=True, blank=False)
    task_status = models.CharField(
        max_length=50,
        choices=AVAILABLE_STATUS,
        default='not_started'
    )
    task_description = models.CharField(max_length=200, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    finished_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'table_todo'

    def __str__(self):
        return self.task_name

    def updated_finished_date(self):
        if self.task_status == 'completed':
            self.finished_on = datetime.now()
        else:
            self.finished_on = None
        self.save()