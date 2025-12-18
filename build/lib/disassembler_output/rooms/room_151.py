# R151_GAME_INTRO_BOOSTER_HILL
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
        extra_sprite_buffer_size=0,
        buffers = [
            Buffer(
                buffer_type=BufferType.EMPTY_3,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.THREE_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.FOUR_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            )
        ],
        full_palette_buffer=True
    ),
    music=M0030_LONGLONGAGO,
    entrance_event=E1551_BANK_1F_RETURN_EVENT,
    objects=[
        RegularNPC( # 0
            npc=npcs.ROLLING_BARREL_NPC,
            initiator=EventInitiator.ANYTHING_EXCEPT_PRESS_A,
            event_script=E1742_EMPTY,
            action_script=A0160_SEQUENCE_LOOPING_ON,
            visible=True,
            x=1,
            y=50,
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
            cant_pass_npcs=True,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3,
        ),
        RegularClone( # 1
            npc=npcs.ROLLING_BARREL_NPC,
            event_script=E1742_EMPTY,
            action_script=A0160_SEQUENCE_LOOPING_ON,
            visible=True,
            x=2,
            y=48,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
        ),
        RegularClone( # 2
            npc=npcs.ROLLING_BARREL_NPC,
            event_script=E1742_EMPTY,
            action_script=A0160_SEQUENCE_LOOPING_ON,
            visible=True,
            x=3,
            y=46,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
        ),
        RegularNPC( # 3
            npc=npcs.RED_BOMB_NPC,
            initiator=EventInitiator.ANYTHING_EXCEPT_PRESS_A,
            event_script=E1551_BANK_1F_RETURN_EVENT,
            action_script=A0160_SEQUENCE_LOOPING_ON,
            visible=True,
            x=8,
            y=65,
            z=0,
            z_half=False,
            direction=NORTHWEST,
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
        RegularClone( # 4
            npc=npcs.RED_BOMB_NPC,
            event_script=E1551_BANK_1F_RETURN_EVENT,
            action_script=A0160_SEQUENCE_LOOPING_ON,
            visible=True,
            x=9,
            y=63,
            z=0,
            z_half=False,
            direction=NORTHWEST,
        ),
        RegularClone( # 5
            npc=npcs.RED_BOMB_NPC,
            event_script=E1551_BANK_1F_RETURN_EVENT,
            action_script=A0160_SEQUENCE_LOOPING_ON,
            visible=True,
            x=10,
            y=61,
            z=0,
            z_half=False,
            direction=NORTHWEST,
        ),
    ]
)
