#! /usr/bin/perl

use warnings;
use strict;

use PDL;

my ($x, $y, $d) = rcols '-';

my $xdim = $x->max;
my $ydim = $y->max;

$d->reshape($xdim, $ydim);
wfits($d, '-');
