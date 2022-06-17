# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: safeentry.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fsafeentry.proto\x12\tsafeentry\"Q\n\x0f\x43heckIn_Request\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04nric\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x10\n\x08\x64\x61tetime\x18\x04 \x01(\t\" \n\rCheckIn_Reply\x12\x0f\n\x07message\x18\x01 \x01(\t\"I\n\x07Request\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04nric\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x10\n\x08\x64\x61tetime\x18\x04 \x01(\t\"\x18\n\x05Reply\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1f\n\x0fHistory_Request\x12\x0c\n\x04nric\x18\x01 \x01(\t\";\n\rHistory_Reply\x12*\n\thistories\x18\x01 \x03(\x0b\x32\x17.safeentry.History_Item\"e\n\x0cHistory_Item\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04nric\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x12\n\ncheckin_dt\x18\x04 \x01(\t\x12\x13\n\x0b\x63heckout_dt\x18\x05 \x01(\t2\x81\x02\n\x10SafeEntryService\x12\x41\n\x07\x43heckin\x12\x1a.safeentry.CheckIn_Request\x1a\x18.safeentry.CheckIn_Reply\"\x00\x12\x32\n\x08\x43heckout\x12\x12.safeentry.Request\x1a\x10.safeentry.Reply\"\x00\x12\x41\n\x07History\x12\x1a.safeentry.History_Request\x1a\x18.safeentry.History_Reply\"\x00\x12\x33\n\tContacted\x12\x12.safeentry.Request\x1a\x10.safeentry.Reply\"\x00\x62\x06proto3')



_CHECKIN_REQUEST = DESCRIPTOR.message_types_by_name['CheckIn_Request']
_CHECKIN_REPLY = DESCRIPTOR.message_types_by_name['CheckIn_Reply']
_REQUEST = DESCRIPTOR.message_types_by_name['Request']
_REPLY = DESCRIPTOR.message_types_by_name['Reply']
_HISTORY_REQUEST = DESCRIPTOR.message_types_by_name['History_Request']
_HISTORY_REPLY = DESCRIPTOR.message_types_by_name['History_Reply']
_HISTORY_ITEM = DESCRIPTOR.message_types_by_name['History_Item']
CheckIn_Request = _reflection.GeneratedProtocolMessageType('CheckIn_Request', (_message.Message,), {
  'DESCRIPTOR' : _CHECKIN_REQUEST,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:safeentry.CheckIn_Request)
  })
_sym_db.RegisterMessage(CheckIn_Request)

CheckIn_Reply = _reflection.GeneratedProtocolMessageType('CheckIn_Reply', (_message.Message,), {
  'DESCRIPTOR' : _CHECKIN_REPLY,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:safeentry.CheckIn_Reply)
  })
_sym_db.RegisterMessage(CheckIn_Reply)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:safeentry.Request)
  })
_sym_db.RegisterMessage(Request)

Reply = _reflection.GeneratedProtocolMessageType('Reply', (_message.Message,), {
  'DESCRIPTOR' : _REPLY,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:safeentry.Reply)
  })
_sym_db.RegisterMessage(Reply)

History_Request = _reflection.GeneratedProtocolMessageType('History_Request', (_message.Message,), {
  'DESCRIPTOR' : _HISTORY_REQUEST,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:safeentry.History_Request)
  })
_sym_db.RegisterMessage(History_Request)

History_Reply = _reflection.GeneratedProtocolMessageType('History_Reply', (_message.Message,), {
  'DESCRIPTOR' : _HISTORY_REPLY,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:safeentry.History_Reply)
  })
_sym_db.RegisterMessage(History_Reply)

History_Item = _reflection.GeneratedProtocolMessageType('History_Item', (_message.Message,), {
  'DESCRIPTOR' : _HISTORY_ITEM,
  '__module__' : 'safeentry_pb2'
  # @@protoc_insertion_point(class_scope:safeentry.History_Item)
  })
_sym_db.RegisterMessage(History_Item)

_SAFEENTRYSERVICE = DESCRIPTOR.services_by_name['SafeEntryService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CHECKIN_REQUEST._serialized_start=30
  _CHECKIN_REQUEST._serialized_end=111
  _CHECKIN_REPLY._serialized_start=113
  _CHECKIN_REPLY._serialized_end=145
  _REQUEST._serialized_start=147
  _REQUEST._serialized_end=220
  _REPLY._serialized_start=222
  _REPLY._serialized_end=246
  _HISTORY_REQUEST._serialized_start=248
  _HISTORY_REQUEST._serialized_end=279
  _HISTORY_REPLY._serialized_start=281
  _HISTORY_REPLY._serialized_end=340
  _HISTORY_ITEM._serialized_start=342
  _HISTORY_ITEM._serialized_end=443
  _SAFEENTRYSERVICE._serialized_start=446
  _SAFEENTRYSERVICE._serialized_end=703
# @@protoc_insertion_point(module_scope)
