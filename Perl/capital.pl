#! /usr/bin/perl

#this script will convert a txt file to all capital letters
use strict;
use warnings;

open(my $in, "<", "mysql_INSTALL-SOURCE.txt") or die "Can't open file: $!";
open(my $out, ">", "output/capital.txt") or die "Can't open file: $!";

while(my $line = <$in>)
{
  #find all non capital leeters, and convert them to capital:
  $line =~ tr/[a-z]/[A-Z]/;

  print $out $line;
}

close $in or die "$in: $!";
close $out or die "$in: $!";
