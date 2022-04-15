#! /usr/bin/perl

#this script will convert a txt file to all lowercase letters
use strict;
use warnings;

open(my $in, "<", "mysql_INSTALL-SOURCE.txt") or die "Can't open file: $!";
open(my $out, ">", "output/lowercase.txt") or die "Can't open file: $!";

while(my $line = <$in>)
{
  $line =~ tr/[A-Z]/[a-z]/;

  print $out $line;
}

close $in or die "$in: $!";
close $out or die "$in: $!";
