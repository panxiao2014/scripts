#! /usr/bin/perl
use strict;
use warnings;
use String::Random;
use Data::Random qw(:all);

#random number between 1 and 20:
my $random_len = int(rand(19)) + 1;


#random string:
my $foo = new String::Random;
my $regString='[a-zA-Z]{'.$random_len.'}';


#random sex:
my $sex = 'm';
my $random_number = int(rand(1000));
if($random_number % 2 == 0){
  $sex = 'f';
}

#random date:
my $date = rand_date( min => '1978-9-21', max => 'now' );

#output:
print $foo->randregex($regString) . "\n";
print $random_number . $sex . "\n";
print $date . "\n";


