#!/usr/bin/env python
"""
Checked multivalue dictionary
"""
from pprint import pformat
from pprint import pprint
import sys

from checked_dictionary import checked_dictionary


class checked_multivalue_dictionary(checked_dictionary):
    """
    Implements a checked_dictionary structure with additional handling for multivalue entries.
    """

    def __init__(self):
        """
        Default c'tor
        """
        self.__init_default__()

        ####
        ##
        ## custom content here!
        ##
        ####

        return None


    def append_property_value(self, property_name, property_value, validate=True):
        """
        Append a property value.

        Optionally validate it for acceptance. If setting an unknown property with validation off,
        then add the property to the list with no restrictions.

        Args:
            property_name:  Property name (dictionary key)
            property_value: Value to append to the property.
            validate:       If True then verify property_value is valid. Default: True

        Returns:
            True for success.
        """
        if validate is True:
            self.__validate_data__(property_name, property_value, throw_error_on_fail=True)
        else:
            # Add empty restriction to schema for property_name.
            self.add_restriction(property_name)

        if not self._data.has_key(property_name):
            self._data[property_name] = property_value
        else:
            if not isinstance(self._data[property_name], (list)):
                self._data[property_name] = [ self._data[property_name] ]

            self._data[property_name].append(property_value)

        return True


    def __lower__(self, value):
        if isinstance(value, list):
            return [ x.lower() for x in value ]
        return str(value.lower())


    def __2tuple_lower__(self, data):
        """
        converts a 2-tuple of strings to lower case.
        """
        return ( self.__lower__(data[0]), self.__lower__(data[1]) )


    def __gen_key_tuples__(self, key):
        """
        """
        if isinstance(key[1], (list,tuple,set) ):
            for v in key[1]:
                yield (key[0], v)
        else:
            yield key

    def __gen_multikey_allowed_values__(self, tuple_depends_on, restrict_to_key, restrict_to_val):
        output = []
        for k in self.__gen_key_tuples__(tuple_depends_on):
            if k == restrict_to_key:
                output += restrict_to_val
                #break
        return output


    def __restrict_if_lookup__(self, tuple_depends_on, restrict_to, case_sensitive=False):
        """
        Lookup a key (tuple) in a restrict_if structure and return the
        set of allowable values for this key.

        TODO: this needs improving
        """
        output = []
        if case_sensitive is False:
            tuple_depends_on = self.__2tuple_lower__(tuple_depends_on)

        for restrict_to_key,restrict_to_val in restrict_to.iteritems():
            if case_sensitive is False:

                if not restrict_to_key == "dep":
                    restrict_to_key = self.__2tuple_lower__(restrict_to_key)
                    output += self.__gen_multikey_allowed_values__(tuple_depends_on, restrict_to_key, restrict_to_val)
                    #for _key in self.__gen_key_tuples__(tuple_depends_on):
                        #if _key == restrict_to_key:
                            #output += restrict_to_val
                            #break
                    #if tuple_depends_on == restrict_to_key:
                        #output += restrict_to_val
                        #break
            else:
                if tuple_depends_on == restrict_to_key:
                    output = restrict_to_val
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
                msg  = ">>> '%s' is an invalid value for property '%s'.\n"%(property_value, property_name)
                msg += ">>> Allowable values are:\n"
                for r in restrict_to:
                    msg += ">>> - '%s'\n"%(r)
                raise ValueError, msg

        elif restrict_if is not None:
            dep_key = str(restrict_if["dep"])
            dep_val = self.get_property_value(dep_key)         # TODO: this needs to be checked for being a list...

            if not isinstance(dep_val, list):
                dep_val = str(dep_val)

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
                    msg  = " Invalid value for property '%s', given value '%s'.\n"%(property_name, property_value)
                    msg += ">>> Failed depenency check against property/value pair '%s'/'%s'\n"%(dep_key,dep_val)
                    msg += ">>> Allowable values are:\n"
                    allowable_values.sort()
                    for r in allowable_values:
                        msg += ">>> - '%s'\n"%(r)
                    raise ValueError, msg

        return output





def __test_checked_multivalue_dictionary__():
    """
    testing
    """
    rval = 0

    mydata = checked_multivalue_dictionary()

    print ""
    print "Test restriction dependencies:"
    print ""
    mydata.add_restriction("foo", restrictions=None)
    mydata.add_restriction("bar", restrictions=["A","B"])
    mydata.add_restriction("bar", restrictions="C")
    mydata.add_restriction("baz", restrictions=None)

    mydata.add_restriction_dependency("baz", "bar", "A", restrictions=["C","D"])
    mydata.add_restriction_dependency("baz", "bar", "B", restrictions=["E"])
    mydata.add_restriction_dependency("baz", "bar", "B", restrictions=["F"])

    mydata.add_restriction("bif")
    mydata.add_restriction_dependency("bif", "bar", "A", restrictions=["AAA", "BBB"])
    mydata.add_restriction_dependency("bif", "bar", "B", restrictions=["cCc"])
    mydata.add_restriction_dependency("bif", "bar", "C", restrictions="FAQ")


    print "%-60s "%("Test invalid assignment"+":"),
    try:
        mydata.set_property_value("bar","Z",validate=True)
        print "FAIL"
        print mydata
        rval = 1
    except:
        print "PASS"

    print "%-60s "%("Test valid assignment"+":"),
    try:
        mydata["bar"] = "A"
        print "PASS"
    except ValueError, msg:
        print "FAIL"
        print mydata
        rval = 1

    print "%-60s "%("Test valid assignment"+":"),
    try:
        mydata["baz"] = "C"
        print "PASS"
    except ValueError, msg:
        print "FAIL"
        print mydata
        rval = 1

    print "%-60s "%("Test valid assignment"+":"),
    try:
        mydata["baz"] = "D"
        print "PASS"
    except ValueError, msg:
        print "FAIL"
        print mydata
        rval = 1

    print "%-60s "%("Test invalid assignment"+":"),
    try:
        mydata["baz"] = "E"
        print "FAIL"
        print mydata
        rval = 1
    except ValueError,msg:
        print "PASS"
        #print msg


    # Test the conditional dependency on multi-value columns
    mydata.append_property_value("bar", "B")

    print "%-60s "%("Test valid assignment" + ":"),
    try:
        mydata.append_property_value("bif", "AAA")
        print "PASS"
    except:
        print "FAIL"
        rval = 1

    print "%-60s "%("Test valid append" + ":"),
    try:
        mydata.append_property_value("bif", "BBB")
        print "PASS"
    except:
        print "FAIL"
        rval = 1

    print "%-60s "%("Test valid append (alt key)" + ":"),
    try:
        mydata.append_property_value("bif", "CCC")
        print "PASS"
    except:
        print "FAIL"
        rval = 1

    print "%-60s "%("Test invalid append (valid value, dep key missing)" + ":"),
    try:
        mydata.append_property_value("bif", "FAQ")
        print "FAIL"
        rval = 1
    except:
        print "PASS"


    print ""
    print "="*80
    print ""


    if rval == 0:
        print "PASS - checked_multivalue_dictionary"
    else:
        print "FAIL - checked_multivalue_dictionary"





if __name__ == "__main__":

    rval = 0
    rval = __test_checked_multivalue_dictionary__()

    sys.exit(rval)
