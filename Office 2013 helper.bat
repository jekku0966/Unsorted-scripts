echo Office 2013 Serial helper > %COMPUTERNAME%.txt
echo © Niklas Jerva 2014 >> %COMPUTERNAME%.txt
echo V1.5 >> %COMPUTERNAME%.txt
echo   >> %COMPUTERNAME%.txt
echo Tietokone: >> %COMPUTERNAME%.txt
hostname >> %COMPUTERNAME%.txt
echo   >> %COMPUTERNAME%.txt

SET _office14="C:\Program Files\Microsoft Office\Office14\OSPP.VBS"
SET _office1432="C:\Program Files (x86)\Microsoft Office\Office14\OSPP.VBS"
SET _office15="C:\Program Files\Microsoft Office\Office15\OSPP.VBS"
SET _office1532="C:\Program Files (x86)\Microsoft Office\Office15\OSPP.VBS"

IF NOT EXIST %_office14% (
GOTO S1
) ELSE (
cscript %_office14% /dstatus >> %COMPUTERNAME%.txt
GOTO FINAL
)

:S1
IF NOT EXIST %_office1432% (
GOTO S2
) ELSE (
cscript %_office1432% /dstatus >> %COMPUTERNAME%.txt
GOTO FINAL
)

:S2
IF NOT EXIST %_office15% (
GOTO S3
) ELSE (
cscript %_office15% /dstatus >> %COMPUTERNAME%.txt
GOTO FINAL
)

:S3
IF NOT EXIST %_office1532% (
echo Officea ei ole asennettuna tähän koneeseen. >> %COMPUTERNAME%.txt
) ELSE (
cscript %_office1532% /dstatus >> %COMPUTERNAME%.txt
GOTO FINAL
)

:FINAL
start NOTEPAD %COMPUTERNAME%.txt