# generated from rosidl_generator_py/resource/_idl.py.em
# with input from interface_msgs:msg/TimeWindowOffline.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'norm'
import array  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_TimeWindowOffline(type):
    """Metaclass of message 'TimeWindowOffline'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('interface_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'interface_msgs.msg.TimeWindowOffline')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__time_window_offline
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__time_window_offline
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__time_window_offline
            cls._TYPE_SUPPORT = module.type_support_msg__msg__time_window_offline
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__time_window_offline

            from geometry_msgs.msg import Point
            if Point.__class__._TYPE_SUPPORT is None:
                Point.__class__.__import_type_support__()

            from geometry_msgs.msg import PoseArray
            if PoseArray.__class__._TYPE_SUPPORT is None:
                PoseArray.__class__.__import_type_support__()

            from geometry_msgs.msg import Quaternion
            if Quaternion.__class__._TYPE_SUPPORT is None:
                Quaternion.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class TimeWindowOffline(metaclass=Metaclass_TimeWindowOffline):
    """Message class 'TimeWindowOffline'."""

    __slots__ = [
        '_time_window',
        '_j0',
        '_q_spine',
        '_norm',
    ]

    _fields_and_field_types = {
        'time_window': 'sequence<geometry_msgs/PoseArray>',
        'j0': 'sequence<geometry_msgs/Point>',
        'q_spine': 'sequence<geometry_msgs/Quaternion>',
        'norm': 'sequence<double>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'PoseArray')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Point')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Quaternion')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.time_window = kwargs.get('time_window', [])
        self.j0 = kwargs.get('j0', [])
        self.q_spine = kwargs.get('q_spine', [])
        self.norm = array.array('d', kwargs.get('norm', []))

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.time_window != other.time_window:
            return False
        if self.j0 != other.j0:
            return False
        if self.q_spine != other.q_spine:
            return False
        if self.norm != other.norm:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def time_window(self):
        """Message field 'time_window'."""
        return self._time_window

    @time_window.setter
    def time_window(self, value):
        if __debug__:
            from geometry_msgs.msg import PoseArray
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, PoseArray) for v in value) and
                 True), \
                "The 'time_window' field must be a set or sequence and each value of type 'PoseArray'"
        self._time_window = value

    @property
    def j0(self):
        """Message field 'j0'."""
        return self._j0

    @j0.setter
    def j0(self, value):
        if __debug__:
            from geometry_msgs.msg import Point
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, Point) for v in value) and
                 True), \
                "The 'j0' field must be a set or sequence and each value of type 'Point'"
        self._j0 = value

    @property
    def q_spine(self):
        """Message field 'q_spine'."""
        return self._q_spine

    @q_spine.setter
    def q_spine(self, value):
        if __debug__:
            from geometry_msgs.msg import Quaternion
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, Quaternion) for v in value) and
                 True), \
                "The 'q_spine' field must be a set or sequence and each value of type 'Quaternion'"
        self._q_spine = value

    @property
    def norm(self):
        """Message field 'norm'."""
        return self._norm

    @norm.setter
    def norm(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'norm' array.array() must have the type code of 'd'"
            self._norm = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, float) for v in value) and
                 True), \
                "The 'norm' field must be a set or sequence and each value of type 'float'"
        self._norm = array.array('d', value)
