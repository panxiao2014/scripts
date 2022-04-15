#! /usr/bin/perl

#this file will write the words of different length to different files
use strict;
use warnings;

#create multiple files:
my $fileName = "_letters";

for(my $i=1; $i<=20; $i++)
{
  open(my $in, "<", "rfc3261(SIP).txt") or die "Can't open file: $!";

  my $file = "output/".$i.$fileName.".txt";

  open(my $out, ">", "$file") or die "Can't open file: $!";

  my $countLines = 0;

  while (my $line = <$in>)
  {
    if(my @wArray = $line =~ m/\b[a-zA-Z]{$i}\b/g)
    {
      foreach (@wArray)
      {
        print $out "$_\n";

        $countLines++;
      }
    }
  }

  print "$i letters: $countLines\n";

  close $in or die "$in: $!";
  close $out or die "$in: $!";
}
