#include "dataset.au3"
_DatasetFixList(@scriptDir &"\list.txt", "es", true)
if @error then
msgbox(16, "error", "Code: " &@error)
Else
msgbox(0, "Success", "The transcription has ben fixed.")
EndIf
