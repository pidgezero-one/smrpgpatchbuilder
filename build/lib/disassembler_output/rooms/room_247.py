# R247_GAME_INTRO_TADPOLE_POND_MARIO_SUMMONS_TADPOLES
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
        ally_sprite_buffer_size=2,
        allow_extra_sprite_buffer=False,
        extra_sprite_buffer_size=0,
        buffers = [
            Buffer(
                buffer_type=BufferType.EMPTY_3,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.FOUR_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_1024,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.EMPTY_3,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            )
        ],
        full_palette_buffer=True
    ),
    music=M0000_CURRENT,
    entrance_event=E1521_CLONE_RESERVED,
    objects=[
        RegularNPC( # 0
            npc=npcs.TADPOLE_NPC,
            initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
            event_script=E1112_FROG_COIN_EMPORIUM,
            action_script=A0154_TADPOLE_POND_TADPOLE_DEFAULT,
            visible=False,
            x=12,
            y=47,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
            face_on_trigger=False,
            cant_enter_doors=True,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=True,
            cant_walk_up_stairs=True,
            cant_walk_under=True,
            cant_pass_walls=False,
            cant_jump_through=False,
            cant_pass_npcs=False,
            byte3_bit5=True,
            cant_walk_through=True,
            byte3_bit7=True,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3,
        ),
        RegularClone( # 1
            npc=npcs.TADPOLE_NPC,
            event_script=E1116_JUICE_BAR,
            action_script=A0154_TADPOLE_POND_TADPOLE_DEFAULT,
            visible=False,
            x=15,
            y=49,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
        ),
        RegularClone( # 2
            npc=npcs.TADPOLE_NPC,
            event_script=E1114_SUMMON_TADPOLE_SHOPS,
            action_script=A0154_TADPOLE_POND_TADPOLE_DEFAULT,
            visible=False,
            x=14,
            y=43,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
        ),
        RegularClone( # 3
            npc=npcs.TADPOLE_NPC,
            event_script=E1114_SUMMON_TADPOLE_SHOPS,
            action_script=A0154_TADPOLE_POND_TADPOLE_DEFAULT,
            visible=False,
            x=17,
            y=45,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
        ),
        RegularClone( # 4
            npc=npcs.TADPOLE_NPC,
            event_script=E1114_SUMMON_TADPOLE_SHOPS,
            action_script=A0154_TADPOLE_POND_TADPOLE_DEFAULT,
            visible=False,
            x=16,
            y=39,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
        ),
        RegularClone( # 5
            npc=npcs.TADPOLE_NPC,
            event_script=E1114_SUMMON_TADPOLE_SHOPS,
            action_script=A0154_TADPOLE_POND_TADPOLE_DEFAULT,
            visible=False,
            x=19,
            y=41,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
        ),
        RegularClone( # 6
            npc=npcs.TADPOLE_NPC,
            event_script=E1114_SUMMON_TADPOLE_SHOPS,
            action_script=A0154_TADPOLE_POND_TADPOLE_DEFAULT,
            visible=False,
            x=18,
            y=35,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
        ),
        RegularClone( # 7
            npc=npcs.TADPOLE_NPC,
            event_script=E1114_SUMMON_TADPOLE_SHOPS,
            action_script=A0154_TADPOLE_POND_TADPOLE_DEFAULT,
            visible=False,
            x=21,
            y=37,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
        ),
    ]
)
