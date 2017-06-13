#!/usr/bin/env python
"""
checked_dictionary

v1.0: restrict-to version
v1.1: restrict-if addition

"""
from pprint import pformat
from pprint import pprint
import sys



class checked_dictionary(object):
    """
    A checked dictionary structure.

    Emulates much of the behaviour of a dictionary, but adds the ability to have
    restrict the value of entries based on the keys provided.
    """

    # Static Data (Property Map Whitelist)
    #_restriction_list = {}

    def __init__(self):
        """
        Default c'tor.
        """
        self.__init_default__()

        ####
        ##
        ## custom content here!
        ##
        ####


    def __init_default__(self):
        """
        This should be called by all c'tors.
        """
        self.__init_restriction_list__()
        self.__init_data__()
        return True


    def __init_data__(self):
        if not hasattr(self, "_data"):
            self._data = {}
        return True


    def __init_restriction_list__(self):
        if not hasattr(self, "_restriction_list"):
            self._restriction_list = {}
        return True


    def __initialize_restriction__(self, property_name):
        """
        Initialize an empty restriction.
        """
        self.__init_default__()

        if not self._restriction_list.has_key(property_name):
            self._restriction_list[property_name] = { "restrict-to": None,
                                                      "restrict-if": None
                                                    }
        return True


    def add_restriction(self, property_name, restrictions=None):
        """
        Add a new static property to the parameter whitelist.
        Restrictions can be a List or Value (objects are ok but must work with == and != operators.)
        """
        self.__initialize_restriction__(property_name)

        if restrictions is not None:
            if self._restriction_list[property_name]["restrict-to"] is None:
                self._restriction_list[property_name]["restrict-to"] = []

            if not isinstance(restrictions, (list,set,tuple)):
                restrictions = [ restrictions ]

            for r in restrictions:
                if r not in self.get_restrict_to(property_name):
                    self._restriction_list[property_name]["restrict-to"].append(r)

        return True


    def add_restriction_dependency(self, property_name, dependency_name, dependency_value, restrictions=None):
        """
        Adds a new conditional restriction based on values of another field.

        Consider a key-value store like the following:

          key1 = value1
          key2 = value2

        in which allowable values for value2 depend on what value1 is.
        """
        self.add_restriction(property_name,   restrictions=None)
        self.add_restriction(dependency_name, restrictions=None)

        if restrictions is not None:
            key = (dependency_name,dependency_value)

            if self._restriction_list[property_name]["restrict-if"] is None:
                self._restriction_list[property_name]["restrict-if"] = {}

            if not isinstance(restrictions, (list,set,tuple)):
                restrictions = [ restrictions ]

            for r in restrictions:
                if not self._restriction_list[property_name]["restrict-if"].has_key( key ):
                    self._restriction_list[property_name]["restrict-if"][key] = []
                if self._restriction_list[property_name]["restrict-if"].has_key( "dep" ):
                    if self._restriction_list[property_name]["restrict-if"]["dep"] != dependency_name:
                        msg = ">>> Error assigning restriction depedency, cannot have dependencies to multiple properties."
                        raise ValueError,msg
                self._restriction_list[property_name]["restrict-if"]["dep"] = dependency_name

                self._restriction_list[property_name]["restrict-if"][key].append(r)

        return True


    def has_restriction(self, property_name):
        self.__init_default__()
        return self._restriction_list.has_key(property_name)


    def get_restriction_list(self, property_name):
        self.__init_default__()
        if not self._restriction_list.has_key(property_name):
            msg  = ">>> Unknown property: '%s'\n"%(property_name)
            msg += ">>> Valid values are:\n"
            for r in self._restriction_list.keys():
                msg += ">>> - '%s'\n"%(r)
            raise ValueError, msg
        return self._restriction_list[property_name]


    def get_restrict_to(self, property_name):
        return self.get_restriction_list(property_name)["restrict-to"]


    def get_restrict_if(self, property_name):
        return self.get_restriction_list(property_name)["restrict-if"]


    def set_property_value(self, property_name, property_value, validate=True):
        """
        Set a property value.  Optionally validate it for acceptance.
        If we're setting an unknown property with validation off, then
        add the property to the list with no restrictions.
        """
        if validate is True:
            self.__validate_data__(property_name, property_value, throw_error_on_fail=True)
        else:
            self.add_restriction(property_name)

        self._data[property_name] = property_value
        return True


    def has_property_value(self, property_name):
        """
        True if the key, property_name, exists.
        """
        self.__init_default__()
        if not self._data.has_key(property_name):
            return False
        return True


    def get_property_value(self, property_name, validate=False):
        """
        Get the value of a property.  Optionally validate for correctness.
        """
        output = None
        if self.has_property_value(property_name):
            output = self._data[property_name]
        else:
            msg  = ">>> Property '%s' was not found.\n"%(property_name)
            msg += ">>> Perhaps you're looking for %s"%(str(self._data.keys()))
            raise KeyError, msg

        if validate is True:
            self.__validate_data__(property_name, output, throw_error_on_fail=True)

        return output


    def iteritems(self):
        self.__init_default__()
        for k,v in self._data.iteritems():
            yield k,v


    def keys(self):
        self.__init_default__()
        return self._data.keys()


    def str_restrictions(self, indent=0, width=90):
        self.__init_default__()
        return pformat(self._restriction_list, width=width, indent=indent)


    def str_data(self, indent=0, width=90):
        self.__init_default__()
        return pformat(self._data, width=width, indent=indent)


    def __2tuple_lower__(self, data):
        """
        converts a 2-tuple of strings to lower case.
        """
        return (str(data[0]).lower(), str(data[1]).lower())


    def __in_2tuple__(self, value, data_list, case_sensitive=False):
        """
        Check a 2-tuple for inclusion in a data list.
        """
        output = False
        if case_sensitive is False:
            for x in data_list:
                if isinstance(x, tuple):
                    if self.__2tuple_lower__(value) == self.__2tuple_lower__(x):
                        output = True
                        break
        else:
            for x in data_list:
                if isinstance(x, tuple):
                    if value == x:
                        output = True
                        break
        return output


    def __in_list__(self, value, data_list, case_sensitive=False):
        """
        Check a value for inclusion within a list with optional case-sensitive checking.
        """
        output = False
        if case_sensitive is False:
            output = str(value).lower() in [ str(x).lower() for x in data_list ]
        else:
            output = value in [ x for x in data_list ]
        return output


    def __restrict_if_lookup__(self, key, restrict_to, case_sensitive=False):
        """
        Lookup a key (tuple) in a restrict_if structure.
        TODO: this needs improving
        """
        output = None
        if case_sensitive is False:
            key = self.__2tuple_lower__(key)
        for k,v in restrict_to.iteritems():
            if case_sensitive is False:
                if isinstance(k, tuple):
                    if key == self.__2tuple_lower__(k):
                        output = v
                        break
            else:
                if key == k:
                    output = v
                    break
        return output


    def __validate_data__(self, property_name, property_value, throw_error_on_fail=False):
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
        restrict_to = self.get_restrict_to(property_name)
        restrict_if = self.get_restrict_if(property_name)

        # restrict_to == None means there no immediate restrictions
        if restrict_to is not None and str(property_value).lower() not in [str(value).lower() for value in restrict_to]:
            output = False
            if throw_error_on_fail is True:
                msg  = ">>> Invalid value for property '%s'.\n"%(property_name)
                msg += ">>> Allowable values are:\n"
                for r in restrict_to:
                    msg += ">>> - '%s'\n"%(r)
                raise ValueError, msg

        elif restrict_if is not None:
            dep_key = str(restrict_if["dep"])
            dep_val = str(self.get_property_value(dep_key))

            #if not restrict_if.has_key( (dep_key,dep_val) ):
            allowable_values = self.__restrict_if_lookup__((dep_key,dep_val), restrict_if, case_sensitive=False)

            if allowable_values is None:
                output = False
                if throw_error_on_fail is True:
                    msg = ">>> Error: Dependency not configured for property/value:'%s'/'%s'"%(dep_key,dep_val)
                    raise ValueError,msg

            if not self.__in_list__(property_value, allowable_values, case_sensitive=False):
                output = False
                if throw_error_on_fail is True:
                    msg  = ">>> Invalid value for property '%s', given value '%s'.\n"%(property_name, property_value)
                    msg += ">>> Failed depenency check against property/value pair '%s'/'%s'\n"%(dep_key,dep_val)
                    msg += ">>> Allowable values are:\n"
                    for r in allowable_values:
                        msg += ">>> - '%s'\n"%(r)
                    raise ValueError, msg

        return output


    def __iter__(self):
        self.__init_default__()
        return iter(self._data)


    def __getitem__(self, property_name):
        if isinstance(property_name, slice):
            raise NotImplemented, "slicing is not implemented"
        return self.get_property_value(property_name, validate=False)


    def __setitem__(self, property_name, property_value):
        self.set_property_value(property_name, property_value, validate=True)


    def __delitem__(self, property_name):
        if self.has_property_value(property_name):
            del self._data[property_name]


    def __str__(self):
        self.__init_default__()
        output  = "Restrictions:\n"
        output += self.str_restrictions(indent=5, width=90)
        output += "\nData:\n"
        output += self.str_data(indent=5, width=90)
        return output







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
    print "Test set_property_value() assignment of unknown property with validation: ",
    try:
        mydata.set_property_value("golf", 888, validate=True)
        print "ERROR! setting unknown property allowed with validatation"
        rval = 1
        print mydata
    except ValueError:
        pass

    # can I set a property that isn't on the accept list if I do validate?
    print "Test [] assignment of unknown property with validation: ",
    try:
        mydata["hotel"] = 888
        print "FAIL"
        print "ERROR! setting unknown property allowed with validatation"
        print mydata
        rval = 1
    except ValueError:
        print "PASS"

    # test __getitem__
    print "Test __getitem__: ",
    if mydata["alpha"] != 900:
        print "FAIL"
        print mydata
        rval = 1
    else:
        print "PASS"

    # test __delitem__
    print "test __delitem__: ",
    del mydata["alpha"]
    try:
        mydata["alpha"]
        print "FAIL"
        print "ERROR! del mydata['alpha'] failed!"
        print mydata
        rval = 1
    except KeyError:
        print "PASS"

    # test set_property to invalid value
    print "test set_property to invalid value: ",
    try:
        mydata.set_property_value("charlie", "wat?")
        print "FAIL"
        print "ERROR! successfully assigned an invalid value to 'charlie'"
        print mydata
        rval = 1
    except ValueError:
        print "PASS"

    # test __setitem__ to invalid value
    print "test __setitem__ to invalid value: ",
    try:
        mydata["charlie"] = "wat?"
        print "FAIL"
        print "ERROR! successfully assigned an invalid value to 'charlie'"
        print mydata
        rval = 1
    except ValueError:
        print "PASS"


    mydata.set_property_value("echo", "bleu")

    print ""
    print "Test restriction dependencies:"
    print ""
    mydata.add_restriction("foo", restrictions=None)
    mydata.add_restriction("bar", restrictions=["A","B"])
    mydata.add_restriction("baz", restrictions=None)
    mydata.add_restriction_dependency("baz", "bar", "A", restrictions=["C","D"])
    mydata.add_restriction_dependency("baz", "bar", "B", restrictions=["E","F"])


    print "Test invalid assignment: ",
    try:
        mydata.set_property_value("bar","Z",validate=True)
        print "FAIL"
        print mydata
        rval = 1
    except:
        print "PASS"

    print "Test valid assignment: ",
    try:
        mydata["bar"] = "A"
        print "PASS"
    except ValueError, msg:
        print "FAIL"
        print mydata
        rval = 1

    print "Test valid assignment: ",
    try:
        mydata["baz"] = "C"
        print "PASS"
    except ValueError, msg:
        print "FAIL"
        print mydata
        rval = 1

    print "Test valid assignment: ",
    try:
        mydata["baz"] = "D"
        print "PASS"
    except ValueError, msg:
        print "FAIL"
        print mydata
        rval = 1

    print "Test invalid assignment: ",
    try:
        mydata["baz"] = "E"
        print "FAIL"
        print mydata
        rval = 1
    except ValueError,msg:
        print "PASS"
        #print msg


    print ""
    print "="*80
    print ""


    if rval == 0:
        print "PASS - checked_dictionary"
    else:
        print "FAIL - checked_dictionary"


    sys.exit(rval)
