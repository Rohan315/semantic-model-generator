# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: semantic_model.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14semantic_model.proto\x12\x18semantic_model_generator\"\x88\x01\n\tDimension\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08synonyms\x18\x02 \x03(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0c\n\x04\x65xpr\x18\x04 \x01(\t\x12\x11\n\tdata_type\x18\x05 \x01(\t\x12\x0e\n\x06unique\x18\x06 \x01(\x08\x12\x15\n\rsample_values\x18\x07 \x03(\t\"\x8c\x01\n\rTimeDimension\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08synonyms\x18\x02 \x03(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0c\n\x04\x65xpr\x18\x04 \x01(\t\x12\x11\n\tdata_type\x18\x05 \x01(\t\x12\x0e\n\x06unique\x18\x06 \x01(\x08\x12\x15\n\rsample_values\x18\x07 \x03(\t\"\xbe\x01\n\x07Measure\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08synonyms\x18\x02 \x03(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0c\n\x04\x65xpr\x18\x04 \x01(\t\x12\x11\n\tdata_type\x18\x05 \x01(\t\x12\x46\n\x13\x64\x65\x66\x61ult_aggregation\x18\x06 \x01(\x0e\x32).semantic_model_generator.AggregationType\x12\x15\n\rsample_values\x18\x07 \x03(\t\"P\n\x0bNamedFilter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08synonyms\x18\x02 \x03(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0c\n\x04\x65xpr\x18\x04 \x01(\t\"F\n\x13\x46ullyQualifiedTable\x12\x10\n\x08\x64\x61tabase\x18\x01 \x01(\t\x12\x0e\n\x06schema\x18\x02 \x01(\t\x12\r\n\x05table\x18\x03 \x01(\t\"\xe7\x02\n\x05Table\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08synonyms\x18\x02 \x03(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x41\n\nbase_table\x18\x04 \x01(\x0b\x32-.semantic_model_generator.FullyQualifiedTable\x12\x37\n\ndimensions\x18\t \x03(\x0b\x32#.semantic_model_generator.Dimension\x12@\n\x0ftime_dimensions\x18\n \x03(\x0b\x32\'.semantic_model_generator.TimeDimension\x12\x33\n\x08measures\x18\x0b \x03(\x0b\x32!.semantic_model_generator.Measure\x12\x36\n\x07\x66ilters\x18\x08 \x03(\x0b\x32%.semantic_model_generator.NamedFilter\"c\n\rSemanticModel\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12/\n\x06tables\x18\x03 \x03(\x0b\x32\x1f.semantic_model_generator.Table*~\n\x0f\x41ggregationType\x12\x1c\n\x18\x61ggregation_type_unknown\x10\x00\x12\x07\n\x03sum\x10\x01\x12\x07\n\x03\x61vg\x10\x02\x12\n\n\x06median\x10\x07\x12\x07\n\x03min\x10\x03\x12\x07\n\x03max\x10\x04\x12\t\n\x05\x63ount\x10\x05\x12\x12\n\x0e\x63ount_distinct\x10\x06\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'semantic_model_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_AGGREGATIONTYPE']._serialized_start=1142
  _globals['_AGGREGATIONTYPE']._serialized_end=1268
  _globals['_DIMENSION']._serialized_start=51
  _globals['_DIMENSION']._serialized_end=187
  _globals['_TIMEDIMENSION']._serialized_start=190
  _globals['_TIMEDIMENSION']._serialized_end=330
  _globals['_MEASURE']._serialized_start=333
  _globals['_MEASURE']._serialized_end=523
  _globals['_NAMEDFILTER']._serialized_start=525
  _globals['_NAMEDFILTER']._serialized_end=605
  _globals['_FULLYQUALIFIEDTABLE']._serialized_start=607
  _globals['_FULLYQUALIFIEDTABLE']._serialized_end=677
  _globals['_TABLE']._serialized_start=680
  _globals['_TABLE']._serialized_end=1039
  _globals['_SEMANTICMODEL']._serialized_start=1041
  _globals['_SEMANTICMODEL']._serialized_end=1140
# @@protoc_insertion_point(module_scope)