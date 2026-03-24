Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;
public class Displays {
    [DllImport("user32.dll")]
    public static extern int GetDisplayConfigBufferSizes(uint flags, out uint numPathArrayElements, out uint numModeArrayElements);
    [DllImport("user32.dll")]
    public static extern int QueryDisplayConfig(uint flags, ref uint numPathArrayElements, [Out] DISPLAYCONFIG_PATH_INFO[] pathArray, ref uint numModeArrayElements, [Out] DISPLAYCONFIG_MODE_INFO[] modeArray, IntPtr currentTopologyId);

    [StructLayout(LayoutKind.Sequential)]
    public struct DISPLAYCONFIG_PATH_INFO {
        public DISPLAYCONFIG_PATH_SOURCE_INFO sourceInfo;
        public DISPLAYCONFIG_PATH_TARGET_INFO targetInfo;
        public uint flags;
    }
    [StructLayout(LayoutKind.Sequential)]
    public struct DISPLAYCONFIG_PATH_SOURCE_INFO {
        public LUID adapterId;
        public uint id;
        public uint modeInfoIdx;
        public uint statusFlags;
    }
    [StructLayout(LayoutKind.Sequential)]
    public struct DISPLAYCONFIG_PATH_TARGET_INFO { public LUID adapterId; public uint id; public uint modeInfoIdx; private uint a; public uint statusFlags; }
    [StructLayout(LayoutKind.Sequential)]
    public struct DISPLAYCONFIG_MODE_INFO { public uint infoType; public uint id; public LUID adapterId; public object modeInfo; }
    [StructLayout(LayoutKind.Sequential)]
    public struct LUID { public uint LowPart; public int HighPart; }
    public const uint QDC_ALL_PATHS = 1;
}
"@

[Displays]::GetDisplayConfigBufferSizes([Displays]::QDC_ALL_PATHS, [ref] $numPathArrayElements, [ref] $numModeArrayElements)
$pathArray = New-Object Displays.DISPLAYCONFIG_PATH_INFO[] $numPathArrayElements
$modeArray = New-Object Displays.DISPLAYCONFIG_MODE_INFO[] $numModeArrayElements
[Displays]::QueryDisplayConfig([Displays]::QDC_ALL_PATHS, [ref] $numPathArrayElements, $pathArray, [ref] $numModeArrayElements, $modeArray, [IntPtr]::Zero)

Write-Host "--- Monitores Encontrados ---" -ForegroundColor Green
foreach ($path in $pathArray) {
    if ($path.targetInfo.id -ne 0) {
        $ativo = if($path.flags -band 1) { "Sim" } else { "Não" }
        Write-Host "Monitor com ID de Fonte: $($path.sourceInfo.id) | Status: Ativo=`"$ativo`""
    }
}
Write-Host "--------------------------" -ForegroundColor Green
Read-Host "Pressione ENTER para sair"