from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db import connections


def wrapped_function(func_name):
    def operate(model, *arg, **kwargs):
        with connections[model._meta.app_label].schema_editor() as schema_editor:
            getattr(schema_editor, func_name)(model, *arg, **kwargs)
            print('{} {}'.format(func_name, model._meta))
    return operate


for attr in [
    attr for attr in dir(BaseDatabaseSchemaEditor)
    if not attr.startswith('_')
    and not attr.startswith('sql_')
]:
    globals()[attr] = wrapped_function(attr)
