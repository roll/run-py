from .subprocess import SubprocessTask


class AnsibleTask(SubprocessTask):

    # Public

    def meta_invoke(self, command='', *, prefix='', separator=' '):
        prefix = 'ansible 127.0.0.1 -c local {prefix}'.format(prefix=prefix)
        return super().meta_invoke(command, prefix=prefix, separator=separator)
