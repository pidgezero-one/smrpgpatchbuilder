# R415_NIMBUS_LAND_SMALL_PLATFORM_AFTER_NIMBUS_CASTLE_THRONE_PATHS
# pyright: reportWildcardImportFromLibrary=false
from smrpgpatchbuilder.datatypes.levels.classes import ObjectType, EventInitiator, PostBattleBehaviour, Direction, EdgeDirection, ExitType, BufferType, BufferSpace, VramStore, ShadowSize
from smrpgpatchbuilder.datatypes.levels.classes import Buffer, Partition, DestinationProps, RoomExit, MapExit, Event, BattlePackNPC, RegularNPC, ChestNPC, BattlePackClone, RegularClone, ChestClone, Room
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from . import npcs
from ..variables.room_names import *
from ..variables.overworld_area_names import *
from ..variables.music_names import *
from ..variables.event_script_names import *
from ..variables.action_script_names import *
room = Room(
    partition=Partition(
        ally_sprite_buffer_size=1,
        allow_extra_sprite_buffer=False,
        extra_sprite_buffer_size=0,
        buffers = [
            Buffer(
                buffer_type=BufferType.THREE_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.THREE_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.THREE_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            )
        ],
        full_palette_buffer=True
    ),
    music=M0000_CURRENT,
    entrance_event=E3737_NIMBUS_CASTLE_BACK_EXIT_LOADER,
    events=[
        Event(
            event=E3672_NIMBUS_CASTLE_BACK_EXIT_FALL,
            x=28,
            y=119,
            z=2,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=3,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False,
        ),
        Event(
            event=E3672_NIMBUS_CASTLE_BACK_EXIT_FALL,
            x=29,
            y=120,
            z=2,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=3,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False,
        ),
        Event(
            event=E3672_NIMBUS_CASTLE_BACK_EXIT_FALL,
            x=29,
            y=121,
            z=2,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=3,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False,
        ),
    ],
    exits=[
        RoomExit(
            x=28,
            y=122,
            z=4,
            f=EdgeDirection.SOUTHEAST,
            length=1,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD,
            show_message=False,
            dst_x=8,
            dst_y=81,
            dst_z=0,
            dst_z_half=False,
            dst_f=SOUTHWEST,
            x_bit_7=False,
        ),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.MARIO_WALKING_DOWN_LEFT_NPC_2,
            initiator=EventInitiator.NONE,
            event_script=E3636_EMPTY,
            action_script=A0015_DO_NOTHING,
            visible=False,
            x=19,
            y=40,
            z=2,
            z_half=False,
            direction=SOUTHWEST,
            face_on_trigger=True,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=False,
            cant_walk_up_stairs=False,
            cant_walk_under=False,
            cant_pass_walls=False,
            cant_jump_through=False,
            cant_pass_npcs=True,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=False,
            cant_move_if_in_air=False,
            byte7_upper2=3,
        ),
    ]
)
