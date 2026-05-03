def test_task_status_transition_valid():
    from src.models.task import Task, TaskStatus
    t = Task(title='Test')
    t.change_status(TaskStatus.IN_PROGRESS)
    assert t.status == TaskStatus.IN_PROGRESS

def test_task_status_none_invalid():
    from src.models.task import Task
    t = Task(title='Test')
    try:
        t.change_status(None)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert str(e) == 'Status cannot be None'
