cls
function import-excel($data)
{
    Invoke-RestMethod -Method Post -ContentType 'application/json' -Body $data -Uri 'http://127.0.0.1:8080/excel/import'
}

 $body = @{
    file_path='D:\GitHub\SAPMedia\src\services\test\Global Master Deck ENG Articles Q4.xlsm'
}

import-excel (ConvertTo-Json $body)