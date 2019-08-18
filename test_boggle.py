import unittest
import boggle

class testBoggle(unittest.TestCase):
    """
    Our test suit fir boggle solver
    """
    def test_can_create_an_empty_grig(self):
        """
        test to see if we can create an empty grid
        """
        grid = boggle.make_grid(0,0)
        self.assertEqual(len(grid),0)
    def test_grid_is_width_times_height(self):
        """
        test to ensure total grid size is equal to width * height
        """
        grid = boggle.make_grid(2,3)

        self.assertEqual(len(grid),6)

    def test_grid_coordiantes(self):
        """
        test to ensure all coordiantes in the grid can be accessed
        """
        grid=boggle.make_grid(2, 2)
        self.assertIn((0,0),grid)
        self.assertIn((0,1),grid)
        self.assertIn((1,0),grid)
        self.assertIn((1,1),grid)
        self.assertNotIn((2,2),grid)