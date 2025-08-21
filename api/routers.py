class DatabaseRouter:
    """
    A router to control all database operations on models
    """

    def db_for_read(self, model, **hints):
        """Suggest the database to read from."""
        if model._meta.app_label == 'api':
            return 'mongodb'
        return 'default'

    def db_for_write(self, model, **hints):
        """Suggest the database to write to."""
        if model._meta.app_label == 'api':
            return 'mongodb'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if models are in the same app."""
        db_set = {'default', 'mongodb'}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that certain apps' models get created on the right database."""
        if app_label == 'api':
            return db == 'mongodb'
        elif db == 'mongodb':
            return False
        return db == 'default'