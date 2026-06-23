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

# [Sync Mode Prompt]
#
# Prompt the user to choose between reset and update modes
# Reset mode removes existing target configurations before copying
# Update mode overwrites target files without deleting other target files

my $sync_mode; # sync mode
while (1) { # sync mode
    print "Please select synchronization mode:\n"; # sync mode
    print "  [1] Reset (removes target files/directories first, clean slate)\n"; # sync mode
    print "  [2] Update (overwrites changed files, preserves target-specific settings)\n"; # sync mode
    print "Selection (1 or 2): "; # sync mode
    my $input = <STDIN>; # sync mode
    if (defined $input) { # sync mode
        chomp($input); # sync mode
        if ($input eq '1' or $input eq '2') { # sync mode
            $sync_mode = $input; # sync mode
            last; # sync mode
        } # sync mode
    } # sync mode
    print "Invalid entry, please input 1 or 2\n\n"; # sync mode
} # sync mode

# Define the folders and files to sync
my @dirs_to_sync = ('.cursor', '.gemini', '.kiro', '.agents');
my @files_to_sync = ('GEMINI.md', '.ai-kiro.bat', '.ai-cursor.bat', '.ai-gemini.bat', '.ai-antigravity.bat', '.ai-copilot.bat');
 
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

    # [Past version]
    #
    #     foreach my $d (@dirs_to_sync) { # sync mode
    #         my $target_path = "$target_dir/$d"; # sync mode
    #         if (-d $target_path) { # sync mode
    #             rmtree($target_path); # sync mode
    #         } # sync mode
    #     } # sync mode
    #     
    #     foreach my $f (@files_to_sync) { # sync mode
    #         my $target_path = "$target_dir/$f"; # sync mode
    #         if (-e $target_path) { # sync mode
    #             unlink($target_path); # sync mode
    #         } # sync mode
    #     } # sync mode
    #
    # Replaced code that unconditionally deleted target folders and files
    # The new logic checks if the user selected a reset mode before deleting
    # This prevents unintended deletion of local repository-specific settings

    if ($sync_mode eq '1') { # sync mode
        print "Clearing old configurations...\n"; # sync mode
        foreach my $d (@dirs_to_sync) { # sync mode
            my $target_path = "$target_dir/$d"; # sync mode
            if (-d $target_path) { # sync mode
                rmtree($target_path); # sync mode
            } # sync mode
        } # sync mode
        
        foreach my $f (@files_to_sync) { # sync mode
            my $target_path = "$target_dir/$f"; # sync mode
            if (-e $target_path) { # sync mode
                unlink($target_path); # sync mode
            } # sync mode
        } # sync mode
    } # sync mode

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
