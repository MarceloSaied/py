
# configure this: comma-separated list of Servers
$server="test"
$servers = 'ctcvw6017' , 'ctcvw6018'  , 'ctcvw6019' , 'ctcvw6020' , 'ctcvw6021' , 'ctcvw6022' , 'ctcvw6080' , 'ctcvw6081' , 'ctcvw6082'

foreach ($server in $servers) {
    "---------"
    $server
}