#! /usr/bin/perl
use strict;
use warnings;

open(my $in, "<", "ShowTable.pm") or die "Can't open file: $!";
open(my $out, ">", "result.pm") or die "Can't open file: $!";

while (my $line = <$in>)
{
  #practice regular expression:
  if($line =~ /\sand\s/)
  {
    $line =~ s/(\s)and(\s)/$1AND$2/g;
  }

  print $out $line;
}

close $in or die "$in: $!";
close $out or die "$out: $!";

print "\n";
