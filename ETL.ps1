## PowerShell ETL: Breweries

$file=(get-content C:\Users\...\...\target\shakeshack.csv)

set-variable -name "iterations" -value ($file | Measure-Object -Line)

$variable = 0

write-output "insert into locations (latitude,longitude,location) VALUES ">C:\Users\G\OneDrive\Tech\ETL\output\shakeshack.sql

While ($variable -LT $iterations.lines)

{
set-variable -name "target" -value ( $file | Select -Index $variable )
set-variable -name "latitude" -value ( $target -split ',' |select -index 0 )
set-variable -name "longitude" -value ( $target -split ',' |select -index 1 )
set-variable -name "location" -value ( $target -split ',' |select -index 2 )
$location = $location -replace "'",""
write-output "('$latitude','$longitude','$location')," >>C:\Users\G\OneDrive\Tech\ETL\output\shakeshack.sql

$variable++
}
