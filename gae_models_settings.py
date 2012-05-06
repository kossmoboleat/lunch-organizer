from django.contrib.admin.models import LogEntry

FIELD_INDEXES = {
    LogEntry: {'indexed': ['object_id']},
}