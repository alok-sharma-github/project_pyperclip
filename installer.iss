[Setup]
AppName=Clipboard Summarizer
AppVersion=1.0
DefaultDirName={userdesktop}\Clipboard Summarizer
DefaultGroupName=Clipboard Summarizer
OutputBaseFilename=ClipboardSummarizerInstaller
Compression=lzma
SolidCompression=yes
DisableProgramGroupPage=no
DiskSpanning=yes 

[Files]
Source: "dist\project_pyperclip.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "clipboard.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{userdesktop}\Clipboard Summarizer"; Filename: "{app}\project_pyperclip.exe"
Name: "{group}\Clipboard Summarizer"; Filename: "{app}\project_pyperclip.exe"

[Run]
Filename: "{app}\project_pyperclip.exe"; Description: "Launch Clipboard Summarizer"; Flags: nowait postinstall skipifsilent
Filename: "cmd.exe"; Parameters: "/c echo Installation Complete! && pause"; Flags: shellexec runhidden
