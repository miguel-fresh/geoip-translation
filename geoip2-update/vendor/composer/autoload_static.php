<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInita18f88d92854b50c0b3fc30494e97a1d
{
    public static $prefixLengthsPsr4 = array (
        't' => 
        array (
            'tronovav\\GeoIP2Update\\' => 22,
        ),
    );

    public static $prefixDirsPsr4 = array (
        'tronovav\\GeoIP2Update\\' => 
        array (
            0 => __DIR__ . '/../..' . '/src',
        ),
    );

    public static $classMap = array (
        'Composer\\InstalledVersions' => __DIR__ . '/..' . '/composer/InstalledVersions.php',
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->prefixLengthsPsr4 = ComposerStaticInita18f88d92854b50c0b3fc30494e97a1d::$prefixLengthsPsr4;
            $loader->prefixDirsPsr4 = ComposerStaticInita18f88d92854b50c0b3fc30494e97a1d::$prefixDirsPsr4;
            $loader->classMap = ComposerStaticInita18f88d92854b50c0b3fc30494e97a1d::$classMap;

        }, null, ClassLoader::class);
    }
}
