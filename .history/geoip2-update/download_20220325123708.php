<?php

require 'vendor/autoload.php';

$short_options = '';

$long_options = array(
    'license-key:',
    'output_path:',
    'edition:',
    'help',
);

$options = getopt($short_options, $long_options);
var_dump($options);

// $client = new \tronovav\GeoIP2Update\Client(array(
//     'license_key' => 
// ))