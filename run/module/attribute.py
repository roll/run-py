def attribute(module, name, *, category=None, getvalue=True):
    """Return module's attribute by given name.

    :param object module: module instance
    :param str name: attribute name, supports nested "module.attribute"
    :param None/type/str category: returns attribute only of given class
    :param bool getvalue: if True returns attribute's value

    :raises AttributeError: if module has not attribute for given name
    :raises TypeError: if attribute is not instance of given category

    :returns: attribute instance/attribute value
    :rtype: :class:`run.attribute.Attribute`/mixed
    """
    return module.__getattribute__(name, category=category, getvalue=getvalue)
