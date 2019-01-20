def toh(num_of_disks, start_peg=1, end_peg=3):
    """Towers of hanoi problem."""
    if num_of_disks:
        toh(num_of_disks - 1, start_peg, 6-start_peg-end_peg)
        print('move disk %d form peg %d to peg %d'
              % (num_of_disks, start_peg, end_peg))
        toh(num_of_disks - 1, 6-start_peg-end_peg, end_peg)