#!/usr/bin/env python
"""
checked_dictionary

v1.0: restrict-to version
v1.1: restrict-if addition

"""
from pprint import pformat
import sys



class checked_dictionary(object):
    """
    A checked dictionary structure.

    Emulates much of the behaviour of a dictionary, but adds the ability to have
    restrict the value of entries based on the keys provided.
    """

    # Static Data (Property Map Whitelist)
    #_restrictions = {}

    def __init__(self):
        """
        Default c'tor.

        """
        self.__init_default__()


    def __init_default__(self):
        """
        This should be called by all c'tors.
        """
        self.__init_restrictions__()
        self.__init_data__()

        #
        # Override and fill in default values here
        #

        return True


    def __init_restrictions__(self):
        if not hasattr(self, "_restrictions"):
            self._restrictions = {}


    def __init_data__(self):
        if not hasattr(self, "_data"):
            self._data = {}


    def add_restriction(self, property_name, restrictions=None):
        """
        Add a new static property to the parameter whitelist.
        Restrictions can be a List or Value (objects are ok but must work with == and != operators.)
        """
        self.__init_restrictions__()

        if not self._restrictions.has_key(property_name):
            self._restrictions[property_name] = { "restrict-to": None }

        if restrictions is not None:
            if self._restrictions[property_name]["restrict-to"] is None:
                self._restrictions[property_name]["restrict-to"] = []

            if not isinstance(restrictions, (list,set,tuple)):
                restrictions = [ restrictions ]

            for r in restrictions:
                if r not in self.get_restrictions(property_name):
                    self._restrictions[property_name]["restrict-to"].append(r)

        return True


    def has_restriction(self, property_name):
        self.__init_restrictions__()
        return self._restrictions.has_key(property_name)


    def get_restrictions(self, property_name):
        self.__init_restrictions__()
        if not self._restrictions.has_key(property_name):
            msg  = ">>> Unknown property: '%s'\n"%(property_name)
            msg += ">>> Valid values are:\n"
            for r in self._restrictions.keys():
                msg += ">>> - '%s'\n"%(r)
            raise ValueError, msg
        return self._restrictions[property_name]["restrict-to"]


    def _validate_data(self, property_name, property_value, throw_error_on_fail=False):
        """
        Check a property against the restrictions.  Returns True if
        the property is ok, False otherwise.
        Set throw_error_on_fail if you want this to throw an error.

        This method is treated as a private method... calling it directly might result
        in unexpected failures.  For example, we don't check that self._data has been
        created, so validating a property against an uninitialized instance will throw
        errors.
        """
        output = True
        restrictions = self.get_restrictions(property_name)

        # restrictions == None means there are no restrictions.
        if restrictions is not None and str(property_value).lower() not in [str(value).lower() for value in restrictions]:
            output = False
            if throw_error_on_fail is True:
                msg  = ">>> Invalid value for property '%s'.\n"%(property_name)
                msg += ">>> Allowable values are:\n"
                for r in restrictions:
                    msg += ">>> - '%s'\n"%(r)
                raise ValueError, msg

        return output


    def set_property_value(self, property_name, property_value, validate=True):
        """
        Set a property value.  Optionally validate it for acceptance.
        If we're setting an unknown property with validation off, then
        add the property to the list with no restrictions.
        """
        self.__init_data__()
        if validate is True:
            self._validate_data(property_name, property_value, throw_error_on_fail=True)
        else:
            self.add_restriction(property_name)

        self._data[property_name] = property_value
        return True


    def has_property_value(self, property_name):
        """
        True if the property exists.
        """
        self.__init_data__()
        if not self._data.has_key(property_name):
            return False
        return True


    def get_property_value(self, property_name, validate=False):
        """
        Get the value of a property.  Optionally validate for correctness.
        """
        self.__init_data__()
        output = None
        if self.has_property_value(property_name):
            output = self._data[property_name]
        else:
            msg  = ">>> Property '%s' was not found.\n"%(property_name)
            msg += ">>> Perhaps you're looking for %s"%(str(self._data.keys()))
            raise KeyError, msg

        if validate is True:
            self._validate_data(property_name, output, throw_error_on_fail=True)

        return output


    def __iter__(self):
        return iter(self._data)


    def iteritems(self):
        for k,v in self._data.iteritems():
            yield k,v


    def __getitem__(self, property_name):
        if isinstance(property_name, slice):
            raise NotImplemented, "slicing is not implemented"
        return self.get_property_value(property_name, validate=False)


    def __setitem__(self, property_name, property_value):
        self.set_property_value(property_name, property_value, validate=True)


    def __delitem__(self, property_name):
        if self.has_property_value(property_name):
            del self._data[property_name]


    def keys(self):
        return self._data.keys()


    def __str__(self):
        output  = "Restrictions:\n"
        output += self.str_restrictions(indent=5, width=90)
        output += "\nData:\n"
        output += self.str_data(indent=5, width=90)
        return output


    def str_restrictions(self, indent=0, width=90):
        return pformat(self._restrictions, width=width, indent=indent)


    def str_data(self, indent=0, width=90):
        return pformat(self._data, width=width, indent=indent)





if __name__ == "__main__":
    """
    testing
    """
    rval = 0

    mydata = checked_dictionary()

    # create properties
    mydata.add_restriction("alpha")
    mydata.add_restriction("bravo",   restrictions=None)
    mydata.add_restriction("charlie", restrictions=300)
    mydata.add_restriction("charlie", restrictions=300)
    mydata.add_restriction("charlie", restrictions=300)
    mydata.add_restriction("delta",   restrictions=[400])
    mydata.add_restriction("echo",    restrictions="rouge")
    mydata.add_restriction("echo",    restrictions=["bleu", "vert"])

    # set some values
    mydata.set_property_value("alpha",   100)
    mydata.set_property_value("bravo",   200)
    mydata.set_property_value("charlie", 300)
    mydata["alpha"] = 900

    # can I set a property that isn't on the accept list if I don't validate?
    mydata.set_property_value("foxtrot", 999, validate=False)

    # what if I try to access it?
    mydata["foxtrot"]
    mydata.get_property_value("foxtrot", validate=False)
    mydata.get_property_value("foxtrot", validate=True)

    # can I set a property that isn't on the accept list if I do validate?
    try:
        mydata.set_property_value("golf", 888, validate=True)
        print "ERROR! setting unknown property allowed with validatation"
        rval = 1
    except ValueError:
        pass

    # can I set a property that isn't on the accept list if I do validate?
    try:
        mydata["hotel"] = 888
        print "ERROR! setting unknown property allowed with validatation"
        rval = 1
    except ValueError:
        pass

    # test __setitem__
    if mydata["alpha"] != 900:
        print "ERROR: __getitem__ failed."
        rval = 1

    # test __delitem__
    del mydata["alpha"]
    try:
        mydata["alpha"]
        print "ERROR! del mydata['alpha'] failed!"
        rval = 1
    except KeyError:
        pass

    # test set_property to invalid value
    try:
        mydata.set_property_value("charlie", "wat?")
        print "ERROR! successfully assigned an invalid value to 'charlie'"
        rval = 1
    except ValueError:
        pass

    # test __setitem__ to invalid value
    try:
        mydata["charlie"] = "wat?"
        print "ERROR! successfully assigned an invalid value to 'charlie'"
        rval = 1
    except ValueError:
        pass

    mydata.set_property_value("echo", "bleu")

    print mydata.keys()
    print mydata

    if rval == 0:
        print "PASS - checked_dictionary"
    else:
        print "FAIL - checked_dictionary"

    sys.exit(rval)
