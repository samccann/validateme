# temperature.py - A temperature module plugin for Ansible.
# Author: Sam McCann (@samccann)
# License: GPL-3.0-or-later

from __future__ import absolute_import, annotations, division, print_function


__metaclass__ = type  # pylint: disable=C0103

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from typing import Callable


DOCUMENTATION = """
    name: temperature
    author: Sandra McCann (@samccann)
    version_added: "1.0.0"
    short_description: Convert tempurature to Fahrenheit or Celsius.
    description:
      - This module converts the given temperature from the specified unit (Fahrenheit or Celsius)
      - to the other unit.
    options:
      temp:
        description: The temperature to convert.
        type: float
        required: true
      unit:
        description: The input unit of the temperature.
        type: str
        choices:
          - fahrenheit
          - celsius
        required: true
"""

EXAMPLES = """
# Convert 79.5 Fahrenheit to Celsius

- name: Convert 79.5 Fahrenheit to Celsius
  samccann.validateme.temperature:
    temp: 79.5
    unit: fahrenheit

"""
RETURN = """
temp:
    description: The converted temperature.
    type: float
    returned: always
    sample: 26.39
"""

from ansible.module_utils.basic import AnsibleModule

def _temperature(temp: float, unit: str) -> float:
    """Converts the given temperature to the specified unit (Fahrenheit or Celsius).

    Args:
        temp: temperature to convert.
        unit: input unit of the temperature.

    Returns:
        float: The converted temperature.
    """
    if unit == "fahrenheit":
        return (temp - 32) * 5/9
    elif unit == "celsius":
        return (temp * 9/5) + 32
    else:
        raise ValueError(f"Invalid unit: {unit}")


def main():
    argument_spec = dict(
        temp=dict(type='float', required=True),
        unit=dict(type='str', required=True, choices=['fahrenheit', 'celsius'])

    )

    module = AnsibleModule(argument_spec=argument_spec)
    try:
        temp = module.params['temp']
        unit = module.params['unit']
        result = _temperature(temp, unit)
        module.exit_json(changed=False, temp=result)
    except Exception as e:
        module.fail_json(msg=str(e))



if __name__ == '__main__':  # pragma: no cover
    main()  # pragma: no cover