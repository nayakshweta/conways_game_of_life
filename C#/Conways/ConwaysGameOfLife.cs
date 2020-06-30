using System;

namespace Conways
{
    public class ConwaysGameOfLife
    {
        public static void Main()
        {
            Console.WriteLine("Welcome to Conways Game of Life!");

            string filename = "../inputfile.txt"; 
            Console.WriteLine("We will now read the grid from the file {0}", filename);
            
            string[] FileLines = Grid.ReadInputGridFromFile("/home/shwetn/workspace/csharpprac/conways/conways_game_of_life/C#/Conways/inputfile.txt");

            var grid = new Grid(4, 8, FileLines);
            
            Console.WriteLine("Determining the next grid...");
            Grid nextGrid = grid.DetermineNextGrid();

            Console.WriteLine(nextGrid.ToString());
        }

    }
}
