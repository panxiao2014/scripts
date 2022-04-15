#! /usr/bin/perl

#This script will count each letter used in a document
use strict;
use warnings;

my @charArray;

for(my $i=0; $i<26; $i++)
{
  open(my $in, "<", "mysql_INSTALL-SOURCE.txt") or die "Can't open file: $!";

  my $countLetter = 0;
  my $charNum = $i + 97;
  my $char = chr($charNum);

  while (my $line = <$in>)
  {
    if(my @wArray = $line =~ m/$char/ig)
    {
      $countLetter += @wArray;
    }
  }

  print "$char: $countLetter\n";

  $charArray[$i] = $countLetter;

  close $in or die "$in: $!";
}

#my @sortArray = sort {$a <=> $b} @charArray;
#
#foreach (@sortArray)
#{
#  print "$_\n";
#}

