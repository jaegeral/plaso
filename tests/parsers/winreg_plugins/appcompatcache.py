#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for the Application Compatibility Cache key Windows Registry plugin."""

import unittest

from dfdatetime import filetime as dfdatetime_filetime
from dfvfs.path import fake_path_spec
from dfwinreg import definitions as dfwinreg_definitions
from dfwinreg import fake as dfwinreg_fake

from plaso.parsers.winreg_plugins import appcompatcache

from tests.parsers.winreg_plugins import test_lib


class TestFileEntry(object):
  """File entry object for testing purposes.

  Attributes:
    name (str): name of the file entry.
    path_spec (dfvfs.PathSpec): path specification of the file entry.
  """

  def __init__(self, name):
    """Initializes a file entry.

    Args:
      name (str): the file entry name.
    """
    super(TestFileEntry, self).__init__()
    self.name = name
    self.path_spec = fake_path_spec.FakePathSpec(location=name)

  # pylint: disable=redundant-returns-doc
  def GetStat(self):
    """Retrieves the stat object.

    Returns:
      dfvfs.VFSStat: None for testing.
    """
    return None


class AppCompatCacheWindowsRegistryPluginTest(test_lib.RegistryPluginTestCase):
  """Tests for the AppCompatCache Windows Registry plugin."""

  _TEST_KEY_PATH = '\\ControlSet001\\Control\\Session Manager\\AppCompatCache'

  _TEST_DATA_XP = bytes(bytearray([
      0xef, 0xbe, 0xad, 0xde, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00,
      0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x5c, 0x00, 0x3f, 0x00, 0x3f, 0x00, 0x5c, 0x00,
      0x43, 0x00, 0x3a, 0x00, 0x5c, 0x00, 0x57, 0x00, 0x49, 0x00, 0x4e, 0x00,
      0x44, 0x00, 0x4f, 0x00, 0x57, 0x00, 0x53, 0x00, 0x5c, 0x00, 0x73, 0x00,
      0x79, 0x00, 0x73, 0x00, 0x74, 0x00, 0x65, 0x00, 0x6d, 0x00, 0x33, 0x00,
      0x32, 0x00, 0x5c, 0x00, 0x68, 0x00, 0x74, 0x00, 0x69, 0x00, 0x63, 0x00,
      0x6f, 0x00, 0x6e, 0x00, 0x73, 0x00, 0x2e, 0x00, 0x64, 0x00, 0x6c, 0x00,
      0x6c, 0x00, 0x00, 0x00, 0x44, 0x00, 0x6f, 0x00, 0x77, 0x00, 0x6e, 0x00,
      0x6c, 0x00, 0x6f, 0x00, 0x61, 0x00, 0x64, 0x00, 0x5c, 0x00, 0x62, 0x00,
      0x37, 0x00, 0x66, 0x00, 0x30, 0x00, 0x62, 0x00, 0x32, 0x00, 0x38, 0x00,
      0x39, 0x00, 0x32, 0x00, 0x62, 0x00, 0x32, 0x00, 0x31, 0x00, 0x32, 0x00,
      0x31, 0x00, 0x31, 0x00, 0x61, 0x00, 0x35, 0x00, 0x36, 0x00, 0x33, 0x00,
      0x30, 0x00, 0x35, 0x00, 0x31, 0x00, 0x38, 0x00, 0x64, 0x00, 0x30, 0x00,
      0x35, 0x00, 0x38, 0x00, 0x66, 0x00, 0x34, 0x00, 0x38, 0x00, 0x64, 0x00,
      0x39, 0x00, 0x5c, 0x00, 0x75, 0x00, 0x70, 0x00, 0x64, 0x00, 0x61, 0x00,
      0x74, 0x00, 0x65, 0x00, 0x5c, 0x00, 0x75, 0x00, 0x70, 0x00, 0x64, 0x00,
      0x61, 0x00, 0x74, 0x00, 0x65, 0x00, 0x2e, 0x00, 0x65, 0x00, 0x78, 0x00,
      0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0xb0, 0xe9, 0x54, 0x2b, 0x7a, 0xc4, 0x01,
      0x00, 0xae, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x62, 0xd3, 0x0e, 0xc7,
      0xe9, 0x39, 0xca, 0x01]))

  _TEST_DATA_2003 = bytes(bytearray([
      0xfe, 0x0f, 0xdc, 0xba, 0x01, 0x00, 0x00, 0x00, 0x72, 0x00, 0x74, 0x00,
      0x20, 0x00, 0x00, 0x00, 0x00, 0x35, 0x86, 0x76, 0x44, 0xf2, 0xc2, 0x01,
      0x00, 0x20, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x5c, 0x00, 0x3f, 0x00,
      0x3f, 0x00, 0x5c, 0x00, 0x43, 0x00, 0x3a, 0x00, 0x5c, 0x00, 0x57, 0x00,
      0x49, 0x00, 0x4e, 0x00, 0x44, 0x00, 0x4f, 0x00, 0x57, 0x00, 0x53, 0x00,
      0x5c, 0x00, 0x4d, 0x00, 0x69, 0x00, 0x63, 0x00, 0x72, 0x00, 0x6f, 0x00,
      0x73, 0x00, 0x6f, 0x00, 0x66, 0x00, 0x74, 0x00, 0x2e, 0x00, 0x4e, 0x00,
      0x45, 0x00, 0x54, 0x00, 0x5c, 0x00, 0x46, 0x00, 0x72, 0x00, 0x61, 0x00,
      0x6d, 0x00, 0x65, 0x00, 0x77, 0x00, 0x6f, 0x00, 0x72, 0x00, 0x6b, 0x00,
      0x5c, 0x00, 0x76, 0x00, 0x31, 0x00, 0x2e, 0x00, 0x31, 0x00, 0x2e, 0x00,
      0x34, 0x00, 0x33, 0x00, 0x32, 0x00, 0x32, 0x00, 0x5c, 0x00, 0x6e, 0x00,
      0x67, 0x00, 0x65, 0x00, 0x6e, 0x00, 0x2e, 0x00, 0x65, 0x00, 0x78, 0x00,
      0x65, 0x00, 0x00, 0x00]))

  _TEST_DATA_VISTA = bytes(bytearray([
      0xfe, 0x0f, 0xdc, 0xba, 0x01, 0x00, 0x00, 0x00, 0x46, 0x00, 0x48, 0x00,
      0x20, 0x00, 0x00, 0x00, 0xc2, 0xfe, 0x87, 0x5e, 0x7b, 0xfe, 0xc6, 0x01,
      0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x5c, 0x00, 0x3f, 0x00,
      0x3f, 0x00, 0x5c, 0x00, 0x43, 0x00, 0x3a, 0x00, 0x5c, 0x00, 0x57, 0x00,
      0x69, 0x00, 0x6e, 0x00, 0x64, 0x00, 0x6f, 0x00, 0x77, 0x00, 0x73, 0x00,
      0x5c, 0x00, 0x53, 0x00, 0x59, 0x00, 0x53, 0x00, 0x54, 0x00, 0x45, 0x00,
      0x4d, 0x00, 0x33, 0x00, 0x32, 0x00, 0x5c, 0x00, 0x57, 0x00, 0x49, 0x00,
      0x53, 0x00, 0x50, 0x00, 0x54, 0x00, 0x49, 0x00, 0x53, 0x00, 0x2e, 0x00,
      0x45, 0x00, 0x58, 0x00, 0x45, 0x00, 0x00, 0x00]))

  _TEST_DATA_8_0 = bytes(bytearray([
      0x80, 0x00, 0x00, 0x00, 0x2e, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x09, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x4a, 0x01, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00,
      0x05, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x24, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x08, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x30, 0x30, 0x74, 0x73,
      0x9e, 0x6b, 0x3c, 0x8a, 0x68, 0x00, 0x00, 0x00, 0x52, 0x00, 0x53, 0x00,
      0x59, 0x00, 0x53, 0x00, 0x56, 0x00, 0x4f, 0x00, 0x4c, 0x00, 0x5c, 0x00,
      0x57, 0x00, 0x69, 0x00, 0x6e, 0x00, 0x64, 0x00, 0x6f, 0x00, 0x77, 0x00,
      0x73, 0x00, 0x5c, 0x00, 0x53, 0x00, 0x79, 0x00, 0x73, 0x00, 0x74, 0x00,
      0x65, 0x00, 0x6d, 0x00, 0x33, 0x00, 0x32, 0x00, 0x5c, 0x00, 0x77, 0x00,
      0x62, 0x00, 0x65, 0x00, 0x6d, 0x00, 0x5c, 0x00, 0x57, 0x00, 0x6d, 0x00,
      0x69, 0x00, 0x50, 0x00, 0x72, 0x00, 0x76, 0x00, 0x53, 0x00, 0x45, 0x00,
      0x2e, 0x00, 0x65, 0x00, 0x78, 0x00, 0x65, 0x00, 0x43, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x01, 0xf0, 0xa4, 0xa4, 0xbc, 0xfc, 0xed, 0xcc, 0x01,
      0x00, 0x00, 0x00, 0x00]))

  _TEST_DATA_8_1 = bytes(bytearray([
      0x80, 0x00, 0x00, 0x00, 0x09, 0x15, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x09, 0x01, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x06, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x73, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x46, 0x15, 0x00, 0x00, 0x3a, 0x00, 0x00, 0x00,
      0x47, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x38, 0x01, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x01, 0x00, 0x00, 0x00, 0x6c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x6c, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x38, 0x30, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x31, 0x30, 0x74, 0x73,
      0xbc, 0x4c, 0xa0, 0x05, 0x5e, 0x00, 0x00, 0x00, 0x46, 0x00, 0x53, 0x00,
      0x59, 0x00, 0x53, 0x00, 0x56, 0x00, 0x4f, 0x00, 0x4c, 0x00, 0x5c, 0x00,
      0x57, 0x00, 0x69, 0x00, 0x6e, 0x00, 0x64, 0x00, 0x6f, 0x00, 0x77, 0x00,
      0x73, 0x00, 0x5c, 0x00, 0x53, 0x00, 0x79, 0x00, 0x73, 0x00, 0x74, 0x00,
      0x65, 0x00, 0x6d, 0x00, 0x33, 0x00, 0x32, 0x00, 0x5c, 0x00, 0x64, 0x00,
      0x6c, 0x00, 0x6c, 0x00, 0x68, 0x00, 0x6f, 0x00, 0x73, 0x00, 0x74, 0x00,
      0x2e, 0x00, 0x65, 0x00, 0x78, 0x00, 0x65, 0x00, 0x00, 0x00, 0x7f, 0x00,
      0x00, 0x00, 0x00, 0x11, 0x00, 0x01, 0xb5, 0x1f, 0x73, 0x13, 0x34, 0x9f,
      0xce, 0x01, 0x00, 0x00, 0x00, 0x00]))

  _TEST_DATA_10 = bytes(bytearray([
      0x30, 0x00, 0x00, 0x00, 0x0a, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0xc9, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x31, 0x30, 0x74, 0x73, 0x64, 0x7e, 0xcd, 0xc9, 0xcc, 0x00, 0x00, 0x00,
      0x42, 0x00, 0x43, 0x00, 0x3a, 0x00, 0x5c, 0x00, 0x57, 0x00, 0x69, 0x00,
      0x6e, 0x00, 0x64, 0x00, 0x6f, 0x00, 0x77, 0x00, 0x73, 0x00, 0x5c, 0x00,
      0x73, 0x00, 0x79, 0x00, 0x73, 0x00, 0x74, 0x00, 0x65, 0x00, 0x6d, 0x00,
      0x33, 0x00, 0x32, 0x00, 0x5c, 0x00, 0x4d, 0x00, 0x70, 0x00, 0x53, 0x00,
      0x69, 0x00, 0x67, 0x00, 0x53, 0x00, 0x74, 0x00, 0x75, 0x00, 0x62, 0x00,
      0x2e, 0x00, 0x65, 0x00, 0x78, 0x00, 0x65, 0x00, 0x80, 0x99, 0xe3, 0x66,
      0x30, 0xd6, 0xcf, 0x01, 0x7c, 0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00,
      0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x08, 0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x10, 0x00, 0x00, 0x00,
      0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x40, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00,
      0x00, 0x04, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x03, 0x00, 0x00, 0x00,
      0x20, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x01, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00]))

  _TEST_DATA_10_CREATOR = bytes(bytearray([
      0x34, 0x00, 0x00, 0x00, 0x1a, 0x4e, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x53, 0x07, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x7a, 0x23, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0xfa, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x00, 0x00, 0x00, 0x31, 0x30, 0x74, 0x73, 0xd5, 0xf1, 0x23, 0x93,
      0xd4, 0x00, 0x00, 0x00, 0x7e, 0x00, 0x43, 0x00, 0x3a, 0x00, 0x5c, 0x00,
      0x50, 0x00, 0x72, 0x00, 0x6f, 0x00, 0x67, 0x00, 0x72, 0x00, 0x61, 0x00,
      0x6d, 0x00, 0x20, 0x00, 0x46, 0x00, 0x69, 0x00, 0x6c, 0x00, 0x65, 0x00,
      0x73, 0x00, 0x20, 0x00, 0x28, 0x00, 0x78, 0x00, 0x38, 0x00, 0x36, 0x00,
      0x29, 0x00, 0x5c, 0x00, 0x4e, 0x00, 0x56, 0x00, 0x49, 0x00, 0x44, 0x00,
      0x49, 0x00, 0x41, 0x00, 0x20, 0x00, 0x43, 0x00, 0x6f, 0x00, 0x72, 0x00,
      0x70, 0x00, 0x6f, 0x00, 0x72, 0x00, 0x61, 0x00, 0x74, 0x00, 0x69, 0x00,
      0x6f, 0x00, 0x6e, 0x00, 0x5c, 0x00, 0x33, 0x00, 0x44, 0x00, 0x20, 0x00,
      0x56, 0x00, 0x69, 0x00, 0x73, 0x00, 0x69, 0x00, 0x6f, 0x00, 0x6e, 0x00,
      0x5c, 0x00, 0x6e, 0x00, 0x76, 0x00, 0x73, 0x00, 0x74, 0x00, 0x72, 0x00,
      0x65, 0x00, 0x67, 0x00, 0x2e, 0x00, 0x65, 0x00, 0x78, 0x00, 0x65, 0x00,
      0xe9, 0x09, 0x99, 0x7b, 0xa8, 0x9e, 0xd2, 0x01, 0x48, 0x00, 0x00, 0x00,
      0x00, 0x02, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x08, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x4c, 0x01, 0x00, 0x00,
      0x00, 0x04, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x03, 0x00, 0x00, 0x00,
      0x40, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00,
      0x20, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
      0x00, 0x01, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00]))

  def _CreateTestKey(self, time_string, binary_data):
    """Creates Registry keys and values for testing.

    Args:
      time_string (str): key last written date and time.
      binary_data (bytes): AppCompatCache Registry value data.

    Returns:
      dfwinreg.WinRegistryKey: a Windows Registry key.
    """
    filetime = dfdatetime_filetime.Filetime()
    filetime.CopyFromDateTimeString(time_string)
    registry_key = dfwinreg_fake.FakeWinRegistryKey(
        'AppCompatCache', key_path=self._TEST_KEY_PATH,
        last_written_time=filetime.timestamp, offset=1456)

    registry_value = dfwinreg_fake.FakeWinRegistryValue(
        'AppCompatCache', data=binary_data,
        data_type=dfwinreg_definitions.REG_BINARY)
    registry_key.AddValue(registry_value)

    return registry_key

  def testFilters(self):
    """Tests the FILTERS class attribute."""
    plugin = appcompatcache.AppCompatCacheWindowsRegistryPlugin()

    key_path = (
        'HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\'
        'Session Manager\\AppCompatibility')
    self._AssertFiltersOnKeyPath(plugin, key_path)

    key_path = (
        'HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\'
        'Session Manager\\AppCompatCache')
    self._AssertFiltersOnKeyPath(plugin, key_path)

    self._AssertNotFiltersOnKeyPath(plugin, 'HKEY_LOCAL_MACHINE\\Bogus')

  def testProcessWindowsXP(self):
    """Tests the Process function for Windows XP AppCompatCache data."""
    test_file_entry = TestFileEntry('SYSTEM-XP')
    registry_key = self._CreateTestKey(
        '2015-06-15 11:53:37.043061', self._TEST_DATA_XP)
    plugin = appcompatcache.AppCompatCacheWindowsRegistryPlugin()
    storage_writer = self._ParseKeyWithPlugin(
        registry_key, plugin, file_entry=test_file_entry,
        parser_chain=plugin.plugin_name)

    self.assertEqual(storage_writer.number_of_events, 2)
    self.assertEqual(storage_writer.number_of_extraction_warnings, 0)
    self.assertEqual(storage_writer.number_of_recovery_warnings, 0)

    events = list(storage_writer.GetEvents())

    expected_event_values = {
        'date_time': '2004-08-04 14:00:00.0000000',
        'data_type': 'windows:registry:appcompatcache',
        'entry_index': 1,
        'key_path': self._TEST_KEY_PATH,
        'path': '\\??\\C:\\WINDOWS\\system32\\hticons.dll'}

    self.CheckEventValues(storage_writer, events[0], expected_event_values)

  def testProcessWindows2003(self):
    """Tests the Process function for Windows 2003 AppCompatCache data."""
    test_file_entry = TestFileEntry('SYSTEM-Windows2003')
    registry_key = self._CreateTestKey(
        '2015-06-15 11:53:37.043061', self._TEST_DATA_2003)
    plugin = appcompatcache.AppCompatCacheWindowsRegistryPlugin()
    storage_writer = self._ParseKeyWithPlugin(
        registry_key, plugin, file_entry=test_file_entry,
        parser_chain=plugin.plugin_name)

    self.assertEqual(storage_writer.number_of_events, 1)
    self.assertEqual(storage_writer.number_of_extraction_warnings, 0)
    self.assertEqual(storage_writer.number_of_recovery_warnings, 0)

    events = list(storage_writer.GetEvents())

    expected_event_values = {
        'date_time': '2003-03-24 20:32:18.0000000',
        'data_type': 'windows:registry:appcompatcache',
        'entry_index': 1,
        'key_path': self._TEST_KEY_PATH,
        'path': (
            '\\??\\C:\\WINDOWS\\Microsoft.NET\\Framework\\v1.1.4322\\ngen.exe')}

    self.CheckEventValues(storage_writer, events[0], expected_event_values)

    # TODO: implement 64 bit

  def testProcessWindowsVista(self):
    """Tests the Process function for Windows Vista AppCompatCache data."""
    test_file_entry = TestFileEntry('SYSTEM-Vista')
    registry_key = self._CreateTestKey(
        '2015-06-15 11:53:37.043061', self._TEST_DATA_VISTA)
    plugin = appcompatcache.AppCompatCacheWindowsRegistryPlugin()
    storage_writer = self._ParseKeyWithPlugin(
        registry_key, plugin, file_entry=test_file_entry,
        parser_chain=plugin.plugin_name)

    self.assertEqual(storage_writer.number_of_events, 1)
    self.assertEqual(storage_writer.number_of_extraction_warnings, 0)
    self.assertEqual(storage_writer.number_of_recovery_warnings, 0)

    events = list(storage_writer.GetEvents())

    expected_event_values = {
        'date_time': '2006-11-02 12:35:24.7041218',
        'data_type': 'windows:registry:appcompatcache',
        'entry_index': 1,
        'key_path': self._TEST_KEY_PATH,
        'path': '\\??\\C:\\Windows\\SYSTEM32\\WISPTIS.EXE'}

    self.CheckEventValues(storage_writer, events[0], expected_event_values)

    # TODO: implement 64 bit

  def testProcessWindows7(self):
    """Tests the Process function for Windows 7 AppCompatCache data."""
    test_file_entry = self._GetTestFileEntry(['SYSTEM'])
    key_path = (
        'HKEY_LOCAL_MACHINE\\System\\ControlSet001\\Control\\'
        'Session Manager\\AppCompatCache')

    win_registry = self._GetWinRegistryFromFileEntry(test_file_entry)
    registry_key = win_registry.GetKeyByPath(key_path)
    plugin = appcompatcache.AppCompatCacheWindowsRegistryPlugin()
    storage_writer = self._ParseKeyWithPlugin(
        registry_key, plugin, file_entry=test_file_entry,
        parser_chain=plugin.plugin_name)

    self.assertEqual(storage_writer.number_of_events, 330)
    self.assertEqual(storage_writer.number_of_extraction_warnings, 0)
    self.assertEqual(storage_writer.number_of_recovery_warnings, 0)

    events = list(storage_writer.GetEvents())

    expected_event_values = {
        'date_time': '2012-04-04 01:46:37.9329644',
        'data_type': 'windows:registry:appcompatcache',
        'entry_index': 10,
        # This should just be the plugin name, as we're invoking it directly,
        # and not through the parser.
        'parser': plugin.plugin_name,
        'path': '\\??\\C:\\Windows\\PSEXESVC.EXE'}

    self.CheckEventValues(storage_writer, events[9], expected_event_values)

    # TODO: implement 64 bit

  def testProcessWindows8_0(self):
    """Tests the Process function for Windows 8.0 AppCompatCache data."""
    test_file_entry = TestFileEntry('SYSTEM-Windows8.0')
    registry_key = self._CreateTestKey(
        '2015-06-15 11:53:37.043061', self._TEST_DATA_8_0)
    plugin = appcompatcache.AppCompatCacheWindowsRegistryPlugin()
    storage_writer = self._ParseKeyWithPlugin(
        registry_key, plugin, file_entry=test_file_entry,
        parser_chain=plugin.plugin_name)

    self.assertEqual(storage_writer.number_of_events, 1)
    self.assertEqual(storage_writer.number_of_extraction_warnings, 0)
    self.assertEqual(storage_writer.number_of_recovery_warnings, 0)

    events = list(storage_writer.GetEvents())

    expected_event_values = {
        'date_time': '2012-02-18 05:18:23.9350000',
        'data_type': 'windows:registry:appcompatcache',
        'entry_index': 1,
        'key_path': self._TEST_KEY_PATH,
        'path': 'SYSVOL\\Windows\\System32\\wbem\\WmiPrvSE.exe'}

    self.CheckEventValues(storage_writer, events[0], expected_event_values)

  def testProcessWindows8_1(self):
    """Tests the Process function for Windows 8.1 AppCompatCache data."""
    test_file_entry = TestFileEntry('SYSTEM-Windows8.1')
    registry_key = self._CreateTestKey(
        '2015-06-15 11:53:37.043061', self._TEST_DATA_8_1)
    plugin = appcompatcache.AppCompatCacheWindowsRegistryPlugin()
    storage_writer = self._ParseKeyWithPlugin(
        registry_key, plugin, file_entry=test_file_entry,
        parser_chain=plugin.plugin_name)

    self.assertEqual(storage_writer.number_of_events, 1)
    self.assertEqual(storage_writer.number_of_extraction_warnings, 0)
    self.assertEqual(storage_writer.number_of_recovery_warnings, 0)

    events = list(storage_writer.GetEvents())

    expected_event_values = {
        'date_time': '2013-08-22 12:35:25.3750709',
        'data_type': 'windows:registry:appcompatcache',
        'entry_index': 1,
        'key_path': self._TEST_KEY_PATH,
        'path': 'SYSVOL\\Windows\\System32\\dllhost.exe'}

    self.CheckEventValues(storage_writer, events[0], expected_event_values)

  def testProcessWindows10(self):
    """Tests the Process function for Windows 10 AppCompatCache data."""
    test_file_entry = TestFileEntry('SYSTEM-Windows10')
    registry_key = self._CreateTestKey(
        '2015-06-15 11:53:37.043061', self._TEST_DATA_10)
    plugin = appcompatcache.AppCompatCacheWindowsRegistryPlugin()
    storage_writer = self._ParseKeyWithPlugin(
        registry_key, plugin, file_entry=test_file_entry,
        parser_chain=plugin.plugin_name)

    self.assertEqual(storage_writer.number_of_events, 1)
    self.assertEqual(storage_writer.number_of_extraction_warnings, 0)
    self.assertEqual(storage_writer.number_of_recovery_warnings, 0)

    events = list(storage_writer.GetEvents())

    expected_event_values = {
        'date_time': '2014-09-22 06:42:39.0000000',
        'data_type': 'windows:registry:appcompatcache',
        'entry_index': 1,
        'key_path': self._TEST_KEY_PATH,
        'path': 'C:\\Windows\\system32\\MpSigStub.exe'}

    self.CheckEventValues(storage_writer, events[0], expected_event_values)

  def testProcessWindows10Creator(self):
    """Tests the Process function for Windows 10 Creator AppCompatCache data."""
    test_file_entry = TestFileEntry('SYSTEM-Windows10-Creator')
    registry_key = self._CreateTestKey(
        '2015-06-15 11:53:37.043061', self._TEST_DATA_10_CREATOR)
    plugin = appcompatcache.AppCompatCacheWindowsRegistryPlugin()
    storage_writer = self._ParseKeyWithPlugin(
        registry_key, plugin, file_entry=test_file_entry,
        parser_chain=plugin.plugin_name)

    self.assertEqual(storage_writer.number_of_events, 1)
    self.assertEqual(storage_writer.number_of_extraction_warnings, 0)
    self.assertEqual(storage_writer.number_of_recovery_warnings, 0)

    events = list(storage_writer.GetEvents())

    expected_event_values = {
        'date_time': '2017-03-16 22:56:01.2487145',
        'data_type': 'windows:registry:appcompatcache',
        'entry_index': 1,
        'key_path': self._TEST_KEY_PATH,
        'path': (
            'C:\\Program Files (x86)\\NVIDIA Corporation\\3D Vision\\'
            'nvstreg.exe')}

    self.CheckEventValues(storage_writer, events[0], expected_event_values)


if __name__ == '__main__':
  unittest.main()
