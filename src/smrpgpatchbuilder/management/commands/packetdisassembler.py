from django.core.management.base import BaseCommand
from randomizer.management.disassembler_common import shortify, bit, dbyte, hbyte, named, con, byte, byte_int, short, short_int, build_table, use_table_name, get_flag_string, flags, con_int, flags_short, writeline, bit_bool_from_num
from randomizer.helpers.npcmodeltables import sprite_name_table, vram_store_table, shadow_size_table

start = 0x1DB000
end = 0x1DB7FF


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-r', '--rom', dest='rom',
                            help='Path to a Mario RPG rom')

        parser.add_argument('-d', '--debug', action="store_true",
                            help='If set, dumps to a gitignored folder instead of overwriting the scripts sourced by SMRPG Randomizer')

    def handle(self, *args, **options):
        debug = options['debug']

        dest = 'randomizer/data'
        if debug:
            dest = 'randomizer/management/commands/output/disassembler'

        global rom
        rom = bytearray(open(options['rom'], 'rb').read())


        file = open("%s/packets.py" % dest, "w")
        writeline(file, '# AUTOGENERATED DO NOT EDIT!!')
        writeline(file, '# Run the following command if you need to rebuild the table')
        writeline(file, '# python manage.py packetdisassembler --rom ROM')
        writeline(file, 'from randomizer.helpers.npcmodeltables import SpriteName')
        writeline(file, 'packets = [None]* %i' % ((end + 1 - start) // 5))
        ctr = 0
        for offset in range(start, end+1, 5):
            if offset + 5 > end:
                break

            raw_data = rom[offset:(offset+5)]

            if raw_data == bytearray([0xFF] * 5):
                writeline(file, 'packets[%i] = None # 0x%06x' % (ctr, offset))
            else:
                sprite_id = 0xC0 + (raw_data[0] & 0x3F)
                sprite, _ = byte(prefix="SpriteName", table=sprite_name_table)([sprite_id])

                unknown_bytes = [raw_data[0] >> 6, raw_data[1] & 0x07, (raw_data[1] >> 3) & 0x03, raw_data[1] >> 5, raw_data[2] & 0x03, raw_data[2] >> 6, raw_data[4] >> 4]
                unknown_bits = [bit(raw_data, 2, 2), bit(raw_data, 2, 3), bit(raw_data, 2, 4)]

                shadow = bit(raw_data, 2, 5) == 1
                action = shortify(raw_data, 3) & 0x3FF

                writeline(file, 'packets[%i] = {' % (ctr))
                writeline(file, '  "sprite": %s,' % sprite)
                writeline(file, '  "shadow": %r,' % shadow)
                writeline(file, '  "action_script": %i,' % action)
                writeline(file, '  "unknown_bits": %r,' % [u == 1 for u in unknown_bits])
                writeline(file, '  "unknown_bytes": %r' % unknown_bytes)
                writeline(file, '} # 0x%06x' % (offset))
            ctr += 1

        file.close()
