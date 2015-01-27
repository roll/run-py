class Settings(dict):
    """Settings representation.

    Class settings representation is usefull to have deal with any
    type of settings in your program like Django or Flask settings.
    It allow to inherit and override values, add clean looking
    computable values (properties).

    Main use case is to have something like:

    - BaseSettings
    - DevelopmentSettings(BaseSettings)
    - ProductionSettings(BaseSettings)

    For frameworks like Django just export settings to local scope
    using locals().update(settings) command.

    Parameters
    ----------
    upper: bool
        Make dict keys upper case.

    Examples
    --------
    Let see the example::

      >>> class Settings(Settings):
      ...   attr1 = 'value1'
      ...
      >>> settings = Settings(upper=True)
      >>> settings
      {'ATTR1': 'value1'}
      >>> settings.attr1
      'value1'
      >>> del settings.attr1
      >>> settings.attr2 = 'value2'
      >>> settings
      {'ATTR2': 'value2'}
      >>> locals().update(settings)

    After last command settings will be available as local variables.
    """

    # Public

    def __init__(self, upper=False):
        self.__upper = upper
        self.update(self.__as_dict)

    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        self.update(self.__as_dict)

    def __delattr__(self, name):
        super().__delattr__(name)
        self.clear()
        self.update(self.__as_dict)

    # Private

    @property
    def __as_dict(self):
        items = {}
        for scope in [self] + type(self).mro():
            if scope is Settings:
                break
            for name in vars(scope):
                if name in items:
                    continue
                if name.startswith('_'):
                    continue
                attr = getattr(self, name)
                if self.__upper:
                    name = name.upper()
                items[name] = attr
        return items
