<?php

require 'vendor/autoload.php';

$short_options = 'lk:op:ed:';

$long_options = array(
    'license-key:',
    'output_path:',
    'edition:',
);

$options = getopt($short_options, $long_options);

// $client = new \tronovav\GeoIP2Update\Client(array(
//     'license_key' => 
// ))