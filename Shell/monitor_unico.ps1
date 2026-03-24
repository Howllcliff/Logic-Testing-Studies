function Set-Display {
    param(
        [string]$DisplayId,
        [switch]$Primary,
        [switch]$Enable,
        [switch]$Disable,
        [string]$ExtendTo
    )

    $user32 = Add-Type -MemberDefinition '
        [DllImport("user32.dll")]
        public static extern int SetDisplayConfig(uint numPathArrayElements, IntPtr pathArray, uint numModeArrayElements, IntPtr modeArray, uint flags);
    ' -Name "User32" -Namespace "Win32" -PassThru

    if ($Enable) {
        $flags = 0x00000001;
        $user32::SetDisplayConfig(0, [IntPtr]::Zero, 0, [IntPtr]::Zero, $flags)
    }

    if ($Disable) {
        Write-Warning "A desativação individual é complexa. Este script vai desativar TODOS os monitores secundários."
        $flags = 0x00000001; # SDC_APPLY
        C:\Windows\System32\DisplaySwitch.exe /internal
    }
}

Write-Host "Ativando apenas o monitor principal..."
C:\Windows\System32\DisplaySwitch.exe /internal
Write-Host "Concluído."