"""Constants related to IStorage and related interfaces

This file was generated by h2py from d:\msdev\include\objbase.h
then hand edited, a few extra constants added, etc.
"""

STGC_DEFAULT = 0
STGC_OVERWRITE = 1
STGC_ONLYIFCURRENT = 2
STGC_DANGEROUSLYCOMMITMERELYTODISKCACHE = 4
STGC_CONSOLIDATE = 8

STGTY_STORAGE = 1
STGTY_STREAM = 2
STGTY_LOCKBYTES = 3
STGTY_PROPERTY = 4
STREAM_SEEK_SET = 0
STREAM_SEEK_CUR = 1
STREAM_SEEK_END = 2

LOCK_WRITE = 1
LOCK_EXCLUSIVE = 2
LOCK_ONLYONCE = 4

# Generated as from here.

CWCSTORAGENAME = 32
STGM_DIRECT = 0x00000000
STGM_TRANSACTED = 0x00010000
STGM_SIMPLE = 0x08000000
STGM_READ = 0x00000000
STGM_WRITE = 0x00000001
STGM_READWRITE = 0x00000002
STGM_SHARE_DENY_NONE = 0x00000040
STGM_SHARE_DENY_READ = 0x00000030
STGM_SHARE_DENY_WRITE = 0x00000020
STGM_SHARE_EXCLUSIVE = 0x00000010
STGM_PRIORITY = 0x00040000
STGM_DELETEONRELEASE = 0x04000000
STGM_NOSCRATCH = 0x00100000
STGM_CREATE = 0x00001000
STGM_CONVERT = 0x00020000
STGM_FAILIFTHERE = 0x00000000
STGM_NOSNAPSHOT = 0x00200000
ASYNC_MODE_COMPATIBILITY = 0x00000001
ASYNC_MODE_DEFAULT = 0x00000000
STGTY_REPEAT = 0x00000100
STG_TOEND = 0xFFFFFFFF
STG_LAYOUT_SEQUENTIAL = 0x00000000
STG_LAYOUT_INTERLEAVED = 0x00000001

## access rights used with COM server ACL's
COM_RIGHTS_EXECUTE = 1
COM_RIGHTS_EXECUTE_LOCAL = 2
COM_RIGHTS_EXECUTE_REMOTE = 4
COM_RIGHTS_ACTIVATE_LOCAL = 8
COM_RIGHTS_ACTIVATE_REMOTE = 16

STGFMT_DOCUMENT = 0
STGFMT_STORAGE = 0
STGFMT_NATIVE = 1
STGFMT_FILE = 3
STGFMT_ANY = 4
STGFMT_DOCFILE = 5

PID_DICTIONARY = 0
PID_CODEPAGE = 1
PID_FIRST_USABLE = 2
PID_FIRST_NAME_DEFAULT = 4095

PID_LOCALE = -2147483648
PID_MODIFY_TIME = -2147483647
PID_SECURITY = -2147483646
PID_BEHAVIOR = -2147483645
PID_ILLEGAL = -1
PID_MIN_READONLY = -2147483648
PID_MAX_READONLY = -1073741825

## DiscardableInformation
PIDDI_THUMBNAIL = 0x00000002

## SummaryInformation
PIDSI_TITLE = 2
PIDSI_SUBJECT = 3
PIDSI_AUTHOR = 4
PIDSI_KEYWORDS = 5
PIDSI_COMMENTS = 6
PIDSI_TEMPLATE = 7
PIDSI_LASTAUTHOR = 8
PIDSI_REVNUMBER = 9
PIDSI_EDITTIME = 10
PIDSI_LASTPRINTED = 11
PIDSI_CREATE_DTM = 12
PIDSI_LASTSAVE_DTM = 13
PIDSI_PAGECOUNT = 14
PIDSI_WORDCOUNT = 15
PIDSI_CHARCOUNT = 16
PIDSI_THUMBNAIL = 17
PIDSI_APPNAME = 18
PIDSI_DOC_SECURITY = 19

## DocSummaryInformation
PIDDSI_CATEGORY = 2
PIDDSI_PRESFORMAT = 3
PIDDSI_BYTECOUNT = 4
PIDDSI_LINECOUNT = 5
PIDDSI_PARCOUNT = 6
PIDDSI_SLIDECOUNT = 7
PIDDSI_NOTECOUNT = 8
PIDDSI_HIDDENCOUNT = 9
PIDDSI_MMCLIPCOUNT = 10
PIDDSI_SCALE = 11
PIDDSI_HEADINGPAIR = 12
PIDDSI_DOCPARTS = 13
PIDDSI_MANAGER = 14
PIDDSI_COMPANY = 15
PIDDSI_LINKSDIRTY = 16


## MediaFileSummaryInfo
PIDMSI_EDITOR = 2
PIDMSI_SUPPLIER = 3
PIDMSI_SOURCE = 4
PIDMSI_SEQUENCE_NO = 5
PIDMSI_PROJECT = 6
PIDMSI_STATUS = 7
PIDMSI_OWNER = 8
PIDMSI_RATING = 9
PIDMSI_PRODUCTION = 10
PIDMSI_COPYRIGHT = 11

## PROPSETFLAG enum
PROPSETFLAG_DEFAULT = 0
PROPSETFLAG_NONSIMPLE = 1
PROPSETFLAG_ANSI = 2
PROPSETFLAG_UNBUFFERED = 4
PROPSETFLAG_CASE_SENSITIVE = 8

## STGMOVE enum
STGMOVE_MOVE = 0
STGMOVE_COPY = 1
STGMOVE_SHALLOWCOPY = 2
