subroutine step1()
    implicit none
    real(8) :: U(0:18, 0:18), V(0:18, 0:18)
    real(8) :: grid_X(17, 17), grid_Y(17, 17)

    call read_uv(U, V)
    print *, U(0, :)
    call read_grid(grid_X, grid_Y)

end subroutine
