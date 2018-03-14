class AppRouter(object):
    def db_for_read(self, model, **hints):
        # print(model._meta.model_name)
        if model._meta.model_name in ['houselocation']:
            return 'location'
        return 'default'

    def db_for_write(self, model, **hints):
        # print("test2")
        if model._meta.model_name in ['houselocation']:
            return 'location'
        return 'default'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'auth_db'
        database.
        """
        # print(db == 'location')
        if model_name in ['houselocation']:
            return db == 'location'
        return False

    def allow_relation(self, obj1, obj2, **hints):
        # print("3")
        # if obj1._meta.app_label == 'myapp2' or obj2._meta.app_label == 'myapp2':
        #     return True
        return 'default'

    def allow_syncdb(self, db, model):
        # print("4")
        # if db == 'location':
        #     return model._meta.app_label == 'myapp2'
        # elif model._meta.app_label == 'myapp2':
        #     return False
        return 'default'
