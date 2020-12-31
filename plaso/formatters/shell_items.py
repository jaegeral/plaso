# -*- coding: utf-8 -*-
"""Windows shell item custom event formatter helpers."""

from __future__ import unicode_literals

from plaso.formatters import interface
from plaso.formatters import manager


class ShellItemFileEntryEventFormatter(interface.CustomEventFormatterHelper):
  """Custom formatter for Windows shell item file entry event values."""

  DATA_TYPE = 'windows:shell_item:file_entry'

  def FormatEventValues(self, event_values):
    """Formats event values using the helper.

    Args:
      event_values (dict[str, object]): event values.
    """
    event_values['file_entry_name'] = event_values.get('long_name', None)
    if not event_values['file_entry_name']:
      event_values['file_entry_name'] = event_values.get('name', None)


manager.FormattersManager.RegisterEventFormatterHelper(
    ShellItemFileEntryEventFormatter)
