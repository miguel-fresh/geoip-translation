<?php

function displayUsage()
{
    echo "Usage:\n";
    echo "    $ php download.php OPTIONS\n";
    echo "OPTIONS:\n";
    echo "   --license-key  : MaxMind license key";
    echo "   --output_path  : Path to destiny folder";
    echo "   --edition      : MaxMind database edition (e.g GeoLite2-City-CSV)";

}

$short_options = '';

$long_options = array(
    'license-key:',
    'output_path:',
    'edition:',
    'help',
);

$options = getopt($short_options, $long_options);
if (!$options['license-key'] | !$options['output_path'] | !$options['license-key']) return displayUsage();
var_dump($options);


require 'vendor/autoload.php';
// $client = new \tronovav\GeoIP2Update\Client(array(
//     'license_key' => 
// ))