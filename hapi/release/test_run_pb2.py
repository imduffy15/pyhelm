# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hapi/release/test_run.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hapi/release/test_run.proto',
  package='hapi.release',
  syntax='proto3',
  serialized_options=b'Z\007release',
  serialized_pb=b'\n\x1bhapi/release/test_run.proto\x12\x0chapi.release\x1a\x1fgoogle/protobuf/timestamp.proto\"\xf3\x01\n\x07TestRun\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x06status\x18\x02 \x01(\x0e\x32\x1c.hapi.release.TestRun.Status\x12\x0c\n\x04info\x18\x03 \x01(\t\x12.\n\nstarted_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0c\x63ompleted_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"<\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07\x46\x41ILURE\x10\x02\x12\x0b\n\x07RUNNING\x10\x03\x42\tZ\x07releaseb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_TESTRUN_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='hapi.release.TestRun.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=262,
  serialized_end=322,
)
_sym_db.RegisterEnumDescriptor(_TESTRUN_STATUS)


_TESTRUN = _descriptor.Descriptor(
  name='TestRun',
  full_name='hapi.release.TestRun',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='hapi.release.TestRun.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='hapi.release.TestRun.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='hapi.release.TestRun.info', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='started_at', full_name='hapi.release.TestRun.started_at', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='completed_at', full_name='hapi.release.TestRun.completed_at', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TESTRUN_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=322,
)

_TESTRUN.fields_by_name['status'].enum_type = _TESTRUN_STATUS
_TESTRUN.fields_by_name['started_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TESTRUN.fields_by_name['completed_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TESTRUN_STATUS.containing_type = _TESTRUN
DESCRIPTOR.message_types_by_name['TestRun'] = _TESTRUN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestRun = _reflection.GeneratedProtocolMessageType('TestRun', (_message.Message,), {
  'DESCRIPTOR' : _TESTRUN,
  '__module__' : 'hapi.release.test_run_pb2'
  # @@protoc_insertion_point(class_scope:hapi.release.TestRun)
  })
_sym_db.RegisterMessage(TestRun)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
