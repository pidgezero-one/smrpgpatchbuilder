# R382_NIMBUS_LAND_ENTRANCE_NO_TRAMPOLINESEXITS
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
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    objects=[
        RegularNPC( # 0
            npc=npcs.EMPTY_NPC,
            initiator=EventInitiator.NONE,
            event_script=E0541_DEBUG_DIALOG,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=17,
            y=20,
            z=4,
            z_half=False,
            direction=SOUTHWEST,
            face_on_trigger=False,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=False,
            cant_float=False,
            cant_walk_up_stairs=False,
            cant_walk_under=False,
            cant_pass_walls=False,
            cant_jump_through=True,
            cant_pass_npcs=False,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=False,
            cant_move_if_in_air=False,
            byte7_upper2=3,
        ),
        RegularClone( # 1
            npc=npcs.EMPTY_NPC,
            event_script=E0541_DEBUG_DIALOG,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=17,
            y=20,
            z=4,
            z_half=False,
            direction=SOUTHWEST,
        ),
        RegularClone( # 2
            npc=npcs.EMPTY_NPC,
            event_script=E0541_DEBUG_DIALOG,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=17,
            y=20,
            z=4,
            z_half=False,
            direction=SOUTHWEST,
        ),
        RegularClone( # 3
            npc=npcs.EMPTY_NPC,
            event_script=E0541_DEBUG_DIALOG,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=17,
            y=20,
            z=4,
            z_half=False,
            direction=SOUTHWEST,
        ),
        RegularClone( # 4
            npc=npcs.EMPTY_NPC,
            event_script=E0541_DEBUG_DIALOG,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=17,
            y=20,
            z=4,
            z_half=False,
            direction=SOUTHWEST,
        ),
        RegularClone( # 5
            npc=npcs.EMPTY_NPC,
            event_script=E0541_DEBUG_DIALOG,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=17,
            y=20,
            z=4,
            z_half=False,
            direction=SOUTHWEST,
        ),
        RegularClone( # 6
            npc=npcs.EMPTY_NPC,
            event_script=E0541_DEBUG_DIALOG,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=17,
            y=20,
            z=4,
            z_half=False,
            direction=SOUTHWEST,
        ),
        RegularClone( # 7
            npc=npcs.EMPTY_NPC,
            event_script=E0541_DEBUG_DIALOG,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=17,
            y=20,
            z=4,
            z_half=False,
            direction=SOUTHWEST,
        ),
    ]
)
