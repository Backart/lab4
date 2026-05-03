class TaskService:
    def __init__(self):
        self.tasks = {}

    def create_task(self, task):
        self.tasks[task.id] = task
        return task

    def get_task_by_id(self, task_id):
        return self.tasks.get(task_id)

    def assign_task(self, task_id, user_id):
        task = self.get_task_by_id(task_id)
        if task:
            task.assignee_id = user_id
        return task
