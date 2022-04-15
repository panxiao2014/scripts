#! /usr/bin/perl

#This script will create mysql data to load to the database table 
use strict;
use warnings;
use String::Random;
use Data::Random qw(:all);

#open data file, ">>" allows append mode
open(my $file, ">", "data.txt") or die "Can't open file: $!";

#print $file "\\N	joho	f	1977-12-23\n";

for (my $i = 0; $i <= 1000000; $i++) {
  #random number between 1 and 20:
  my $random_len = int(rand(19)) + 1;

  #random name:
  my $foo = new String::Random;
  my $regString = '[a-zA-Z]{'.$random_len.'}';
  my $name = $foo->randregex($regString);

  #random sex:
  my $sex = 'm';
  my $random_number = int(rand(1000));
  if($random_number % 2 == 0){
    $sex = 'f';
  }

  #random birth:
  my $birth = rand_date( min => '1978-9-21', max => 'now' );

  #print $name . "\n";
  #print $sex . "\n";
  #print $birth . "\n\n";

  my $insertString = "\\N	" . $name . "	". $sex . "	" . $birth . "\n";
  #print $insertString;

  #write to the file:
  print $file $insertString;
}

#close file:
close $file or die "$!";
