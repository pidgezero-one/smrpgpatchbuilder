import pytest
from typing import Optional, Type, List
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.battlefields import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.colours import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.controller_inputs import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.intro_title_text import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.layers import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.packets import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_types import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.scenes import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.tutorials import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.variables import *
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.ids import *
from smrpgpatchbuilder.datatypes.overworld_scripts.ids import *
from smrpgpatchbuilder.datatypes.dialogs.ids.dialog_ids import *
from smrpgpatchbuilder.datatypes.items.implementations import *
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (
    EventScriptBank,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.types.classes import (
    UsableEventScriptCommand,
)
from smrpgpatchbuilder.datatypes.scripts_common.classes import (
    ScriptBankTooLongException,
    IdentifierException,
    InvalidCommandArgumentException,
    InvalidOpcodeException,
    RenderException,
)

from dataclasses import dataclass


@dataclass
class Case:
    label: str
    commands_factory: callable
    expected_bytes: Optional[List[int]] = None
    exception: Optional[str] = None
    exception_type: Optional[Type] = None


test_cases = [
    #
    # Basic (no GOTOs) command tests
    #
    Case(
        "Loop 10 frames",
        commands_factory=lambda: [StartLoopNFrames(10)],
        expected_bytes=[0xD5, 0x0A, 0x00],
    ),
    Case(
        label="StartLoopNFrames",
        commands_factory=lambda: [StartLoopNFrames()],
        expected_bytes=[],
    ),
    Case(
        label="StartLoopNTimes",
        commands_factory=lambda: [StartLoopNTimes()],
        expected_bytes=[],
    ),
    Case(label="EndLoop", commands_factory=lambda: [EndLoop()], expected_bytes=[]),
    Case(
        label="MoveScriptToMainThread",
        commands_factory=lambda: [MoveScriptToMainThread()],
        expected_bytes=[],
    ),
    Case(
        label="MoveScriptToBackgroundThread1",
        commands_factory=lambda: [MoveScriptToBackgroundThread1()],
        expected_bytes=[],
    ),
    Case(
        label="MoveScriptToBackgroundThread2",
        commands_factory=lambda: [MoveScriptToBackgroundThread2()],
        expected_bytes=[],
    ),
    Case(label="Pause", commands_factory=lambda: [Pause()], expected_bytes=[]),
    Case(
        label="RememberLastObject",
        commands_factory=lambda: [RememberLastObject()],
        expected_bytes=[],
    ),
    Case(
        label="ResumeBackgroundEvent",
        commands_factory=lambda: [ResumeBackgroundEvent()],
        expected_bytes=[],
    ),
    Case(
        label="RunBackgroundEvent",
        commands_factory=lambda: [RunBackgroundEvent()],
        expected_bytes=[],
    ),
    Case(
        label="RunBackgroundEventWithPause",
        commands_factory=lambda: [RunBackgroundEventWithPause()],
        expected_bytes=[],
    ),
    Case(
        label="RunBackgroundEventWithPauseReturnOnExit",
        commands_factory=lambda: [RunBackgroundEventWithPauseReturnOnExit()],
        expected_bytes=[],
    ),
    Case(
        label="RunEventAtReturn",
        commands_factory=lambda: [RunEventAtReturn()],
        expected_bytes=[],
    ),
    Case(
        label="RunEventAsSubroutine",
        commands_factory=lambda: [RunEventAsSubroutine()],
        expected_bytes=[],
    ),
    Case(
        label="StopAllBackgroundEvents",
        commands_factory=lambda: [StopAllBackgroundEvents()],
        expected_bytes=[],
    ),
    Case(
        label="StopBackgroundEvent",
        commands_factory=lambda: [StopBackgroundEvent()],
        expected_bytes=[],
    ),
    Case(label="Return", commands_factory=lambda: [Return()], expected_bytes=[]),
    Case(label="ReturnAll", commands_factory=lambda: [ReturnAll()], expected_bytes=[]),
    Case(label="ReturnFD", commands_factory=lambda: [ReturnFD()], expected_bytes=[]),
    Case(
        label="UnknownCommand",
        commands_factory=lambda: [UnknownCommand()],
        expected_bytes=[],
    ),
    Case(
        label="If0210Bits012ClearDoNotJump",
        commands_factory=lambda: [If0210Bits012ClearDoNotJump()],
        expected_bytes=[],
    ),
    Case(
        label="SetMem704XAt7000Bit",
        commands_factory=lambda: [SetMem704XAt7000Bit()],
        expected_bytes=[],
    ),
    Case(
        label="ClearMem704XAt7000Bit",
        commands_factory=lambda: [ClearMem704XAt7000Bit()],
        expected_bytes=[],
    ),
    Case(
        label="Move70107015To7016701B",
        commands_factory=lambda: [Move70107015To7016701B()],
        expected_bytes=[],
    ),
    Case(
        label="Move7016701BTo70107015",
        commands_factory=lambda: [Move7016701BTo70107015()],
        expected_bytes=[],
    ),
    Case(
        label="SetVarToConst",
        commands_factory=lambda: [SetVarToConst()],
        expected_bytes=[],
    ),
    Case(
        label="ReadFromAddress",
        commands_factory=lambda: [ReadFromAddress()],
        expected_bytes=[],
    ),
    Case(
        label="Set7000To7FMemVar",
        commands_factory=lambda: [Set7000To7FMemVar()],
        expected_bytes=[],
    ),
    Case(label="SetBit", commands_factory=lambda: [SetBit()], expected_bytes=[]),
    Case(label="ClearBit", commands_factory=lambda: [ClearBit()], expected_bytes=[]),
    Case(
        label="Set0158Bit3Offset",
        commands_factory=lambda: [Set0158Bit3Offset()],
        expected_bytes=[],
    ),
    Case(
        label="Set0158Bit7Offset",
        commands_factory=lambda: [Set0158Bit7Offset()],
        expected_bytes=[],
    ),
    Case(
        label="Clear0158Bit7Offset",
        commands_factory=lambda: [Clear0158Bit7Offset()],
        expected_bytes=[],
    ),
    Case(
        label="Clear7016To7018AndIsolate701AHighByteIf7018Bit0Set",
        commands_factory=lambda: [Clear7016To7018AndIsolate701AHighByteIf7018Bit0Set()],
        expected_bytes=[],
    ),
    Case(
        label="CopyVarToVar",
        commands_factory=lambda: [CopyVarToVar()],
        expected_bytes=[],
    ),
    Case(
        label="StoreBytesTo0335And0556",
        commands_factory=lambda: [StoreBytesTo0335And0556()],
        expected_bytes=[],
    ),
    Case(
        label="Store00To0248",
        commands_factory=lambda: [Store00To0248()],
        expected_bytes=[],
    ),
    Case(
        label="Store00To0334",
        commands_factory=lambda: [Store00To0334()],
        expected_bytes=[],
    ),
    Case(
        label="Store01To0248",
        commands_factory=lambda: [Store01To0248()],
        expected_bytes=[],
    ),
    Case(
        label="Store01To0335",
        commands_factory=lambda: [Store01To0335()],
        expected_bytes=[],
    ),
    Case(
        label="Store02To0248",
        commands_factory=lambda: [Store02To0248()],
        expected_bytes=[],
    ),
    Case(
        label="StoreFFTo0335",
        commands_factory=lambda: [StoreFFTo0335()],
        expected_bytes=[],
    ),
    Case(
        label="Set7000ToMinecartTimer",
        commands_factory=lambda: [Set7000ToMinecartTimer()],
        expected_bytes=[],
    ),
    Case(
        label="StoreSetBits",
        commands_factory=lambda: [StoreSetBits()],
        expected_bytes=[],
    ),
    Case(label="SwapVars", commands_factory=lambda: [SwapVars()], expected_bytes=[]),
    Case(
        label="AddConstToVar",
        commands_factory=lambda: [AddConstToVar()],
        expected_bytes=[],
    ),
    Case(label="Inc", commands_factory=lambda: [Inc()], expected_bytes=[]),
    Case(label="Dec", commands_factory=lambda: [Dec()], expected_bytes=[]),
    Case(
        label="AddVarTo7000",
        commands_factory=lambda: [AddVarTo7000()],
        expected_bytes=[],
    ),
    Case(
        label="DecVarFrom7000",
        commands_factory=lambda: [DecVarFrom7000()],
        expected_bytes=[],
    ),
    Case(
        label="GenerateRandomNumFromRangeVar",
        commands_factory=lambda: [GenerateRandomNumFromRangeVar()],
        expected_bytes=[],
    ),
    Case(
        label="SetVarToRandom",
        commands_factory=lambda: [SetVarToRandom()],
        expected_bytes=[],
    ),
    Case(
        label="CompareVarToConst",
        commands_factory=lambda: [CompareVarToConst()],
        expected_bytes=[],
    ),
    Case(
        label="Compare7000ToVar",
        commands_factory=lambda: [Compare7000ToVar()],
        expected_bytes=[],
    ),
    Case(
        label="Mem7000AndConst",
        commands_factory=lambda: [Mem7000AndConst()],
        expected_bytes=[],
    ),
    Case(
        label="Mem7000AndVar",
        commands_factory=lambda: [Mem7000AndVar()],
        expected_bytes=[],
    ),
    Case(
        label="Mem7000OrConst",
        commands_factory=lambda: [Mem7000OrConst()],
        expected_bytes=[],
    ),
    Case(
        label="Mem7000OrVar",
        commands_factory=lambda: [Mem7000OrVar()],
        expected_bytes=[],
    ),
    Case(
        label="Mem7000XorConst",
        commands_factory=lambda: [Mem7000XorConst()],
        expected_bytes=[],
    ),
    Case(
        label="Mem7000XorVar",
        commands_factory=lambda: [Mem7000XorVar()],
        expected_bytes=[],
    ),
    Case(
        label="VarShiftLeft",
        commands_factory=lambda: [VarShiftLeft()],
        expected_bytes=[],
    ),
    Case(
        label="MultiplyAndAddMem3148StoreToOffsrt7fB000PlusOutputX2",
        commands_factory=lambda: [
            MultiplyAndAddMem3148StoreToOffsrt7fB000PlusOutputX2()
        ],
        expected_bytes=[],
    ),
    Case(
        label="Xor3105With01",
        commands_factory=lambda: [Xor3105With01()],
        expected_bytes=[],
    ),
    Case(
        label="SetAsyncActionScript",
        commands_factory=lambda: [SetAsyncActionScript()],
        expected_bytes=[],
    ),
    Case(
        label="SetSyncActionScript",
        commands_factory=lambda: [SetSyncActionScript()],
        expected_bytes=[],
    ),
    Case(
        label="SetTempAsyncActionScript",
        commands_factory=lambda: [SetTempAsyncActionScript()],
        expected_bytes=[],
    ),
    Case(
        label="SetTempSyncActionScript",
        commands_factory=lambda: [SetTempSyncActionScript()],
        expected_bytes=[],
    ),
    Case(
        label="UnsyncActionScript",
        commands_factory=lambda: [UnsyncActionScript()],
        expected_bytes=[],
    ),
    Case(
        label="SummonObjectToSpecificLevel",
        commands_factory=lambda: [SummonObjectToSpecificLevel()],
        expected_bytes=[],
    ),
    Case(
        label="SummonObjectToCurrentLevel",
        commands_factory=lambda: [SummonObjectToCurrentLevel()],
        expected_bytes=[],
    ),
    Case(
        label="SummonObjectToCurrentLevelAtMariosCoords",
        commands_factory=lambda: [SummonObjectToCurrentLevelAtMariosCoords()],
        expected_bytes=[],
    ),
    Case(
        label="SummonObjectAt70A8ToCurrentLevel",
        commands_factory=lambda: [SummonObjectAt70A8ToCurrentLevel()],
        expected_bytes=[],
    ),
    Case(
        label="RemoveObjectFromSpecificLevel",
        commands_factory=lambda: [RemoveObjectFromSpecificLevel()],
        expected_bytes=[],
    ),
    Case(
        label="RemoveObjectFromCurrentLevel",
        commands_factory=lambda: [RemoveObjectFromCurrentLevel()],
        expected_bytes=[],
    ),
    Case(
        label="RemoveObjectAt70A8FromCurrentLevel",
        commands_factory=lambda: [RemoveObjectAt70A8FromCurrentLevel()],
        expected_bytes=[],
    ),
    Case(
        label="PauseActionScript",
        commands_factory=lambda: [PauseActionScript()],
        expected_bytes=[],
    ),
    Case(
        label="ResumeActionScript",
        commands_factory=lambda: [ResumeActionScript()],
        expected_bytes=[],
    ),
    Case(
        label="EnableObjectTrigger",
        commands_factory=lambda: [EnableObjectTrigger()],
        expected_bytes=[],
    ),
    Case(
        label="DisableObjectTrigger",
        commands_factory=lambda: [DisableObjectTrigger()],
        expected_bytes=[],
    ),
    Case(
        label="EnableObjectTriggerInSpecificLevel",
        commands_factory=lambda: [EnableObjectTriggerInSpecificLevel()],
        expected_bytes=[],
    ),
    Case(
        label="DisableObjectTriggerInSpecificLevel",
        commands_factory=lambda: [DisableObjectTriggerInSpecificLevel()],
        expected_bytes=[],
    ),
    Case(
        label="EnableTriggerOfObjectAt70A8InCurrentLevel",
        commands_factory=lambda: [EnableTriggerOfObjectAt70A8InCurrentLevel()],
        expected_bytes=[],
    ),
    Case(
        label="DisableTriggerOfObjectAt70A8InCurrentLevel",
        commands_factory=lambda: [DisableTriggerOfObjectAt70A8InCurrentLevel()],
        expected_bytes=[],
    ),
    Case(
        label="StopEmbeddedActionScript",
        commands_factory=lambda: [StopEmbeddedActionScript()],
        expected_bytes=[],
    ),
    Case(
        label="ResetCoords", commands_factory=lambda: [ResetCoords()], expected_bytes=[]
    ),
    Case(
        label="FreezeAllNPCsUntilReturn",
        commands_factory=lambda: [FreezeAllNPCsUntilReturn()],
        expected_bytes=[],
    ),
    Case(
        label="UnfreezeAllNPCs",
        commands_factory=lambda: [UnfreezeAllNPCs()],
        expected_bytes=[],
    ),
    Case(
        label="FreezeCamera",
        commands_factory=lambda: [FreezeCamera()],
        expected_bytes=[],
    ),
    Case(
        label="UnfreezeCamera",
        commands_factory=lambda: [UnfreezeCamera()],
        expected_bytes=[],
    ),
    Case(
        label="ReactivateObject70A8TriggerIfMarioOnTopOfIt",
        commands_factory=lambda: [ReactivateObject70A8TriggerIfMarioOnTopOfIt()],
        expected_bytes=[],
    ),
    Case(
        label="Set7000ToObjectCoord",
        commands_factory=lambda: [Set7000ToObjectCoord()],
        expected_bytes=[],
    ),
    Case(
        label="Set70107015ToObjectXYZ",
        commands_factory=lambda: [Set70107015ToObjectXYZ()],
        expected_bytes=[],
    ),
    Case(
        label="Set7016701BToObjectXYZ",
        commands_factory=lambda: [Set7016701BToObjectXYZ()],
        expected_bytes=[],
    ),
    Case(
        label="SetObjectMemoryToVar",
        commands_factory=lambda: [SetObjectMemoryToVar()],
        expected_bytes=[],
    ),
    Case(
        label="EnableControls",
        commands_factory=lambda: [EnableControls()],
        expected_bytes=[],
    ),
    Case(
        label="EnableControlsUntilReturn",
        commands_factory=lambda: [EnableControlsUntilReturn()],
        expected_bytes=[],
    ),
    Case(
        label="Set7000ToPressedButton",
        commands_factory=lambda: [Set7000ToPressedButton()],
        expected_bytes=[],
    ),
    Case(
        label="Set7000ToTappedButton",
        commands_factory=lambda: [Set7000ToTappedButton()],
        expected_bytes=[],
    ),
    Case(label="AddCoins", commands_factory=lambda: [AddCoins()], expected_bytes=[]),
    Case(
        label="Dec7000FromCoins",
        commands_factory=lambda: [Dec7000FromCoins()],
        expected_bytes=[],
    ),
    Case(
        label="AddFrogCoins",
        commands_factory=lambda: [AddFrogCoins()],
        expected_bytes=[],
    ),
    Case(
        label="Dec7000FromFrogCoins",
        commands_factory=lambda: [Dec7000FromFrogCoins()],
        expected_bytes=[],
    ),
    Case(
        label="Add7000ToCurrentFP",
        commands_factory=lambda: [Add7000ToCurrentFP()],
        expected_bytes=[],
    ),
    Case(
        label="Dec7000FromCurrentFP",
        commands_factory=lambda: [Dec7000FromCurrentFP()],
        expected_bytes=[],
    ),
    Case(
        label="Add7000ToMaxFP",
        commands_factory=lambda: [Add7000ToMaxFP()],
        expected_bytes=[],
    ),
    Case(
        label="Dec7000FromCurrentHP",
        commands_factory=lambda: [Dec7000FromCurrentHP()],
        expected_bytes=[],
    ),
    Case(
        label="EquipItemToCharacter",
        commands_factory=lambda: [EquipItemToCharacter()],
        expected_bytes=[],
    ),
    Case(
        label="IncEXPByPacket",
        commands_factory=lambda: [IncEXPByPacket()],
        expected_bytes=[],
    ),
    Case(
        label="CharacterJoinsParty",
        commands_factory=lambda: [CharacterJoinsParty()],
        expected_bytes=[],
    ),
    Case(
        label="CharacterLeavesParty",
        commands_factory=lambda: [CharacterLeavesParty()],
        expected_bytes=[],
    ),
    Case(
        label="Store70A7ToEquipsInventory",
        commands_factory=lambda: [Store70A7ToEquipsInventory()],
        expected_bytes=[],
    ),
    Case(
        label="AddToInventory",
        commands_factory=lambda: [AddToInventory()],
        expected_bytes=[],
    ),
    Case(
        label="RemoveOneOfItemFromInventory",
        commands_factory=lambda: [RemoveOneOfItemFromInventory()],
        expected_bytes=[],
    ),
    Case(
        label="RestoreAllFP",
        commands_factory=lambda: [RestoreAllFP()],
        expected_bytes=[],
    ),
    Case(
        label="RestoreAllHP",
        commands_factory=lambda: [RestoreAllHP()],
        expected_bytes=[],
    ),
    Case(
        label="SetEXPPacketTo7000",
        commands_factory=lambda: [SetEXPPacketTo7000()],
        expected_bytes=[],
    ),
    Case(
        label="Set7000ToIDOfMemberInSlot",
        commands_factory=lambda: [Set7000ToIDOfMemberInSlot()],
        expected_bytes=[],
    ),
    Case(
        label="Set7000ToPartySize",
        commands_factory=lambda: [Set7000ToPartySize()],
        expected_bytes=[],
    ),
    Case(
        label="StoreItemAt70A7QuantityTo7000",
        commands_factory=lambda: [StoreItemAt70A7QuantityTo7000()],
        expected_bytes=[],
    ),
    Case(
        label="StoreCharacterEquipmentTo7000",
        commands_factory=lambda: [StoreCharacterEquipmentTo7000()],
        expected_bytes=[],
    ),
    Case(
        label="StoreCurrentFPTo7000",
        commands_factory=lambda: [StoreCurrentFPTo7000()],
        expected_bytes=[],
    ),
    Case(
        label="StoreEmptyItemInventorySlotCountTo7000",
        commands_factory=lambda: [StoreEmptyItemInventorySlotCountTo7000()],
        expected_bytes=[],
    ),
    Case(
        label="StoreCoinCountTo7000",
        commands_factory=lambda: [StoreCoinCountTo7000()],
        expected_bytes=[],
    ),
    Case(
        label="StoreItemAmountTo7000",
        commands_factory=lambda: [StoreItemAmountTo7000()],
        expected_bytes=[],
    ),
    Case(
        label="StoreFrogCoinCountTo7000",
        commands_factory=lambda: [StoreFrogCoinCountTo7000()],
        expected_bytes=[],
    ),
    Case(
        label="MarioGlows", commands_factory=lambda: [MarioGlows()], expected_bytes=[]
    ),
    Case(
        label="MarioStopsGlowing",
        commands_factory=lambda: [MarioStopsGlowing()],
        expected_bytes=[],
    ),
    Case(
        label="PaletteSet", commands_factory=lambda: [PaletteSet()], expected_bytes=[]
    ),
    Case(
        label="PaletteSetMorphs",
        commands_factory=lambda: [PaletteSetMorphs()],
        expected_bytes=[],
    ),
    Case(
        label="PauseScriptUntilEffectDone",
        commands_factory=lambda: [PauseScriptUntilEffectDone()],
        expected_bytes=[],
    ),
    Case(
        label="PixelateLayers",
        commands_factory=lambda: [PixelateLayers()],
        expected_bytes=[],
    ),
    Case(
        label="PrioritySet", commands_factory=lambda: [PrioritySet()], expected_bytes=[]
    ),
    Case(
        label="ResetPrioritySet",
        commands_factory=lambda: [ResetPrioritySet()],
        expected_bytes=[],
    ),
    Case(
        label="ScreenFlashesWithColour",
        commands_factory=lambda: [ScreenFlashesWithColour()],
        expected_bytes=[],
    ),
    Case(
        label="TintLayers", commands_factory=lambda: [TintLayers()], expected_bytes=[]
    ),
    Case(
        label="CircleMaskExpandFromScreenCenter",
        commands_factory=lambda: [CircleMaskExpandFromScreenCenter()],
        expected_bytes=[],
    ),
    Case(
        label="CircleMaskShrinkToScreenCenter",
        commands_factory=lambda: [CircleMaskShrinkToScreenCenter()],
        expected_bytes=[],
    ),
    Case(
        label="CircleMaskShrinkToObject",
        commands_factory=lambda: [CircleMaskShrinkToObject()],
        expected_bytes=[],
    ),
    Case(
        label="StarMaskExpandFromScreenCenter",
        commands_factory=lambda: [StarMaskExpandFromScreenCenter()],
        expected_bytes=[],
    ),
    Case(
        label="StarMaskShrinkToScreenCenter",
        commands_factory=lambda: [StarMaskShrinkToScreenCenter()],
        expected_bytes=[],
    ),
    Case(
        label="FadeInFromBlack",
        commands_factory=lambda: [FadeInFromBlack()],
        expected_bytes=[],
    ),
    Case(
        label="FadeInFromColour",
        commands_factory=lambda: [FadeInFromColour()],
        expected_bytes=[],
    ),
    Case(
        label="FadeOutToBlack",
        commands_factory=lambda: [FadeOutToBlack()],
        expected_bytes=[],
    ),
    Case(
        label="FadeOutToColour",
        commands_factory=lambda: [FadeOutToColour()],
        expected_bytes=[],
    ),
    Case(
        label="InitiateBattleMask",
        commands_factory=lambda: [InitiateBattleMask()],
        expected_bytes=[],
    ),
    Case(
        label="SlowDownMusicTempoBy",
        commands_factory=lambda: [SlowDownMusicTempoBy()],
        expected_bytes=[],
    ),
    Case(
        label="SpeedUpMusicTempoBy",
        commands_factory=lambda: [SpeedUpMusicTempoBy()],
        expected_bytes=[],
    ),
    Case(
        label="ReduceMusicPitchBy",
        commands_factory=lambda: [ReduceMusicPitchBy()],
        expected_bytes=[],
    ),
    Case(
        label="IncreaseMusicPitchBy",
        commands_factory=lambda: [IncreaseMusicPitchBy()],
        expected_bytes=[],
    ),
    Case(
        label="DeactivateSoundChannels",
        commands_factory=lambda: [DeactivateSoundChannels()],
        expected_bytes=[],
    ),
    Case(
        label="FadeInMusic", commands_factory=lambda: [FadeInMusic()], expected_bytes=[]
    ),
    Case(
        label="FadeOutMusic",
        commands_factory=lambda: [FadeOutMusic()],
        expected_bytes=[],
    ),
    Case(
        label="FadeOutMusicFDA3",
        commands_factory=lambda: [FadeOutMusicFDA3()],
        expected_bytes=[],
    ),
    Case(
        label="FadeOutMusicToVolume",
        commands_factory=lambda: [FadeOutMusicToVolume()],
        expected_bytes=[],
    ),
    Case(
        label="FadeOutSoundToVolume",
        commands_factory=lambda: [FadeOutSoundToVolume()],
        expected_bytes=[],
    ),
    Case(label="PlayMusic", commands_factory=lambda: [PlayMusic()], expected_bytes=[]),
    Case(
        label="PlayMusicAtCurrentVolume",
        commands_factory=lambda: [PlayMusicAtCurrentVolume()],
        expected_bytes=[],
    ),
    Case(
        label="PlayMusicAtDefaultVolume",
        commands_factory=lambda: [PlayMusicAtDefaultVolume()],
        expected_bytes=[],
    ),
    Case(label="PlaySound", commands_factory=lambda: [PlaySound()], expected_bytes=[]),
    Case(
        label="PlaySoundBalance",
        commands_factory=lambda: [PlaySoundBalance()],
        expected_bytes=[],
    ),
    Case(
        label="PlaySoundBalanceFD9D",
        commands_factory=lambda: [PlaySoundBalanceFD9D()],
        expected_bytes=[],
    ),
    Case(
        label="SlowDownMusic",
        commands_factory=lambda: [SlowDownMusic()],
        expected_bytes=[],
    ),
    Case(
        label="SpeedUpMusicToDefault",
        commands_factory=lambda: [SpeedUpMusicToDefault()],
        expected_bytes=[],
    ),
    Case(label="StopMusic", commands_factory=lambda: [StopMusic()], expected_bytes=[]),
    Case(
        label="StopMusicFD9F",
        commands_factory=lambda: [StopMusicFD9F()],
        expected_bytes=[],
    ),
    Case(
        label="StopMusicFDA0",
        commands_factory=lambda: [StopMusicFDA0()],
        expected_bytes=[],
    ),
    Case(
        label="StopMusicFDA1",
        commands_factory=lambda: [StopMusicFDA1()],
        expected_bytes=[],
    ),
    Case(
        label="StopMusicFDA2",
        commands_factory=lambda: [StopMusicFDA2()],
        expected_bytes=[],
    ),
    Case(
        label="StopMusicFDA6",
        commands_factory=lambda: [StopMusicFDA6()],
        expected_bytes=[],
    ),
    Case(label="StopSound", commands_factory=lambda: [StopSound()], expected_bytes=[]),
    Case(
        label="AppendDialogAt7000ToCurrentDialog",
        commands_factory=lambda: [AppendDialogAt7000ToCurrentDialog()],
        expected_bytes=[],
    ),
    Case(
        label="CloseDialog", commands_factory=lambda: [CloseDialog()], expected_bytes=[]
    ),
    Case(
        label="PauseScriptResumeOnNextDialogPageA",
        commands_factory=lambda: [PauseScriptResumeOnNextDialogPageA()],
        expected_bytes=[],
    ),
    Case(
        label="PauseScriptResumeOnNextDialogPageB",
        commands_factory=lambda: [PauseScriptResumeOnNextDialogPageB()],
        expected_bytes=[],
    ),
    Case(label="RunDialog", commands_factory=lambda: [RunDialog()], expected_bytes=[]),
    Case(
        label="RunDialogForDuration",
        commands_factory=lambda: [RunDialogForDuration()],
        expected_bytes=[],
    ),
    Case(
        label="UnsyncDialog",
        commands_factory=lambda: [UnsyncDialog()],
        expected_bytes=[],
    ),
    Case(label="EnterArea", commands_factory=lambda: [EnterArea()], expected_bytes=[]),
    Case(
        label="ApplyTileModToLevel",
        commands_factory=lambda: [ApplyTileModToLevel()],
        expected_bytes=[],
    ),
    Case(
        label="ApplySolidityModToLevel",
        commands_factory=lambda: [ApplySolidityModToLevel()],
        expected_bytes=[],
    ),
    Case(
        label="ExitToWorldMap",
        commands_factory=lambda: [ExitToWorldMap()],
        expected_bytes=[],
    ),
    Case(
        label="Set7000ToCurrentLevel",
        commands_factory=lambda: [Set7000ToCurrentLevel()],
        expected_bytes=[],
    ),
    Case(
        label="DisplayIntroTitleText",
        commands_factory=lambda: [DisplayIntroTitleText()],
        expected_bytes=[],
    ),
    Case(
        label="ExorCrashesIntoKeep",
        commands_factory=lambda: [ExorCrashesIntoKeep()],
        expected_bytes=[],
    ),
    Case(
        label="RunMenuOrEventSequence",
        commands_factory=lambda: [RunMenuOrEventSequence()],
        expected_bytes=[],
    ),
    Case(
        label="OpenSaveMenu",
        commands_factory=lambda: [OpenSaveMenu()],
        expected_bytes=[],
    ),
    Case(label="OpenShop", commands_factory=lambda: [OpenShop()], expected_bytes=[]),
    Case(
        label="PauseScriptIfMenuOpen",
        commands_factory=lambda: [PauseScriptIfMenuOpen()],
        expected_bytes=[],
    ),
    Case(
        label="ResetAndChooseGame",
        commands_factory=lambda: [ResetAndChooseGame()],
        expected_bytes=[],
    ),
    Case(label="ResetGame", commands_factory=lambda: [ResetGame()], expected_bytes=[]),
    Case(
        label="RunEndingCredits",
        commands_factory=lambda: [RunEndingCredits()],
        expected_bytes=[],
    ),
    Case(
        label="RunEventSequence",
        commands_factory=lambda: [RunEventSequence()],
        expected_bytes=[],
    ),
    Case(
        label="RunLevelupBonusSequence",
        commands_factory=lambda: [RunLevelupBonusSequence()],
        expected_bytes=[],
    ),
    Case(
        label="RunMenuTutorial",
        commands_factory=lambda: [RunMenuTutorial()],
        expected_bytes=[],
    ),
    Case(
        label="RunMolevilleMountainIntroSequence",
        commands_factory=lambda: [RunMolevilleMountainIntroSequence()],
        expected_bytes=[],
    ),
    Case(
        label="RunMolevilleMountainSequence",
        commands_factory=lambda: [RunMolevilleMountainSequence()],
        expected_bytes=[],
    ),
    Case(
        label="RunStarPieceSequence",
        commands_factory=lambda: [RunStarPieceSequence()],
        expected_bytes=[],
    ),
    Case(
        label="StartBattleAtBattlefield",
        commands_factory=lambda: [StartBattleAtBattlefield()],
        expected_bytes=[],
    ),
    Case(
        label="StartBattleWithPackAt700E",
        commands_factory=lambda: [StartBattleWithPackAt700E()],
        expected_bytes=[],
    ),
    #
    # Tests with GOTOs
    #
    Case(
        "Basic GOTO",
        commands_factory=lambda: [
            StopSound(),
            Set7000ToTappedButton(identifier="jmp_here"),
            Jmp(destinations=["jmp_here"]),
        ],
        expected_bytes=[0x9B, 0xCB, 0xD2, 0x03, 0x00],
    ),
    Case(
        "Should fail if GOTO destination doesn't match anything",
        commands_factory=lambda: [
            StopSound(),
            Set7000ToTappedButton(identifier="jmp_fails"),
            Jmp(destinations=["jmp_here"]),
        ],
        exception="couldn't find destination jmp_here",
        exception_type=IdentifierException,
    ),
    Case(
        "Should fail if GOTO finds multiple matches",
        commands_factory=lambda: [
            StopSound(),
            Set7000ToTappedButton(identifier="jmp_here"),
            Jmp(destinations=["jmp_here"]),
            Return(identifier="jmp_here"),
        ],
        exception="duplicate command identifier found: jmp_here",
        exception_type=IdentifierException,
    ),
    Case(
        "Should not fail if GOTO destination uses illegal override format",
        commands_factory=lambda: [
            StopSound(),
            Set7000ToTappedButton(),
            Jmp(destinations=["ILLEGAL_JUMP_0001"]),
        ],
        expected_bytes=[0x9B, 0xCB, 0xD2, 0x01, 0x00],
    ),
    Case(label="Jmp", commands_factory=lambda: [Jmp()], expected_bytes=[]),
    Case(
        label="JmpToEvent", commands_factory=lambda: [JmpToEvent()], expected_bytes=[]
    ),
    Case(
        label="JmpToStartOfThisScript",
        commands_factory=lambda: [JmpToStartOfThisScript()],
        expected_bytes=[],
    ),
    Case(
        label="JmpToStartOfThisScriptFA",
        commands_factory=lambda: [JmpToStartOfThisScriptFA()],
        expected_bytes=[],
    ),
    Case(
        label="JmpToSubroutine",
        commands_factory=lambda: [JmpToSubroutine()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIf316DIs3",
        commands_factory=lambda: [JmpIf316DIs3()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIf7000AllBitsClear",
        commands_factory=lambda: [JmpIf7000AllBitsClear()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIf7000AnyBitsSet",
        commands_factory=lambda: [JmpIf7000AnyBitsSet()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfBitSet", commands_factory=lambda: [JmpIfBitSet()], expected_bytes=[]
    ),
    Case(
        label="JmpIfBitClear",
        commands_factory=lambda: [JmpIfBitClear()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfLoadedMemoryIs0",
        commands_factory=lambda: [JmpIfLoadedMemoryIs0()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfLoadedMemoryIsAboveOrEqual0",
        commands_factory=lambda: [JmpIfLoadedMemoryIsAboveOrEqual0()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfLoadedMemoryIsBelow0",
        commands_factory=lambda: [JmpIfLoadedMemoryIsBelow0()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfLoadedMemoryIsNot0",
        commands_factory=lambda: [JmpIfLoadedMemoryIsNot0()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfMem704XAt7000BitSet",
        commands_factory=lambda: [JmpIfMem704XAt7000BitSet()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfMem704XAt7000BitClear",
        commands_factory=lambda: [JmpIfMem704XAt7000BitClear()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfRandom2of3",
        commands_factory=lambda: [JmpIfRandom2of3()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfRandom1of2",
        commands_factory=lambda: [JmpIfRandom1of2()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfComparisonResultIsGreaterOrEqual",
        commands_factory=lambda: [JmpIfComparisonResultIsGreaterOrEqual()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfComparisonResultIsLesser",
        commands_factory=lambda: [JmpIfComparisonResultIsLesser()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfVarEqualsConst",
        commands_factory=lambda: [JmpIfVarEqualsConst()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfVarNotEqualsConst",
        commands_factory=lambda: [JmpIfVarNotEqualsConst()],
        expected_bytes=[],
    ),
    Case(
        label="CreatePacketAtObjectCoords",
        commands_factory=lambda: [CreatePacketAtObjectCoords()],
        expected_bytes=[],
    ),
    Case(
        label="CreatePacketAt7010",
        commands_factory=lambda: [CreatePacketAt7010()],
        expected_bytes=[],
    ),
    Case(
        label="CreatePacketAt7010WithEvent",
        commands_factory=lambda: [CreatePacketAt7010WithEvent()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfMarioOnObject",
        commands_factory=lambda: [JmpIfMarioOnObject()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfMarioOnAnObjectOrNot",
        commands_factory=lambda: [JmpIfMarioOnAnObjectOrNot()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfObjectInAir",
        commands_factory=lambda: [JmpIfObjectInAir()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfObjectInSpecificLevel",
        commands_factory=lambda: [JmpIfObjectInSpecificLevel()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfObjectInCurrentLevel",
        commands_factory=lambda: [JmpIfObjectInCurrentLevel()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfObjectNotInSpecificLevel",
        commands_factory=lambda: [JmpIfObjectNotInSpecificLevel()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfObjectTriggerEnabledInSpecificLevel",
        commands_factory=lambda: [JmpIfObjectTriggerEnabledInSpecificLevel()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfObjectTriggerDisabledInSpecificLevel",
        commands_factory=lambda: [JmpIfObjectTriggerDisabledInSpecificLevel()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfObjectIsUnderwater",
        commands_factory=lambda: [JmpIfObjectIsUnderwater()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfObjectActionScriptIsRunning",
        commands_factory=lambda: [JmpIfObjectActionScriptIsRunning()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfObjectsAreLessThanXYStepsApart",
        commands_factory=lambda: [JmpIfObjectsAreLessThanXYStepsApart()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfObjectsAreLessThanXYStepsApartSameZCoord",
        commands_factory=lambda: [JmpIfObjectsAreLessThanXYStepsApartSameZCoord()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfMarioInAir",
        commands_factory=lambda: [JmpIfMarioInAir()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAudioMemoryIsAtLeast",
        commands_factory=lambda: [JmpIfAudioMemoryIsAtLeast()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAudioMemoryEquals",
        commands_factory=lambda: [JmpIfAudioMemoryEquals()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfDialogOptionBSelected",
        commands_factory=lambda: [JmpIfDialogOptionBSelected()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfDialogOptionBOrCSelected",
        commands_factory=lambda: [JmpIfDialogOptionBOrCSelected()],
        expected_bytes=[],
    ),
    #
    # Embedded action queue tests
    #
    Case(
        label="ActionQueueAsync",
        commands_factory=lambda: [ActionQueueAsync()],
        expected_bytes=[],
    ),
    Case(
        label="ActionQueueSync",
        commands_factory=lambda: [ActionQueueSync()],
        expected_bytes=[],
    ),
    Case(
        label="StartAsyncEmbeddedActionScript",
        commands_factory=lambda: [StartAsyncEmbeddedActionScript()],
        expected_bytes=[],
    ),
    Case(
        label="StartSyncEmbeddedActionScript",
        commands_factory=lambda: [StartSyncEmbeddedActionScript()],
        expected_bytes=[],
    ),
    #
    # Non-embedded action queue tests
    #
    Case(
        "NEAQ already in desired position",
        commands_factory=lambda: [
            StopSound(),
            StopSound(),
            StopSound(),
            NonEmbeddedActionQueue(
                required_offset=0x03, subscript=[A_AddConstToVar(PRIMARY_TEMP_700C, 10)]
            ),
        ],
        expected_bytes=[0x9B, 0x9B, 0x9B, 0xAD, 0x0A, 0x00],
    ),
    Case(
        "NEAQ is too early, inserts dummy commands to make up the difference",
        commands_factory=lambda: [
            StopSound(),
            NonEmbeddedActionQueue(
                required_offset=0x05, subscript=[A_AddConstToVar(PRIMARY_TEMP_700C, 10)]
            ),
        ],
        expected_bytes=[0x9B, 0x9B, 0x9B, 0x9B, 0x9B, 0xAD, 0x0A, 0x00],
    ),
    Case(
        "NEAQ should fail if it would be rendered after required offset",
        commands_factory=lambda: [
            StopSound(),
            StopSound(),
            NonEmbeddedActionQueue(
                required_offset=0x01, subscript=[A_AddConstToVar(PRIMARY_TEMP_700C, 10)]
            ),
        ],
        exception="too many commands in script 0 before non-embedded action queue",
        exception_type=ScriptBankTooLongException,
    ),
    Case(
        "background thread",
        commands_factory=lambda: [MoveScriptToBackgroundThread1()],
        expected_bytes=[0xFD, 0x41],
    ),
]


@pytest.mark.parametrize("case", test_cases, ids=lambda case: case.label)
def test_add(case: Case):
    if case.expected_bytes is not None and len(case.expected_bytes) == 0:
        return
    if case.exception or case.exception_type:
        with pytest.raises(case.exception_type) as exc_info:
            commands = case.commands_factory()
            script = EventScript(commands)
            bank = EventScriptBank(0x1E0000, 0x1E0002, 0x1EFFFF, [script])
            bank.render()
        if case.exception:
            assert case.exception in str(exc_info.value)
    elif case.expected_bytes is not None:
        commands = case.commands_factory()
        script = EventScript(commands)
        expected_bytes = bytearray(case.expected_bytes)
        bank = EventScriptBank(
            0x1E0000, 0x1E0002, 0x1E0002 + len(expected_bytes), [script]
        )
        assert bank.render() == bytearray([0x02, 0x00]) + expected_bytes
    else:
        raise "At least one of exception or expected_bytes needs to be set"
