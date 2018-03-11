class AppRouter(object):
    def db_for_read(self, model, **hints):
        print("test1")
        if model._meta.model_name  == 'HouseLocation':
            return 'location'
        return 'default'

    def db_for_write(self, model, **hints):
        print("test2")
        if model._meta.model_name  == 'HouseLocation':
            return 'location'
        return 'default'
    
    # def allow_relation(self, obj1, obj2, **hints):
    #     if obj1._meta.app_label == 'myapp2' or obj2._meta.app_label == 'myapp2':
    #         return True
    #     return 'default'
    
    # def allow_syncdb(self, db, model):
    
    #     if db == 'location':
    #         return model._meta.app_label == 'myapp2'
    #     elif model._meta.app_label == 'myapp2':
    #         return False
    #     return 'default'