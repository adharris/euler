

import click

@click.command('91')
@click.option('--verbose', '-v', count=True)
def problem_091(verbose):
    """Right triangles with integer coordinates.

    The points P (_x_1, _y_1) and Q (_x_2, _y_2) are plotted at integer co-
    ordinates and are joined to the origin, O(0,0), to form ΔOPQ.
    
    ![](project/images/p091_1.gif)  
    
    There are exactly fourteen triangles containing a right angle that can be
    formed when each co-ordinate lies between 0 and 2 inclusive; that is,  
    0 ≤ _x_1, _y_1, _x_2, _y_2 ≤ 2.
    
    ![](project/images/p091_2.gif)  
    
    Given that 0 ≤ _x_1, _y_1, _x_2, _y_2 ≤ 50, how many right triangles can
    be formed?
    
    """
