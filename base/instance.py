import abc


class Instance(abc.ABCMeta, type):
    """
    Metaclass which ensures only one instance of a given object exists.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print(f"Creating {cls} instance")
            cls._instances[cls] = super(Instance, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
