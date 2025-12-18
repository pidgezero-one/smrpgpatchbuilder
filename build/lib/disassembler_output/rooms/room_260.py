# R260_GAME_INTRO_FOREST_MAZE_JUMPING_ON_WIGGLER
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
        allow_extra_sprite_buffer=True,
        extra_sprite_buffer_size=1,
        buffers = [
            Buffer(
                buffer_type=BufferType.FOUR_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.THREE_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.COINS,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            )
        ],
        full_palette_buffer=True
    ),
    music=M0030_LONGLONGAGO,
    entrance_event=E1718_EMPTY,
    objects=[
        RegularNPC( # 0
            npc=npcs.WIGGLER_HEAD_NPC,
            initiator=EventInitiator.ANYTHING_EXCEPT_PRESS_A,
            event_script=E1720_EMPTY,
            action_script=A0160_SEQUENCE_LOOPING_ON,
            speed=1,
            visible=False,
            x=5,
            y=30,
            z=3,
            z_half=False,
            direction=SOUTHEAST,
            face_on_trigger=False,
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
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3,
        ),
        RegularClone( # 1
            npc=npcs.WIGGLER_BODY_SEGMENT_NPC,
            event_script=E1720_EMPTY,
            action_script=A0160_SEQUENCE_LOOPING_ON,
            visible=False,
            x=5,
            y=30,
            z=3,
            z_half=False,
            direction=SOUTHEAST,
        ),
        RegularClone( # 2
            npc=npcs.WIGGLER_BODY_SEGMENT_NPC,
            event_script=E1720_EMPTY,
            action_script=A0160_SEQUENCE_LOOPING_ON,
            visible=False,
            x=5,
            y=30,
            z=3,
            z_half=False,
            direction=SOUTHEAST,
        ),
        RegularClone( # 3
            npc=npcs.WIGGLER_BODY_SEGMENT_NPC,
            event_script=E1720_EMPTY,
            action_script=A0160_SEQUENCE_LOOPING_ON,
            visible=False,
            x=5,
            y=30,
            z=3,
            z_half=False,
            direction=SOUTHEAST,
        ),
        RegularNPC( # 4
            npc=npcs.COIN_NPC,
            initiator=EventInitiator.NONE,
            event_script=E1551_BANK_1F_RETURN_EVENT,
            action_script=A0160_SEQUENCE_LOOPING_ON,
            visible=False,
            x=0,
            y=0,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
            face_on_trigger=False,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=False,
            cant_walk_up_stairs=False,
            cant_walk_under=False,
            cant_pass_walls=False,
            cant_jump_through=False,
            cant_pass_npcs=False,
            byte3_bit5=False,
            cant_walk_through=False,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3,
        ),
    ]
)
