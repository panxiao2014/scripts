#! /usr/bin/perl
use strict;
use warnings;
use Image::PNG;

my $png = Image::PNG->new ();
$png->read_file ("../Pictures/notes_Vertical2.png");

printf "Your PNG is %d x %d\n", $png->width, $png->height;
