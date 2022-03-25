<?php

require 'vendor/autoload.php';

$long_options = array(
    'license-key:',
    'output_path:',
    'edition:',
);


$client = new \tronovav\GeoIP2Update\Client(array(
    'license_key' => 
))