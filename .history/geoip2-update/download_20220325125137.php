<?php


function displayUsage()
{
    echo "Usage:\n";
    echo "    $ php download.php OPTIONS\n";
    echo "OPTIONS:\n";
    echo "   --license-key  : MaxMind license key\n";
    echo "   --output-path  : Path to destiny folder\n";
    echo "   --edition      : MaxMind database edition (e.g GeoLite2-City-CSV)\n";
    return;
}

$short_options = '';

$long_options = array(
    'license-key:',
    'output-path:',
    'edition:',
    'help',
);

$options = getopt($short_options, $long_options);

if (isset($options['help'])) return displayUsage();
foreach ($long_options as $long_option) {
    if (
        !isset($options[$long_option])
        && $long_option !== 'help'
    ) 
    {
        echo $long_option;
    }
}




require 'vendor/autoload.php';
// $client = new \tronovav\GeoIP2Update\Client(array(
//     'license_key' => 
// ))