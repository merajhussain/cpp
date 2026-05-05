import importlib



def dynamic_import(name):
    return importlib.import_module(name)

if __name__ == '__main__':
    print(dynamic_import('foo').main())
    print(dynamic_import('bar').main())