<?php

function displayUsage()
{
    echo "Usage:\n";
    echo "    $ php download.php OPTIONS\n";
    echo "OPTIONS:\n";
    echo "   --license-key  : MaxMind license key";
    echo "   --output_path  : Path to destiny folder";
    echo "   --edition      : MaxMind database edition (e.g GeoLite2-City-CSV)";
    return;
}

$short_options = '';

$long_options = array(
    'license-key:',
    'output_path:',
    'edition:',
    'help',
);

$options = getopt($short_options, $long_options);
foreach ($long_options as $long_option) {
    if (isset($options[$long_option])) return displayUsage();
}

var_dump($options);


require 'vendor/autoload.php';
// $client = new \tronovav\GeoIP2Update\Client(array(
//     'license_key' => 
// ))