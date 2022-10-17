"""
`pytest` testing framework file for Entrysat
"""

import satnogsdecoders.decoder as decoder
from tests.shared_methods import check_type, load_objects


def test_answer():  # pylint: disable=too-many-locals
    """
    `pytest` entry point
    """

    example1 = bytearray([
        0x8c, 0x6c, 0x96, 0xa8, 0x82, 0x40, 0xe0, 0x9e, 0x9c, 0x60, 0x64, 0x8c,
        0xa4, 0x61, 0x03, 0xf0, 0x00, 0x00, 0x00, 0x00, 0x08, 0x01, 0xc7, 0x29,
        0x00, 0x12, 0x10, 0x03, 0x19, 0x23, 0xfe, 0xbd, 0xcd, 0x17, 0x06, 0x00,
        0xf1, 0x6b, 0x00, 0x00, 0x9e, 0xa0, 0x98, 0x1f, 0xc6, 0xb0, 0x09, 0xbe,
        0xfe, 0x23
    ])
    example1_keys = 23
    packets = [example1]
    dut = 'Entrysat'
    result = []

    for frame in packets:
        result = load_objects(decoder, dut, frame)
        count = check_type(result)
        if frame == example1:
            assert count == example1_keys