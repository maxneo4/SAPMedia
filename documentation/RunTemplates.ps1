Import-Module NeoMaxTemplates
Get-DataFromClipboard
$template = Get-ContentFromFile "$PSScriptRoot/template_selectReport.txt"
Format-DataExpand -template $template | Set-ToClipboard