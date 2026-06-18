#!/usr/bin/env perl
use strict;
use warnings;
use Cwd qw(abs_path getcwd);
use File::Copy qw(copy);
use File::Path qw(rmtree make_path);

print "===========================================================================\n";
print "AI Environment Synchronization Script (Perl)\n";
print "===========================================================================\n\n";

my $current_dir = abs_path(getcwd());
print "Current Directory: $current_dir\n\n";

# Define the folders and files to sync
my @dirs_to_sync = ('.cursor', '.gemini', '.kiro');
my @files_to_sync = ('GEMINI.md', '.ai-kiro.bat', '.ai-cursor.bat', '.ai-gemini.bat');
 
# Custom recursive directory copy to avoid requiring non-core CPAN modules
sub dircopy {
    my ($src, $dest) = @_;
    return unless -d $src;
    
    make_path($dest) unless -d $dest;
    
    opendir(my $dh, $src) or do {
        warn "Cannot open $src: $!\n";
        return;
    };
    
    while (my $item = readdir($dh)) {
        next if $item eq '.' or $item eq '..';
        my $src_item = "$src/$item";
        my $dest_item = "$dest/$item";
        
        if (-d $src_item) {
            dircopy($src_item, $dest_item);
        } else {
            copy($src_item, $dest_item) or warn "Failed to copy $src_item to $dest_item: $!\n";
        }
    }
    closedir($dh);
}

print "Searching for sibling directories matching: ../_*\n";
my @siblings = glob("../_*");

foreach my $sibling (@siblings) {
    next unless -d $sibling;
    
    my $target_dir = abs_path($sibling);
    next unless defined $target_dir; # skip if absolute path resolution fails

    # Skip if it's the current directory
    if ($target_dir eq $current_dir) {
        next;
    }

    print "\n--------------------------------------------------\n";
    print "Processing: $target_dir\n";
    print "--------------------------------------------------\n";

    # 1. Delete existing target files and folders
    print "Clearing old configurations...\n";
    foreach my $d (@dirs_to_sync) {
        my $target_path = "$target_dir/$d";
        if (-d $target_path) {
            rmtree($target_path);
        }
    }
    
    foreach my $f (@files_to_sync) {
        my $target_path = "$target_dir/$f";
        if (-e $target_path) {
            unlink($target_path);
        }
    }

    # 2. Copy source to target
    print "Copying new configurations...\n";
    foreach my $d (@dirs_to_sync) {
        my $src_path = "$current_dir/$d";
        my $target_path = "$target_dir/$d";
        if (-d $src_path) {
            dircopy($src_path, $target_path);
        }
    }

    foreach my $f (@files_to_sync) {
        my $src_path = "$current_dir/$f";
        my $target_path = "$target_dir/$f";
        if (-e $src_path) {
            copy($src_path, $target_path) or warn "Could not copy $f to $target_dir: $!\n";
        }
    }

    print "[OK] Synced to $target_dir\n";
}

print "\n===========================================================================\n";
print "Synchronization complete.\n";
print "===========================================================================\n";
