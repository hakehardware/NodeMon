# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spacemesh/v1/smesher.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from spacemesh.v1 import smesher_types_pb2 as spacemesh_dot_v1_dot_smesher__types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aspacemesh/v1/smesher.proto\x12\x0cspacemesh.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a spacemesh/v1/smesher_types.proto2\xa1\t\n\x0eSmesherService\x12\x46\n\nIsSmeshing\x12\x16.google.protobuf.Empty\x1a .spacemesh.v1.IsSmeshingResponse\x12X\n\rStartSmeshing\x12\".spacemesh.v1.StartSmeshingRequest\x1a#.spacemesh.v1.StartSmeshingResponse\x12U\n\x0cStopSmeshing\x12!.spacemesh.v1.StopSmeshingRequest\x1a\".spacemesh.v1.StopSmeshingResponse\x12\x44\n\tSmesherID\x12\x16.google.protobuf.Empty\x1a\x1f.spacemesh.v1.SmesherIDResponse\x12\x42\n\x08\x43oinbase\x12\x16.google.protobuf.Empty\x1a\x1e.spacemesh.v1.CoinbaseResponse\x12R\n\x0bSetCoinbase\x12 .spacemesh.v1.SetCoinbaseRequest\x1a!.spacemesh.v1.SetCoinbaseResponse\x12>\n\x06MinGas\x12\x16.google.protobuf.Empty\x1a\x1c.spacemesh.v1.MinGasResponse\x12L\n\tSetMinGas\x12\x1e.spacemesh.v1.SetMinGasRequest\x1a\x1f.spacemesh.v1.SetMinGasResponse\x12\x61\n\x10\x45stimatedRewards\x12%.spacemesh.v1.EstimatedRewardsRequest\x1a&.spacemesh.v1.EstimatedRewardsResponse\x12P\n\x0fPostSetupStatus\x12\x16.google.protobuf.Empty\x1a%.spacemesh.v1.PostSetupStatusResponse\x12^\n\x15PostSetupStatusStream\x12\x16.google.protobuf.Empty\x1a+.spacemesh.v1.PostSetupStatusStreamResponse0\x01\x12g\n\x12PostSetupProviders\x12\'.spacemesh.v1.PostSetupProvidersRequest\x1a(.spacemesh.v1.PostSetupProvidersResponse\x12\x46\n\nPostConfig\x12\x16.google.protobuf.Empty\x1a .spacemesh.v1.PostConfigResponse\x12\x64\n\x11UpdatePoetServers\x12&.spacemesh.v1.UpdatePoetServersRequest\x1a\'.spacemesh.v1.UpdatePoetServersResponseB4Z2github.com/spacemeshos/api/release/go/spacemesh/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spacemesh.v1.smesher_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2github.com/spacemeshos/api/release/go/spacemesh/v1'
  _globals['_SMESHERSERVICE']._serialized_start=108
  _globals['_SMESHERSERVICE']._serialized_end=1293
# @@protoc_insertion_point(module_scope)
